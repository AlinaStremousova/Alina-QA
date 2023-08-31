from modules.ui.page_objects.SwagLabs.sign_in_page_swag_labs import SignInPage
from modules.ui.page_objects.SwagLabs.add_to_card_swag_labs import Card, InventoryPage
from modules.ui.page_objects.SwagLabs.base_page_swag_labs import BasePage
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pytest


@pytest.mark.ui
def test_check_correct_username():
    driver = webdriver.Chrome(service=Service(BasePage.PATH + BasePage.DRIVER_NAME))
    sign_in_page = SignInPage(driver=driver)
    sign_in_page.go_to()
    sign_in_page.try_login("standard_user", "secret_sauce")
    assert sign_in_page.check_title("Swag Labs")

@pytest.mark.ui
def test_check_card():
    driver = webdriver.Chrome(service=Service(BasePage.PATH + BasePage.DRIVER_NAME))
    login_page = SignInPage(driver=driver)
    login_page.go_to()
    login_page.try_login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(driver=driver)
    inventory_page.go_to(inventory_page.URL)
    inventory_page.add_item_to_card()

    card_page = Card(driver=driver)
    card_page.go_to_card()
    assert card_page.check_card() is not None
    card_page.proceed_to_checkout()

    driver.quit()