from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


SEARCH_INPUT = (By.ID, 'search')
SEARCH_BUTTON = (By.XPATH, "//button[@type='submit']")
ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "#addToCartButtonOrTextIdFor88827592")
CART_BTTN = (By.XPATH, "//a[@href='/cart']")
@given('Open the main page')
def open_target(context):
    context.driver.get('https://www.target.com/')

@when('Search for {product} in search field')
def search_item(context, product):
    context.driver.find_element(*SEARCH_INPUT).send_keys(product)
    context.driver.find_element(*SEARCH_BUTTON).click()
    sleep(4)

@then('Add product into cart')
def add_to_cart(context):
    context.driver.find_element(*ADD_TO_CART_BUTTON)
    sleep(4)
    context.driver.find_element(*ADD_TO_CART_BUTTON).click()
    sleep(5)
    context.driver.find_element(By.CSS_SELECTOR, "button[data-test='orderPickupButton']").click()
    sleep(3)

@then('Proceed to cart')
def proceed_to_cart(context):
    context.driver.find_element(*CART_BTTN).click()
    sleep(3)

@then('Verify item in cart')
def cart_verification(context):
    text = context.driver.find_element(By.CSS_SELECTOR, "[data-test='cartItem-qty']").text
    assert 'Qty' in text, f"Error! Qty is not showing up"

