from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.base_page import Base

@given('Open Help page for Returns')
def open_help(context):
    context.app.help_page.open_page()

@then('Verify help Returns page opened')
def verify_help_page_open(context):
    context.app.help_page.verify_help_page()

@when('Select help topic Gift Cards')
def select_topic(context):
    context.app.help_page.select_drop()
@then('Verify help Gift Cards page opened')
def verify_gift_cards_page_opened(context):
    context.app.help_page.verify_gift_card()


