from modules.ui.page_objects.GitHub.base_page_gitlub import BasePage
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class SignInPage(BasePage):
    URL = "https://checkout1.iherb.com/auth/Account/Login"

    def __init__(self) -> None:
        super().__init__()
    
    def go_to(self):
        self.driver.get(SignInPage.URL)

    def try_login(self, username, password):
        login_elem = self.driver.find_element(By.ID, "username_input")
        login_elem.send_keys(username)
        pass_elem = self.driver.find_element(By.ID, "Password")
        pass_elem.send_keys(password)
        btn_elem = self.driver.find_element(By.ID, "sign_in_button")
        btn_elem.click()


    def check_exists_by_class_name(self):
        try:
            self.driver.find_element(By.CLASS_NAME, "form-row link")
        except NoSuchElementException:
            return False
        return True
        
    