from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


@given('Opens target sign in page')
def open_target(context):
    context.app.sign_in_page.open_sign_in_page()


@when('Enter the incorrect username')
def enter_bad_username(context):
    context.app.sign_in_page.bad_username_input()

@when('Enter incorrect password combination')
def enter_bad_password(context):
    context.app.sign_in_page.bad_password_input()

@then('Click sign in button')
def click_sign_in_btn(context):
    context.app.sign_in_page.click_sign_in_btn()

@then("Verify that 'We can\'t find your account.' message is shown")
def verify_message_login(context):
    context.app.sign_in_page.verify_cannot_signin()