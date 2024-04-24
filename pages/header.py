from selenium.webdriver.common.by import By
from pages.base_page import Base
from time import sleep

class Header(Base):
    SEARCH_INPUT = (By.ID, 'search')
    SEARCH_BUTTON = (By.XPATH, "//button[@type='submit']")
    CART_BUTTON = (By.CSS_SELECTOR, "a[data-test='@web/CartLink']")
    SIGN_IN_ICON = (By.XPATH, "//span[text()='Sign in']")

    def search_product(self, item):
        self.input_text(item, *self.SEARCH_INPUT)
        self.click(*self.SEARCH_BUTTON)
        sleep(6)

    def click_cart(self):
        self.click(*self.CART_BUTTON)

    def click_sign_in(self):
        self.click(*self.SIGN_IN_ICON)

