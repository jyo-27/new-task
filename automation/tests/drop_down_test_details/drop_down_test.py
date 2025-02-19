from automation.practise_pages.drop_down_page.drop_down import drop_down
from playwright.sync_api import Page
from automation.data.data import Data


def test_drop_down_page(page: Page):
    page.goto(Data.drop_down_page_url)
    drop_down(page)
