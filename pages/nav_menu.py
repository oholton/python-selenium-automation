from pages.base_page import Base
from selenium.webdriver.common.by import By
from time import sleep

class NavMenu(Base):
    NAV_MENU_SIGN_IN_BTN = (By.XPATH, "//span[contains(@class, 'ListItemText') and text()='Sign in']")

    def click_sign_in(self):
        self.click(*self.NAV_MENU_SIGN_IN_BTN)
        sleep(3)
