from behave import given, when, then
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

SEARCH_INPUT = (By.ID, 'search')
SEARCH_BUTTON = (By.XPATH, "//button[@type='submit']")
ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "#addToCartButtonOrTextIdFor88827592")
CART_BTTN = (By.XPATH, "//a[@href='/cart']")
ADD_CART_SIDEBUTTON = (By.CSS_SELECTOR, "button[data-test='orderPickupButton']")

@given('Open the main page')
def open_target(context):
    context.driver.get('https://www.target.com/')

@when('Search for {product} in search field')
def search_item(context, product):
    context.driver.find_element(*SEARCH_INPUT).send_keys(product)
    context.driver.find_element(*SEARCH_BUTTON).click()
    sleep(5)

@then('Add product into cart')
def add_to_cart(context):
    context.driver.find_element(*ADD_TO_CART_BUTTON).click()
    context.wait.until(EC.element_to_be_clickable((ADD_CART_SIDEBUTTON))).click()

@then('Proceed to cart')
def proceed_to_cart(context):
    context.wait.until(EC.element_to_be_clickable((CART_BTTN))).click()

@then('Verify item in cart')
def cart_verification(context):
    text = context.driver.find_element(By.CSS_SELECTOR, "[data-test='cartItem-qty']").text
    assert 'Qty' in text, f"Error! Qty is not showing up"

