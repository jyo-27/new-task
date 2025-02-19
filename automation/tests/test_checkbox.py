from playwright.sync_api import Page,expect

def test_checkbox(page:Page, text="checkbox1"):
    page.goto("https://practice.expandtesting.com/checkboxes")
    # check = page.wait_for_selector('[id="checkboxes"] > [id ="checkbox2"]').check()
    # if check:
    #     # check.click()
    #     check.
   
    b = page.locator('[id="checkboxes"] > label:text-is("Checkbox 1")').is_visible()
    if b:
        page.wait_for_selector(f'[id="checkboxes"] > [id ="{text}"]').check()
        # assert(page.locator('[id="checkboxes"] > label:text-is("Checkbox 1")').is_visible())
        print(b)
    else:
        print("is not correct")
