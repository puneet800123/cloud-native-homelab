# scripts

Standalone helper scripts. These are **not** Kubernetes manifests.

| Script | Description |
|--------|-------------|
| [youtube-player](youtube-player) | Playwright script that opens YouTube videos in a persistent Firefox profile |
| [inverter-ocr](inverter-ocr) | Flask service that OCRs an inverter's LCD via frames from go2rtc |

## youtube-player

`youtubeplay.py` launches Firefox via Playwright using a persistent profile.
Edit `USER_DATA_DIR` and the `VIDEOS` list for your environment. Requires
`playwright` (and its Firefox browser) installed in a virtualenv.

## inverter-ocr

A Flask + OpenCV + Tesseract service that fetches JPEG frames from a go2rtc endpoint,
runs multi-threshold OCR, and exposes parsed battery stats over a REST API. Ships with a
`Dockerfile` and `requirements.txt`; the matching Kubernetes manifests live in
`apps/inverter-ocr/`.

Build and run:
```bash
cd scripts/inverter-ocr
docker build -t inverter-ocr:latest .
```

Configuration note: the frame source URL (a LAN address / go2rtc endpoint) is set at the
top of `app.py` — adjust it for your network.

> Python virtualenvs are intentionally excluded from the repo via `.gitignore`.
