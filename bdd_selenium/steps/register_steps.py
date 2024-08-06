from behave import *

@given('I am on the register page')
def step_impl(context):
    context.register_page.open()

@when('I click Register button')
def step_impl(context):
    context.register_page.click_register_button()

@then('"{message}" error text is displayed for first name field')
def step_impl(context, message):
    context.register_page.verify_first_name_mandatory_error(message)

@then('"{message}" error text is displayed for last name field')
def step_impl(context, message):
    context.register_page.verify_last_name_mandatory_error(message)

@then('"{message}" error text is displayed for email field')
def step_impl(context, message):
    context.register_page.verify_email_mandatory_error(message)

@then('"{message}" error text is displayed for password field')
def step_impl(context, message):
    context.register_page.verify_password_mandatory_error(message)

@when('I set "{text}" as first name')
def step_impl(context, text):
    context.register_page.set_first_name(text)

@when('I set "{text}" as last name')
def step_impl(context, text):
    context.register_page.set_last_name(text)

@when('I select "{day}" "{month}" "{year}" as birth date')
def step_impl(context, day, month, year):
    context.register_page.select_day_of_birth(day)
    context.register_page.select_month_of_birth(month)
    context.register_page.select_year_of_birth(year)

@when('I set "{text}" as email')
def step_impl(context, text):
    context.register_page.set_email(text)

@when('I set "{text}" as password')
def step_impl(context, text):
    context.register_page.set_password(text)

@when('I set "{text}" as password confirm')
def step_impl(context, text):
    context.register_page.set_password_confirm(text)

@then('I should see "{text_1}" and "{text_2}" in the password error message')
def step_impl(context, text_1, text_2):
    context.register_page.verify_pass_validation_text_contains(text_1)
    context.register_page.verify_pass_validation_text_contains(text_2)