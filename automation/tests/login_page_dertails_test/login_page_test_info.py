from automation.data.data import Data
from automation.practise_pages.login_page.login_page import LoginPage
from playwright.sync_api import Page
from playwright.sync_api import expect
from automation.practise_pages.login_page.login_locators import LoginLocators
import json

def test_login_page_concept(page: Page):
    page.goto(Data.login_page_url)
    login_page = LoginPage(page)
    with open('log.creds') as f:
        creds = json.load(f)
    
    # Use the credentials for login
    username = creds["username1"]
    password = creds["username_password1"]
    login_page.login_username(username)
    login_page.login_password(password)
    page.screenshot(path="screenshots/loginpage.png")
    login_page.login_button()
    expect(page.locator(LoginLocators.sucess_login_button)).to_have_text(
        Data.login_sucessfull_message
    )
#expect
