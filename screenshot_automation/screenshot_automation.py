import time
from pathlib import Path
from datetime import datetime

import pyautogui


# Folder where screenshots will be saved
OUTPUT_FOLDER = Path("screenshots")

# Time interval between screenshots (seconds)
INTERVAL = 5

# Total number of screenshots to capture
NUMBER_OF_SCREENSHOTS = 10

def take_screenshot():
    """
    Capture and save a screenshot with a timestamp.
    """
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = OUTPUT_FOLDER / f"screenshot_{timestamp}.png"

    screenshot = pyautogui.screenshot()
    screenshot.save(filename)

    print(f"Saved: {filename.name}")