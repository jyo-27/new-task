from automation.practise_pages.web_inputs_page.web_inputs import web_inputs
from playwright.sync_api import Page
from automation.data.data import Data


def test_web_inputs_page(page: Page):
    page.goto(Data.web_input_page_url)
    web_inputs(page)
