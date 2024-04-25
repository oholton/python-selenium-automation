from selenium.webdriver.common.by import By
from pages.base_page import Base
from selenium.webdriver.support import expected_conditions as EC



class SearchResultsPage(Base):
    SEARCH_RESULT = (By.XPATH, "//div[@data-test='resultsHeading']")
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "#addToCartButtonOrTextIdFor88827592")
    CART_BTTN = (By.XPATH, "//a[@href='/cart']")
    ADD_CART_SIDEBUTTON = (By.CSS_SELECTOR, "button[data-test='orderPickupButton']")

    def verify_search(self, expected_item):
        actual_text = self.driver.find_element(*self.SEARCH_RESULT).text
        assert expected_item in actual_text, f"Error! Text {expected_item} not found in {actual_text}"

    def add_to_cart(self, *locator):
        self.click(*self.ADD_TO_CART_BUTTON)
        self.wait.until(EC.element_to_be_clickable((self.ADD_CART_SIDEBUTTON))).click()

    def proceed_to_cart(self, *locator):
       self.wait_to_click(*self.CART_BTTN)
