from playwright.sync_api import Page
from automation.practise_pages.login_page.login_locators import LoginLocators


class LoginPage:
    def __init__(self, Page):
        self.page = Page

    def login_username(self, username: str = ""):
        self.page.locator(LoginLocators.login_username_locators).fill(username)

    def login_password(self, password: str = ""):
        self.page.locator(LoginLocators.login_password_locators).fill(password)

    def login_button(self):
        self.page.locator(LoginLocators.login_button_locators).click()
