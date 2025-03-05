from automation.data.data import Data
from automation.practise_pages.login_page.login_page import LoginPage
from playwright.sync_api import Page
from playwright.sync_api import expect
from automation.practise_pages.login_page.login_locators import LoginLocators
import json

def test_login_page_concept(page: Page):
    page.goto(Data.login_page_url)
    login_page = LoginPage(page)
    if os.path.exists('log.creds') and os.path.getsize('log.creds') > 0:
        with open('log.creds') as f:
            file_content = f.read()
            # Print the content of the file for debugging
            print("log.creds content:", file_content)
            
            try:
                # Try to load the JSON from the file content
                creds = json.loads(file_content)
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON: {e}")
                return  # Exit if there's a JSON decode error
    else:
        print("Error: log.creds file is missing or empty")
        return  # Exit if the file is missing or empty

    # Use the credentials for login
    username = creds.get("username1")
    password = creds.get("username_password1")

    login_page.login_username(username)
    login_page.login_password(password)
    page.screenshot(path="screenshots/loginpage.png")
    login_page.login_button()
    expect(page.locator(LoginLocators.sucess_login_button)).to_have_text(
        Data.login_sucessfull_message
    )
#expect
