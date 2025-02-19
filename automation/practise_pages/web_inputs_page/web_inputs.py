from playwright.sync_api import Page, expect
from automation.data.data import Data
from automation.data.common_data import CommonData
from automation.practise_pages.web_inputs_page.web_inputs_page_locators import (
    WebInputLocators,
)


def web_inputs(page: Page):
    page.locator(WebInputLocators.web_input_number_locator).click()
    page.locator(WebInputLocators.web_input_number_locator).fill(Data.web_input_number)
    page.locator(WebInputLocators.web_input_text_locator).fill(
        CommonData.web_input_text
    )
    page.locator(WebInputLocators.web_input_password_locator).fill(
        CommonData.web_input_password
    )
    page.locator(WebInputLocators.web_input_date_locator).click()
    page.locator(WebInputLocators.web_input_date_locator).fill(
        CommonData.web_input_date
    )
    page.locator(WebInputLocators.web_input_display_input_button).click()
    expect(page.locator(WebInputLocators.web_display_number)).to_contain_text(
        Data.web_input_number
    )
    page.locator(WebInputLocators.web_input_clear_button).click()
