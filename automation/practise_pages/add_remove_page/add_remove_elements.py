from playwright.sync_api import Page
from automation.data.data import Data
from automation.practise_pages.add_remove_page.add_remove_locators import (
    AddorRemoveElementsLocators,
)


def add_remove_elements(page:Page):
    page.locator(AddorRemoveElementsLocators.add_elment_button).click()
    page.locator(AddorRemoveElementsLocators.delete_button).click()
