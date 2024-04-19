from behave import given, when, then
from selenium.webdriver.common.by import By
from time import sleep



COLORS_OPTIONS = (By.CSS_SELECTOR, "[class*='StyledVariationSelectorImage'] img")
PRODUCT_PAGE = ("https://www.target.com/p/A-54247255")

@given('Open product page')
def open_product_page(context):
    context.driver.get(PRODUCT_PAGE)

@when('Click on each color of product')
def click_colors(context):
    colors = context.driver.find_elements(*COLORS_OPTIONS)
    for color in colors:
        color.click()
        clicked_color = context.driver.find_element(By.XPATH, "//div[@class='styles__StyledHeaderWrapperDiv-sc-519sqw-3 bCzCRO']").text
        clicked_color = clicked_color.split('\n')[1]
        actual_colors.append(clicked_color)

# def find_colors(context)
expected_colors = ["Black", "Gray", "Railroad Gray", "Red Velvet", "White", "Xavier Navy"]
actual_colors = []

@then('Verify expected colors are selectable')
def verify_expected_colors(context):
    assert actual_colors == expected_colors, f"Expected colors does not match actual colors: {expected_colors}, got {actual_colors}"




