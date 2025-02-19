import playwright.sync_api
from automation.practise_pages.add_remove_page.add_remove_elements import add_remove_elements
from playwright.sync_api import Page,sync_playwright
from automation.data.data import Data
import playwright
import time

from automation.tests.conftest import capture_screenshot



def test_add_or_remove_page(setup_browser):
    # page.goto(Data.add_or_remove_page_url)
    page =setup_browser
    capture_screenshot(page)
    page.wait_for_load_state()
    add_remove_elements(page)
    page.keyboard.press("Enter")
    
