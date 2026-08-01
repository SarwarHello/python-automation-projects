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

def create_output_folder():
    """
    Create the screenshots folder if it does not exist.
    """
    OUTPUT_FOLDER.mkdir(exist_ok=True)

def take_screenshot():
    """
    Capture and save a screenshot with a timestamp.
    """
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = OUTPUT_FOLDER / f"screenshot_{timestamp}.png"

    screenshot = pyautogui.screenshot()
    screenshot.save(filename)

    print(f"Saved: {filename.name}")


def main():
    """
    Capture screenshots at regular intervals.
    """
    create_output_folder()

    print("Screenshot automation started...")
    print("Press Ctrl + C to stop.\n")

    try:
        for i in range(NUMBER_OF_SCREENSHOTS):
            take_screenshot()

            if i < NUMBER_OF_SCREENSHOTS - 1:
                time.sleep(INTERVAL)

        print("\nCompleted successfully!")

    except KeyboardInterrupt:
        print("\nScreenshot automation stopped by user.")


if __name__ == "__main__":
    main()