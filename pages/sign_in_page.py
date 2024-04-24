from pages.base_page import Base
from selenium.webdriver.common.by import By


class SignInPage(Base):
    SIGN_IN_FORM_OPEN = (By.XPATH, "//span[contains(text(), 'Sign into your Target account')]")

    def verify_sign_in_form_open(self):
        # actual_text = self.driver.find_element(*self.SIGN_IN_FORM_OPEN).text
        self.verify_text('Sign into your Target account', *self.SIGN_IN_FORM_OPEN)
        # actual_text = context.driver.find_element(By.XPATH, "//span[contains(text(), 'Sign into your Target account')]").text
        # assert 'Sign into your Target account' in actual_text, f"Error! Text Sign into your Target account not found in {actual_text}"
