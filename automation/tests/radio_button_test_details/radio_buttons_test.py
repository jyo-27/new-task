from automation.practise_pages.radio_buttons_page.radio_buttons import radio_buttons
from playwright.sync_api import Page
from automation.data.data import Data
import pytest
from playwright.sync_api import expect
from automation.practise_pages.radio_buttons_page.radio_buttons_locators import (
    Radio_Buttons,
)


@pytest.mark.parametrize("color,sports", Data.radio_button_options)
def test_radio_button_page(page: Page, color, sports):
    page.goto(Data.radio_buttons_page_url)
    radio_buttons(color, sports, page)
    expect(
        page.locator(Radio_Buttons.choose_favourite_color.format(color))
    ).to_be_checked()
