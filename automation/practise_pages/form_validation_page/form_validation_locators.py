class FormValidationLocators:
    form_validate_title = (
        'h1:text-is("Form Validation page for Automation Testing Practice")'
    )
    form_contact_name = '[id="validationCustom01"]'
    form_contact_number = "(//input[@id='validationCustom05'])[1]"
    form_validate_date = "(//input[@id='validationCustom05'])[2]"
    form_paymeny_method = '[id="validationCustom04"]'
    form_contact_validate_name = 'div:text-is("Please enter your Contact name.")'
    form_contact_validate_number = 'div:text-is("Please provide your Contact number.")'
    form_valid_validate_date = 'div:text-is("Please provide valid Date.")'
    form_valid_paymeny_method = "div:text-is('Please select the Paymeny Method.')"
    form_validation_sucess_message = 'p:text-is("Thank you for validating your ticket")'
    form_validation_button = "button:text-is('Register')"
