from automation.data.data import Data
from automation.practise_pages.forgot_page.forget_page import forgot_page_open
from playwright.sync_api import Page
import pytest
from automation.data.common_data import CommonData
from playwright.sync_api import expect
from automation.practise_pages.forgot_page.forgot_page_locators import ForgotPageLocator


@pytest.mark.parametrize("username", Data.forgot_page_options)
def test_forgot_page_pz(page: Page, username):
    page.goto(Data.forgot_page_url)
    expect(page.get_by_label("E-mail", exact=True)).to_be_visible()
    forgot_page_open(page, username)

    if (
        username.endswith("@gmail.com")
        or username.endswith("@gmail.co")
        or username.endswith("@gmail.c")
    ):
        expect(page.locator(ForgotPageLocator.forgot_sucess_button)).to_have_text(
            Data.forgot_sucessfull_message
        )

    elif username.endswith("@g.") or username.endswith("@g"):
        expect(page.locator(ForgotPageLocator.forgot_email_invalid)).to_have_text(
            Data.forgot_email_failed_message
        )

    else:
        expect(
            page.locator(ForgotPageLocator.forgot_failure_message_locator)
        ).to_have_text(Data.forgot_failure_message)
