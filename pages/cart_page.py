from pages.base_page import Base
from selenium.webdriver.common.by import By
class Cart(Base):
    CART_HEADER = (By.CSS_SELECTOR, "h1[class*='StyledHeading']")
    EMPTY_CART_MESSAGE = (By.CSS_SELECTOR, "h1[class*='StyledHeading']")
    ITEM_IN_CART_TEXT = (By.CSS_SELECTOR, "[data-test='cartItem-qty']")

    def verify_cart_empty_message(self):
        self.verify_text('Your cart is empty', *self.EMPTY_CART_MESSAGE)

    def cart_verification(self):
        self.verify_partial_text('Qty', *self.ITEM_IN_CART_TEXT)

