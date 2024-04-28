from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from pages.base_page import Base


@given('Open sign in page')
def open_sign_in_page(context):
   context.app.sign_in_page.open_sign_in_page()

@when('Store original window')
def store_original_window(context):
    context.original_window = context.driver.current_window_handle
    print('Current window:', context.original_window)

@when('Click on Target terms and conditions link')
def click_on_target_terms_and_cond(context):
    context.app.sign_in_page.terms_and_conditions()

@when('Switch to the newly opened window')
def switch_to_newly_opened_window(context):
    context.app.sign_in_page.switch_to_next_window()

@then('Verify Terms and Conditions page is opened')
def verify_terms_and_conditions(context):
    context.app.terms_and_conditions_page.verify_terms_and_conditions()

@then('User can close new window and switch back to original')
def switch_to_original(context):
    context.app.sign_in_page.close()
def return_to_original_window(context):
    context.app.sign_in_page.switch_to_window_id(context.original_window)
