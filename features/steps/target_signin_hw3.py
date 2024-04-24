from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from pages.main_page import Base
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

NAV_MENU_SIGN_IN_BTN = (By.XPATH, "//span[contains(@class, 'ListItemText') and text()='Sign in']")

@given('Open Target page')
def open_target(context):
    context.driver.get('https://www.target.com/')
@when('Click on sign in')
def click_sign_in(context):
    context.app.header.click_sign_in()
    # context.driver.find_element(By.XPATH, "//span[text()='Sign in']").click()
@when('From right side navigation menu, click on sign in')
def navigate_to_sign_in(context):
    context.app.nav_menu.click_sign_in()
    #
    # context.app.wait.until(EC.presence_of_element_located((NAV_MENU_SIGN_IN_BTN))).click()
    # # context.driver.find_element(*NAV_MENU_SIGN_IN_BTN).click()
sleep(3)

@then('Verify sign in form opened')
def verify_form_open(context):
    context.app.sign_in_page.verify_sign_in_form_open()
    # actual_text = context.driver.find_element(By.XPATH, "//span[contains(text(), 'Sign into your Target account')]").text
    # assert 'Sign into your Target account' in actual_text, f"Error! Text Sign into your Target account not found in {actual_text}"
    sleep(3)

print('Test case passed')