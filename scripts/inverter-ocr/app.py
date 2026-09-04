"""
Inverter OCR Service
Fetches frames from go2rtc, enhances them, runs multi-threshold OCR,
and exposes battery stats via REST API for Home Assistant.

The inverter LCD shows white text on a blue background:
  BATTERY GROUP
  BATTERY VOLT  132.4V
  BATTERY STATUS  092%
  DI+000.0A  DI-000.0A
"""

import io
import re
import time
import logging
from collections import Counter

import cv2
import numpy as np
import requests
import pytesseract
from flask import Flask, jsonify, send_file

app = Flask(__name__)
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger(__name__)

# Configuration
FRAME_URL = "http://192.168.0.199:31060/api/frame.jpeg?src=go2rtc"
CACHE_TTL = 30  # seconds between frame fetches
FETCH_TIMEOUT = 10  # seconds

# Cache
_cache = {
    "stats": {},
    "raw_frame": None,
    "enhanced_frame": None,
    "raw_text": "",
    "last_update": 0,
    "error": None,
}


def fetch_frame():
    """Fetch a JPEG frame from go2rtc."""
    resp = requests.get(FRAME_URL, timeout=FETCH_TIMEOUT)
    resp.raise_for_status()
    img_array = np.frombuffer(resp.content, dtype=np.uint8)
    frame = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    if frame is None:
        raise ValueError("Failed to decode frame")
    return frame


def enhance_frame(frame):
    """
    Enhance frame for visual debugging (single best threshold).
    Returns a clean B&W image for the /api/frame/enhanced endpoint.
    """
    if len(frame.shape) == 3:
        lab = cv2.cvtColor(frame, cv2.COLOR_BGR2LAB)
        gray = lab[:, :, 0]
    else:
        gray = frame

    h, w = gray.shape
    # Crop to LCD text area (remove camera overlay text)
    roi = gray[int(h * 0.15):int(h * 0.85), int(w * 0.07):int(w * 0.93)]

    # Upscale 6x for better OCR
    scale = 6
    big = cv2.resize(roi, (roi.shape[1] * scale, roi.shape[0] * scale),
                     interpolation=cv2.INTER_LANCZOS4)

    # CLAHE for contrast
    clahe = cv2.createCLAHE(clipLimit=4.0, tileGridSize=(16, 16))
    enhanced = clahe.apply(big)

    # Sharpen (unsharp mask)
    gauss = cv2.GaussianBlur(enhanced, (0, 0), 2)
    sharp = cv2.addWeighted(enhanced, 2.0, gauss, -1.0, 0)

    # Binary threshold at the sweet spot for this LCD
    _, bw = cv2.threshold(sharp, 160, 255, cv2.THRESH_BINARY)

    return bw


def multi_threshold_ocr(frame):
    """
    Run OCR at multiple threshold levels on both grayscale and LAB L-channel.
    Returns all OCR text combined for parsing.

    This approach is necessary because the LCD image is low-resolution and
    different threshold levels reveal different characters. By combining
    results from many thresholds, we can extract values reliably.
    """
    all_text = []

    # Prepare channels: grayscale and LAB L-channel
    if len(frame.shape) == 3:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        lab = cv2.cvtColor(frame, cv2.COLOR_BGR2LAB)
        l_chan = lab[:, :, 0]
        channels = [gray, l_chan]
    else:
        channels = [frame]

    for ch in channels:
        h, w = ch.shape
        # Crop to LCD text area
        roi = ch[int(h * 0.15):int(h * 0.85), int(w * 0.07):int(w * 0.93)]

        # Upscale 6x
        scale = 6
        big = cv2.resize(roi, (roi.shape[1] * scale, roi.shape[0] * scale),
                         interpolation=cv2.INTER_LANCZOS4)

        # CLAHE for contrast enhancement
        clahe = cv2.createCLAHE(clipLimit=4.0, tileGridSize=(16, 16))
        enhanced = clahe.apply(big)

        # Sharpen
        gauss = cv2.GaussianBlur(enhanced, (0, 0), 2)
        sharp = cv2.addWeighted(enhanced, 2.0, gauss, -1.0, 0)

        # Run OCR at multiple thresholds (the sweet spot varies per frame)
        for thresh in range(130, 200, 3):
            _, bw = cv2.threshold(sharp, thresh, 255, cv2.THRESH_BINARY)
            txt = pytesseract.image_to_string(bw, config="--oem 3 --psm 6")
            all_text.append(txt.upper())

    return "\n".join(all_text)


