from selenium.webdriver.chrome.service import Service
from selenium import webdriver


class BasePage:
    PATH = "C:\\Users\\38098\\Alina-QA\\"
    DRIVER_NAME = "chromedriver.exe"

    def __init__(self) -> None:
        self.driver = webdriver.Chrome(
    service=Service(BasePage.PATH + BasePage.DRIVER_NAME)
        )

    def go_to(self, url):
        self.driver.get(url)

    def close(self):
        self.driver.close()
