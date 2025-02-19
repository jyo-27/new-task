from automation.data.data import Data
from automation.practise_pages.login_page.login_page import LoginPage
from playwright.sync_api import Page
from playwright.sync_api import expect
from automation.practise_pages.login_page.login_locators import LoginLocators


def test_login_page_concept(page: Page):
    page.goto(Data.login_page_url)
    login_page = LoginPage(page)
    login_page.login_username(Data.login_user_name)
    login_page.login_password(Data.login_password)
    page.screenshot(path="screenshots/loginpage.png")
    login_page.login_button()
    expect(page.locator(LoginLocators.sucess_login_button)).to_have_text(
        Data.login_sucessfull_message
    )
#expect