def parse_stats(combined_text):
    """
    Parse battery/inverter stats from multi-threshold OCR output.
    Uses voting (most common value) across all threshold results
    to get reliable readings.

    Expected values:
      - Battery voltage: 3-digit number with 1 decimal (e.g., 132.4)
      - Battery percent: 0-100 (e.g., 092 -> 92%)
      - Discharge/charge current: 3-digit.1-decimal (e.g., 000.0)
    """
    stats = {}

    # --- Battery Voltage ---
    # Look for patterns like "132.4" (2-3 digits, dot, 1 digit)
    # Filter to reasonable battery bank voltage range (20V - 200V)
    volt_matches = re.findall(r"(\d{2,3}\.\d)", combined_text)
    voltages = [float(v) for v in volt_matches if 20 < float(v) < 200]
    if voltages:
        # Use most frequently detected value
        stats["battery_voltage"] = Counter(voltages).most_common(1)[0][0]

    # --- Battery Percentage (SOC) ---
    # Look for XX% or 0XX% patterns
    pct_matches = re.findall(r"0?(\d{2,3})\s*%", combined_text)
    percents = [float(p) for p in pct_matches if 0 <= float(p) <= 100]
    if percents:
        stats["battery_percent"] = Counter(percents).most_common(1)[0][0]

    # Fallback: look for number near "STATUS" keyword
    if "battery_percent" not in stats:
        status_matches = re.findall(r"STAT\w*\s*0?(\d{2,3})", combined_text)
        percents2 = [float(p) for p in status_matches if 0 <= float(p) <= 100]
        if percents2:
            stats["battery_percent"] = Counter(percents2).most_common(1)[0][0]

    # --- Currents (DI+/DI-) ---
    # The LCD shows "DI+000.0A  DI-000.0A"
    # OCR might read DI, D1, OI, O1 etc.
    # Only match currents that appear near DI+/DI- context (not voltage)
    di_plus = re.findall(r"[DO][I1]\+\s*(\d{3}\.\d)", combined_text)
    di_minus = re.findall(r"[DO][I1][-]\s*(\d{3}\.\d)", combined_text)
    if di_plus:
        vals = [float(v) for v in di_plus
                if float(v) < 500
                and abs(float(v) - stats.get("battery_voltage", -999)) > 5]
        if vals:
            stats["discharge_current"] = Counter(vals).most_common(1)[0][0]
    if di_minus:
        vals = [float(v) for v in di_minus
                if float(v) < 500
                and abs(float(v) - stats.get("battery_voltage", -999)) > 5]
        if vals:
            stats["charge_current"] = Counter(vals).most_common(1)[0][0]

    # Fallback: look for "000.0" pattern (common when battery is idle)
    if "discharge_current" not in stats and "charge_current" not in stats:
        zero_current = re.findall(r"000\.0", combined_text)
        if zero_current:
            stats["discharge_current"] = 0.0
            stats["charge_current"] = 0.0

    return stats


def update_cache():
    """Fetch, enhance, OCR, and parse. Update cache."""
    now = time.time()
    if now - _cache["last_update"] < CACHE_TTL:
        return

    try:
        logger.info("Fetching frame from go2rtc...")
        raw_frame = fetch_frame()
        _cache["raw_frame"] = raw_frame

        logger.info("Enhancing frame...")
        enhanced = enhance_frame(raw_frame)
        _cache["enhanced_frame"] = enhanced

        logger.info("Running multi-threshold OCR...")
        raw_text = multi_threshold_ocr(raw_frame)
        _cache["raw_text"] = raw_text
        logger.info(f"OCR combined text length: {len(raw_text)} chars")

        logger.info("Parsing stats...")
        stats = parse_stats(raw_text)
        _cache["stats"] = stats
        _cache["error"] = None
        _cache["last_update"] = now

        logger.info(f"Parsed stats: {stats}")

    except Exception as e:
        logger.error(f"Error updating cache: {e}")
        _cache["error"] = str(e)
        _cache["last_update"] = now  # avoid hammering on error


@app.route("/api/stats", methods=["GET"])
def get_stats():
    """Return parsed inverter/battery stats as JSON."""
    update_cache()
    response = {
        "stats": _cache["stats"],
        "last_update": _cache["last_update"],
        "error": _cache["error"],
    }
    return jsonify(response)


@app.route("/api/frame/raw", methods=["GET"])
def get_raw_frame():
    """Return the raw frame as JPEG (for debugging)."""
    update_cache()
    if _cache["raw_frame"] is None:
        return jsonify({"error": "No frame available"}), 503

    _, buffer = cv2.imencode(".jpeg", _cache["raw_frame"])
    return send_file(io.BytesIO(buffer.tobytes()), mimetype="image/jpeg")


@app.route("/api/frame/enhanced", methods=["GET"])
def get_enhanced_frame():
    """Return the enhanced B&W frame as JPEG (for debugging)."""
    update_cache()
    if _cache["enhanced_frame"] is None:
        return jsonify({"error": "No frame available"}), 503

    _, buffer = cv2.imencode(".jpeg", _cache["enhanced_frame"])
    return send_file(io.BytesIO(buffer.tobytes()), mimetype="image/jpeg")


@app.route("/api/health", methods=["GET"])
def health():
    """Health check endpoint."""
    return jsonify({"status": "ok", "last_update": _cache["last_update"]})


@app.route("/", methods=["GET"])
def index():
    """Simple index page with links."""
    return """
    <h1>Inverter OCR Service</h1>
    <ul>
        <li><a href="/api/stats">GET /api/stats</a> - Parsed battery/inverter stats (JSON)</li>
        <li><a href="/api/frame/raw">GET /api/frame/raw</a> - Raw frame from go2rtc</li>
        <li><a href="/api/frame/enhanced">GET /api/frame/enhanced</a> - Enhanced B&W frame</li>
        <li><a href="/api/health">GET /api/health</a> - Health check</li>
    </ul>
    """


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
