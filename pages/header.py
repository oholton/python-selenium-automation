from selenium.webdriver.common.by import By
from pages.base_page import Base
from time import sleep

class Header(Base):
    SEARCH_INPUT = (By.ID, 'search')
    SEARCH_BUTTON = (By.XPATH, "//button[@type='submit']")

    def search_product(self, item):
        self.input_text(item, *self.SEARCH_INPUT)
        self.click(*self.SEARCH_BUTTON)
        sleep(6)
