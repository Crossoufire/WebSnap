import os
import time
from datetime import datetime
from typing import List, Dict
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from tqdm import tqdm
from webdriver_manager.chrome import ChromeDriverManager


class WebSnap:
    TIMEOUT: int = 5

    def __init__(self, save_dir: str = None, **kwargs):
        load_dotenv(".env")
        self.save_dir = save_dir
        if not self.save_dir:
            self.save_dir = os.path.join(
                os.path.dirname(os.path.abspath(__file__)),
                f"saves/{datetime.now().strftime('%d-%b-%Y_%H-%M-%S')}"
            )
        os.makedirs(self.save_dir, exist_ok=True)
        self.driver = self._init_driver(**kwargs)

    @staticmethod
    def _init_driver(**kwargs) -> webdriver.Chrome:
        options = webdriver.ChromeOptions()
        for key, value in kwargs.items():
            if isinstance(value, bool) and value:
                options.add_argument(f"--{key}")
            elif value:
                options.add_argument(f"--{key}={value}")
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        driver.set_window_size(1920, 1080)

        return driver

    def login_to_website(self, login_details: Dict, sleep_time: float = 2.0):
        self.driver.get(login_details["url"])

        for step in login_details["steps"]:
            element = WebDriverWait(self.driver, self.TIMEOUT).until(
                EC.presence_of_element_located((By.XPATH, step["xpath"]))
            )
            if step["action"] == "send_keys":
                element.send_keys(os.getenv(step["value"]))
            elif step["action"] == "click":
                element.click()

        print("\nWaiting for login...")
        time.sleep(sleep_time)
        print("Logged in!\n")

    def take_screenshots(self, urls: List[str], sleep_time: float = 2.0):
        for url in tqdm(urls, ncols=70, desc="Taking Screenshots"):
            self.driver.get(url)
            time.sleep(sleep_time)
            filename = url.split("//")[1].replace("/", "_") + ".png"
            screenshot = self.driver.find_element(by=By.TAG_NAME, value="html").screenshot_as_png
            with open(os.path.join(self.save_dir, filename), "wb") as fp:
                fp.write(screenshot)

    def quit(self):
        self.driver.quit()
