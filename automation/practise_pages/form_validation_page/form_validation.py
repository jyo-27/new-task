import logging
from playwright.sync_api import Page, expect
from automation.data.data import Data
from automation.data.common_data import CommonData

# from automation.locators.form_validation_locators import FormValidation
from automation.practise_pages.form_validation_page.form_validation_locators import (
    FormValidationLocators,
)


class FormValidation:
    def __init__(self, page):
        self.page = page
        expect(
            page.get_by_title("Form Validation page for Automation Testing Practice")
        ) == "Form Validation page for Automation Testing Practice"

    def contact_name(self, contact_name: str = ""):
        self.page.locator(FormValidationLocators.form_contact_name).click()
        self.page.locator(FormValidationLocators.form_contact_name).fill(contact_name)

    def contact_number(self, contact_number: str = ""):
        self.page.locator(FormValidationLocators.form_contact_number).click()
        self.page.locator(FormValidationLocators.form_contact_number).fill(
            contact_number
        )

    def pickup_date(self, valid_date: str = ""):
        self.page.locator(FormValidationLocators.form_validate_date).click()
        self.page.locator(FormValidationLocators.form_validate_date).fill(valid_date)

    def payment_method(self):
        self.page.locator(FormValidationLocators.form_paymeny_method).click()
        self.page.keyboard.press("ArrowDown")

    def form_validation_button(self):
        self.page.locator(FormValidationLocators.form_validation_button).click()
