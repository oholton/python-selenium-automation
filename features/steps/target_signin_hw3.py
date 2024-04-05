from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


@given('Open Target page')
def open_target(context):
    context.driver.get('https://www.target.com/')
@when('Click on sign in')
def click_sign_in(context):
    context.driver.find_element(By.XPATH, "//span[text()='Sign in']").click()
@when('From right side navigation menu, click on sign in')
def navigate_to_sign_in(context):
    context.driver.find_element(By.XPATH, "//span[contains(@class, 'ListItemText') and text()='Sign in']").click()
sleep(3)

@then('Verify sign in form opened')
def verify_form_open(context):
    actual_text = context.driver.find_element(By.XPATH, "//span[contains(text(), 'Sign into your Target account')]").text
    assert 'Sign into your Target account' in actual_text, f"Error! Text Sign into your Target account not found in {actual_text}"
    sleep(3)

print('Test case passed')