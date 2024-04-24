from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from pages.main_page import Base

SEARCH_INPUT = (By.ID, 'search')
SEARCH_BUTTON = (By.XPATH, "//button[@type='submit']")
CART_BUTTON = (By.CSS_SELECTOR, "a[data-test='@web/CartLink']")
SIGN_IN_ICON = (By.XPATH, "//span[contains(@class, 'ListItemText') and text()='Sign in']")

@given('Open target main page')
def open_target(context):
    context.app.main_page.open_main()

#enter search
@when('Search for {item}')
def search_item(context, item):
    context.app.header.search_product(item)

@when('Click on cart icon')
def click_cart(context):
    context.app.header.click_cart()
    sleep(2)

sleep(3)