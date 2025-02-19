import pytest
from automation.data.common_data import CommonData
from automation.data.data import Data
from automation.practise_pages.forgot_page.forget_page import forgot_page_open
from playwright.sync_api import Page
from playwright.sync_api import expect
from automation.practise_pages.forgot_page.forgot_page_locators import ForgotPageLocator


def test_forgot_page(page: Page):
    page.goto(Data.forgot_page_url)
    forgot_page_open(page, CommonData.forgot_email)
    expect(page.locator(ForgotPageLocator.forgot_sucess_button)).to_have_text(
        Data.forgot_sucessfull_message
    )
