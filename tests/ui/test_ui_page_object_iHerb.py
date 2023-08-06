from modules.ui.page_objects.sign_in_page_iHerb import SignInPage
import pytest


@pytest.mark.ui_captcha
def test_check_correct_username():
    sign_in_page = SignInPage()
    sign_in_page.go_to()
    sign_in_page.try_login("stremousova14@gmail.com", "Qwerty123")

    assert sign_in_page.check_exists_by_class_name == True

    sign_in_page.close()

