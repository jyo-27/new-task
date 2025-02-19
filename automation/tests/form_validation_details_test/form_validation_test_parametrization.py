import pytest
from automation.practise_pages.form_validation_page.form_validation import (
    FormValidation,
)
from automation.practise_pages.form_validation_page.form_validation_locators import (
    FormValidationLocators,
)
from playwright.sync_api import Page
from playwright.sync_api import expect
from automation.data.common_data import CommonData
from automation.data.data import Data


@pytest.mark.parametrize(
    "contact_name,number,date", [("a", "123", CommonData.web_input_date)]
)
def test_form_validation_multiple_inputs(contact_name, number, date, page: Page):
    page.goto(Data.form_validation_url)
    form_validation = FormValidation(page)
    form_validation.contact_name(contact_name)
    form_validation.contact_number(number)
    form_validation.pickup_date(date)
    form_validation.payment_method()
    form_validation.form_validation_button()
