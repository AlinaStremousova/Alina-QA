from modules.ui.page_objects.SwagLabs.base_page_swag_labs import BasePage
from selenium import webdriver
from selenium.webdriver.common.by import By


class SignInPage(BasePage):
    URL = "https://www.saucedemo.com/"

    def __init__(self, driver: webdriver.Chrome):
        super().__init__(driver)
    
    def go_to(self):
        self.driver.get(SignInPage.URL)

    def try_login(self, username, password):
        login_elem = self.driver.find_element(By.ID, "user-name")
        login_elem.send_keys(username)
        pass_elem = self.driver.find_element(By.ID, "password")
        pass_elem.send_keys(password)
        btn_elem = self.driver.find_element(By.ID, "login-button")
        btn_elem.click()

    def check_title(self, expected_title):
        return self.driver.title == expected_title
    
    