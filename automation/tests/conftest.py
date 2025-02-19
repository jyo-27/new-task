import pytest
from playwright.sync_api import sync_playwright
from automation.data.data import Data

@pytest.fixture(scope="function")
def input_value():
    input= "1"
    yield input


@pytest.fixture(scope="function")
def setup_browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # Set headless=True for CI
        page = browser.new_page()
        page.goto(Data.add_or_remove_page_url)  # Your test URL
        yield page
        browser.close()


def capture_screenshot(page, locator=None):
    """Capture a screenshot for locator issues or page load issues."""
    if locator:
        context_message = f"Locator '{locator}' not found or not visible"
    else:
        context_message = "Page load issue"

    # Define the path for the screenshot
    screenshot_path = f'screenshots/{context_message.replace(" ", "_").replace(":", "_")}.png'

    # Capture the screenshot of the page
    page.screenshot(path=screenshot_path)
    print(f"Screenshot captured for '{context_message}' at '{screenshot_path}'.")