from automation.practise_pages.radio_buttons_page.radio_buttons_locators import (
    Radio_Buttons,
)


def radio_buttons(color, sports, page):
    page.locator(Radio_Buttons.choose_favourite_color.format(color)).check()
    page.locator(Radio_Buttons.choose_favourite_game.format(sports)).check()
