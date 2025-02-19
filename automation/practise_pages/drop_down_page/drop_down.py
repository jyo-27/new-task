from playwright.sync_api import Page
from automation.data.data import Data
from automation.practise_pages.drop_down_page.drop_down_locators import DropDownList


def drop_down(page: Page):
    page.locator(DropDownList.drop_down_select_option).click()
    page.keyboard.press("ArrowDown")
    page.locator(DropDownList.drop_down_element_per_page_id).click()
    page.keyboard.press("ArrowDown")
    page.locator(DropDownList.drop_down_select_country).click()
    page.keyboard.press("ArrowDown")
    page.locator(Data.home_page_locator)
