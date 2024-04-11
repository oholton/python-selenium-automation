from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

SEARCH_INPUT = (By.ID, 'search')
SEARCH_BUTTON = (By.XPATH, "//button[@type='submit']")
CART_BUTTON = (By.CSS_SELECTOR, "a[data-test='@web/CartLink']")

@given('Open target main page')
def open_target(context):
    context.driver.get('https://www.target.com/')

#enter search
@when('Search for {item}')
def search_item(context, item):
    context.driver.find_element(*SEARCH_INPUT).send_keys(item)
    context.driver.find_element(*SEARCH_BUTTON).click()

@when('Click on cart icon')
def click_on_cart(context):
    context.driver.find_element(*CART_BUTTON).click()
    sleep(2)

sleep(3)