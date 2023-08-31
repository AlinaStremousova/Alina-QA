from selenium.webdriver.chrome.service import Service
from selenium import webdriver
import os
from config.config import ROOT_DIR

class BasePage:
    CHROMEDRIVER_PATH = os.path.join(ROOT_DIR, "chromedriver.exe")

    def __init__(self) -> None:
        self.driver = webdriver.Chrome(
    service=Service(BasePage.CHROMEDRIVER_PATH)
        )
    def go_to(self, url):
        self.driver.get(url)

    def close(self):
        self.driver.close()
