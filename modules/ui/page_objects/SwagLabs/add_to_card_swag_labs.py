from modules.ui.page_objects.SwagLabs.base_page_swag_labs import BasePage
from selenium import webdriver
from selenium.webdriver.common.by import By

class Card(BasePage):
    URL = "https://www.saucedemo.com/cart.html"
    CART_QUANTITY_CLASS_NAME = "cart_quantity"
    CHECKOUT_BUTTON = "checkout"
    
    def __init__(self, driver: webdriver.Chrome):
        super().__init__(driver)

    def go_to_card(self):
        self.go_to(self.URL)

    def check_card(self):
        cart_quantity = self.driver.find_element(By.CLASS_NAME, self.CART_QUANTITY_CLASS_NAME)
        return cart_quantity

    def proceed_to_checkout(self):
        checkout_button = self.driver.find_element(By.ID, self.CHECKOUT_BUTTON)
        checkout_button.click()


class InventoryPage(BasePage):
    URL = "https://www.saucedemo.com/inventory.html"
    ADD_TO_CART_BUTTON_ID = "add-to-cart-sauce-labs-backpack"
    
    def __init__(self, driver: webdriver.Chrome):
        super().__init__(driver)

    def add_item_to_card(self):
        add_to_cart_button = self.driver.find_element(By.ID, self.ADD_TO_CART_BUTTON_ID)
        add_to_cart_button.click()

