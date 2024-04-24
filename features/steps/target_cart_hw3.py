from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

EMPTY_CART_MESSAGE = (By.CSS_SELECTOR, "h1[class*='StyledHeading']")


@then('Verify “Your cart is empty” message is shown')
def verify_empty_cart(context):
    context.app.cart_page.verify_cart_empty_message()

