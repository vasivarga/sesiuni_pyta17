from behave import *

@given('I am on the login page')
def step_impl(context):
    context.login_page.open()

@when('I enter "{text}" in the email input')
def step_impl(context, text):
    context.login_page.set_email(text)

@when('I enter "{text}" in the password input')
def step_impl(context, text):
    context.login_page.set_password(text)

@when("I click the login button")
def step_impl(context):
    context.login_page.click_login()

@then('I should see "{text}" message')
def step_impl(context, text):
    context.login_page.verify_error_text_message(text)