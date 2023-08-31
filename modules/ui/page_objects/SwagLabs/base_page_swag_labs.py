from selenium import webdriver


class BasePage:
    PATH = "C:\\Users\\38098\\Alina-QA\\"
    DRIVER_NAME = "chromedriver.exe"

    def __init__(self, driver: webdriver.Chrome) -> None:
        self.driver = driver

    def go_to(self, url):
        self.driver.get(url)