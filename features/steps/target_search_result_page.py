from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

SEARCH_RESULT = (By.XPATH, "//div[@data-test='resultsHeading']")
SEARCH_INPUT = (By.ID, 'search')
SEARCH_BUTTON = (By.XPATH, "//button[@type='submit']")

@then('Verify search results are for {expected_item}')
def verify_search(context, expected_item):
    context.app.search_results_page.verify_search(expected_item)