# WebSnap
WebSnap is a very simple Python script for taking automated screenshots of websites. 
It uses Selenium to control a Chrome browser and captures screenshots of specified URLs after logging into a 
website if required. Screenshots are saved to a specified directory.

## Features
- Automate login to a website using provided credentials
- Capture screenshots of specified URLs
- Save screenshots in a structured directory with timestamps
- Customizable Chrome WebDriver options

## Requirements
- Python 3.6+
- Google Chrome
- ChromeDriver

## Installation
1. Clone the repository:
```bash
git clone https://github.com/Crossoufire/WebSnap.git
```

2. Install the required packages:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the project root directory and add your credentials (if needed):
```env
USERNAME=<your_username>
PASSWORD=<your_password>
```

## Usage
Here is an example of how to use the WebSnap class
```
from websnap import WebSnap

# Define login details (if needed)
login_details = {
    "url": "https://example.com/login",
    "steps": [
        {"xpath": "//input[@name='username']", "action": "send_keys", "value": "USERNAME"},
        {"xpath": "//input[@name='password']", "action": "send_keys", "value": "PASSWORD"},
        {"xpath": "//button[@type='submit']", "action": "click"}
    ]
}

# Define URLs to capture screenshots of
urls = [
    "https://example.com/page1",
    "https://example.com/page2",
    "https://example.com/page3",
]

# Initialize WebSnap with optional Chrome options
web_snap = WebSnap(save_dir="screenshots", headless=True)

# Take screenshots of Login page 
web_snap.take_screenshots(urls=["https://example.com/login"])

# Login to website
web_snap.login_to_website(login_details, sleep_time=2.0)

# Take screenshots of specified URLs
web_snap.take_screenshots(urls, sleep_time=2.0)

# Quit driver
web_snap.quit()
```
