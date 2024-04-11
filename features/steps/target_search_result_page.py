from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

SEARCH_RESULT = (By.XPATH, "//div[@data-test='resultsHeading']")
SEARCH_INPUT = (By.ID, 'search')
SEARCH_BUTTON = (By.XPATH, "//button[@type='submit']")

@then('Verify search results are for {searched_item}')
def verify_search(context, searched_item):
    actual_text = context.driver.find_element(*SEARCH_RESULT).text
    assert searched_item in actual_text, f"Error! Text {searched_item} not found in {actual_text}"