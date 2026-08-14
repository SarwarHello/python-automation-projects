# Screenshot Automation

A simple Python automation tool that automatically captures screenshots at regular time intervals and saves them with timestamped filenames.

## Features

* Automatically captures screenshots
* Saves screenshots with unique timestamps
* Customisable screenshot interval
* Automatically creates an output folder
* Can be stopped using `Ctrl + C`

## Requirements

* Python 3
* PyAutoGUI
* Pillow

Install the dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run the script:

```bash
python screenshot_automation.py
```

Screenshots will automatically be saved inside the `screenshots` folder.

## Project Structure

```text
screenshot-automation/
├── screenshot_automation.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Disclaimer

This project is intended for educational and personal automation purposes. Only capture screens and information you are authorised to access.
