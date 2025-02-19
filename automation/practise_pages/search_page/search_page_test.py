from automation.practise_pages.search_page.locators import searchPageLocators
from playwright.sync_api import Page,expect

def search_page_details(page:Page, title:str):
    # search_input = page.wait_for_selector(searchPageLocators.search).query_selector(search_input_select)
    # if search_input:
    #     search_input.fill(title)
    #     search_input.click()
    #     page.wait_for_load_state('domcontentloaded')
    # else:
    #     print("with in the time locator is not found")

    page.wait_for_selector(searchPageLocators.search).fill(title)
    page.wait_for_load_state('domcontentloaded')