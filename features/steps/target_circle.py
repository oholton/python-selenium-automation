from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

driver_path = ChromeDriverManager().install()

service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

JOIN_TARGET = (By.XPATH, "//h3[contains(text(), 'Join Target Circle')]")
VOTING_TARGET = (By.CSS_SELECTOR, "[data-lnk='Voting ']")
PARTERS_TARGET = (By.CSS_SELECTOR, "[data-lnk='Partner']")
DEALS_TARGET = (By.CSS_SELECTOR, "[data-lnk='Circle Deals ']")
BONUS_TARGET = (By.CSS_SELECTOR, "[data-lnk='Bonus']")
FAQ_TARGET = (By.CSS_SELECTOR, "[data-lnk='Circe FAQs']")
BENEFIT_BOXES = [JOIN_TARGET, VOTING_TARGET, PARTERS_TARGET, DEALS_TARGET, BONUS_TARGET, FAQ_TARGET]

@given('Open target circle page')
def open_circle(context):
    context.driver.get('https://www.target.com/circle')
@then('Verify page have 6 benefit boxes')
def verify_benefits(context):
    benefit_boxes =[]
    benefit_boxes.append(context.driver.find_elements(*JOIN_TARGET))
    benefit_boxes.append(context.driver.find_elements(*VOTING_TARGET))
    benefit_boxes.append(context.driver.find_elements(*PARTERS_TARGET))
    benefit_boxes.append(context.driver.find_elements(*DEALS_TARGET))
    benefit_boxes.append(context.driver.find_elements(*BONUS_TARGET))
    benefit_boxes.append(context.driver.find_elements(*FAQ_TARGET))
    assert len(benefit_boxes) == 6, f"Expected 6 benefit boxes but got {len(benefit_boxes)}"
# for boxes in BENEFIT_BOXES:
#     print(boxes)
