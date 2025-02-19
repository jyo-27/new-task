import pytest
import re


class Data:
    test_link = "https://practice.expandtesting.com/"
    home_page_locator = "a:text-is('Home')"

    # pages_urls
    login_page_url = "https://practice.expandtesting.com/login"
    form_validation_url = "https://practice.expandtesting.com/form-validation"
    forgot_page_url = "https://practice.expandtesting.com/forgot-password"
    web_input_page_url = "https://practice.expandtesting.com/inputs"
    add_or_remove_page_url = "https://practice.expandtesting.com/add-remove-elements"
    drop_down_page_url = "https://practice.expandtesting.com/dropdown"
    radio_buttons_page_url = "https://practice.expandtesting.com/radio-buttons"

    # web_inputs
    web_input_number = "1"

    # form_validation
    form_validate_contact_number = "123-3456789"
    form_validate_sucess_message = "Thank you for validating your ticket"

    # login details
    login_user_name = "practice"
    login_password = "SuperSecretPassword!"
    login_sucessfull_message = "You logged into a secure area!"
    login_user_name_failed = "Your username is invalid!"
    login_password_failed = "Your password is invalid!"
    login_page_test_options = [
        ("anu", "a@123"),
        (" ", login_password),
        ("sona", " "),
        (login_user_name, "a@123"),
        (login_user_name, " "),
        (login_user_name, login_password),
    ]

    # radio_buttons
    radio_button_options = [("red", "football"), ("yellow", "tennis")]

    # forgot_page
    forgot_page_options = [
        ("a"),
        ("a@"),
        ("a@g"),
        ("a1"),
        ("a@gmail.c"),
        ("b@gmail.com"),
    ]
    forgot_sucessfull_message = (
        "An e-mail has been sent to you which explains how to reset your  password. "
    )
    forgot_failure_message = "Please enter a valid email address. "
    forgot_email_failed_message = "Your email is invalid!"