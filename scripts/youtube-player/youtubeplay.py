import time
import sys
from playwright.sync_api import sync_playwright

# Pre-configured with your exact root Firefox profile path
USER_DATA_DIR = "/root/.mozilla/firefox/mx6t28bp.default-esr"

VIDEOS = [
    "https://www.youtube.com/watch?v=6dinnygUx_w"
]

def run():
    print("Starting YouTube automated task...")
    
    with sync_playwright() as p:
        try:
            # Launching Firefox using your persistent profile
            context = p.firefox.launch_persistent_context(
                user_data_dir=USER_DATA_DIR,
                headless=False  # Keeps the browser visible
            )
            
            page = context.new_page()
            
            for index, url in enumerate(VIDEOS, 1):
                print(f"Opening Video {index}: {url}")
                page.goto(url)
                
                # Wait for the page network to go idle (fully loaded)
                page.wait_for_load_state("networkidle")
                
                # Attempt to bypass any standard cookie consent popups
                try:
                    page.click("button:has-text('Reject all')", timeout=3000)
                except:
                    pass

                # Watch time per video (60 seconds)
                print("Watching video for 60 seconds...")
                time.sleep(3600) 
                
            print("Finished watching all videos. Closing browser cleanly...")
            context.close()
            
        except Exception as e:
            print(f"\n[ERROR] An error occurred: {e}")
            print("Reminder: Make sure your regular Firefox browser is COMPLETELY closed before running this script.")

if __name__ == "__main__":
    run()