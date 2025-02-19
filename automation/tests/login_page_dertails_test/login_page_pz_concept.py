import pytest
from automation.practise_pages.login_page.login_page import LoginPage
from playwright.sync_api import Page
from automation.data.data import Data
from playwright.sync_api import expect
from automation.practise_pages.login_page.login_locators import LoginLocators


@pytest.mark.parametrize("username ,password", Data.login_page_test_options)
def test_login_page_pz(username, password, page: Page):
    page.goto(Data.login_page_url)
    login_page = LoginPage(page)
    login_page.login_username(username)
    login_page.login_password(password)
    login_page.login_button()

    if username != Data.login_user_name:
        expect(page.locator(LoginLocators.login_name_invalid)).to_have_text(
            Data.login_user_name_failed
        )

    elif password != Data.login_password:
        expect(page.locator(LoginLocators.login_password_invalid)).to_have_text(
            Data.login_password_failed
        )

    else:
        expect(page.locator(LoginLocators.sucess_login_button)).to_have_text(
            Data.login_sucessfull_message
        )
