import time
from playwright.sync_api import Page, expect
from automation.data.data import Data

from automation.practise_pages.forgot_page.forgot_page_locators import ForgotPageLocator


def forgot_page_open(
    page: Page,
    username: str = "",
):
    page.locator(ForgotPageLocator.fogot_email_id).fill(username)
    page.locator(ForgotPageLocator.retrive_password).click()
