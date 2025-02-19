from automation.practise_pages.search_page.search_page_test import search_page_details
from playwright.sync_api import Page,expect
from automation.data.data import Data
def test_search_page(page:Page):
    page.goto(Data.test_link)
    search_page_details(page,"login")
