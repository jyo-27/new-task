from automation.practise_pages.form_validation_page.form_validation import (
    FormValidation,
)
from automation.practise_pages.form_validation_page.form_validation_locators import (
    FormValidationLocators,
)
from playwright.sync_api import Page
from playwright.sync_api import expect
from automation.data.data import Data
from automation.data.common_data import CommonData


def test_form_validation(page: Page):
    page.goto(Data.form_validation_url)
    form_validation = FormValidation(page)
    form_validation.contact_name(CommonData.web_input_text)
    form_validation.contact_number(Data.form_validate_contact_number)
    form_validation.pickup_date(CommonData.web_input_date)
    form_validation.payment_method()
    form_validation.form_validation_button()
    expect(
        page.locator(FormValidationLocators.form_validation_sucess_message)
    ).to_have_text(Data.form_validate_sucess_message)
