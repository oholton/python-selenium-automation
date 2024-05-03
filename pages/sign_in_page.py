from pages.base_page import Base
from selenium.webdriver.common.by import By
from time import sleep

class SignInPage(Base):
    SIGN_IN_FORM_OPEN = (By.XPATH, "//span[contains(text(), 'Sign into your Target account')]")
    TARGET_SIGN_IN_PAGE = ('https://www.target.com/login?client_id=ecom-web-1.0.0&ui_namespace=ui-default&back_button_action=browser&keep_me_signed_in=true&kmsi_default=false&actions=create_session_signin')
    SIGN_IN_ICON = (By.XPATH, "//span[text()='Sign in']")
    NAV_MENU_SIGN_IN_BTN = (By.XPATH, "//span[contains(@class, 'ListItemText') and text()='Sign in']")
    TERMS_AND_COND_BTN = (By.CSS_SELECTOR, "[aria-label*='terms & conditions']")
    USERNAME = (By.CSS_SELECTOR, "#username")
    PASSWORD = (By.CSS_SELECTOR, "#password")
    INCORRECT_USERNAME = ('asdfghjkl@yahoo.com')
    INCORRECT_PASSWORD = ('password1234')
    SIGN_IN_BTN = (By.CSS_SELECTOR, "#login")
    CANNOT_FIND_ACCOUNT = (By.CSS_SELECTOR, "[data-test*='authAlertDisplay']")


    def verify_sign_in_form_open(self):
        # actual_text = self.driver.find_element(*self.SIGN_IN_FORM_OPEN).text
        self.verify_text('Sign into your Target account', *self.SIGN_IN_FORM_OPEN)
        # actual_text = context.driver.find_element(By.XPATH, "//span[contains(text(), 'Sign into your Target account')]").text
        # assert 'Sign into your Target account' in actual_text, f"Error! Text Sign into your Target account not found in {actual_text}"

    def open_sign_in_page(self):
        self.open('https://www.target.com/')
        self.click(*self.SIGN_IN_ICON)
        self.wait_to_click(*self.NAV_MENU_SIGN_IN_BTN)
        sleep(3)
    def terms_and_conditions(self):
        self.click(*self.TERMS_AND_COND_BTN)
        sleep(3)

    def switch_to_next_window(self):
        self.switch_to_new_window()

    def bad_username_input(self):
        self.input_text(self.INCORRECT_USERNAME, *self.USERNAME)
        sleep(3)


    def bad_password_input(self):
        self.input_text(self.INCORRECT_PASSWORD, *self.PASSWORD)
        sleep(3)


    def click_sign_in_btn(self):
        self.click(*self.SIGN_IN_BTN)


    def verify_cannot_signin(self):
        element = self.find_element(*self.CANNOT_FIND_ACCOUNT)
        assert element.is_displayed(), "We can't find your account.' message is not shown"




