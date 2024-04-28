from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class Base:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def open(self, url):
        self.driver.get(url)

    def find_element(self, *locator):
        self.driver.find_element(*locator)
        return self.driver.find_element(*locator)

    def find_elements(self, *locator):
        self.driver.find_elements(*locator)
        return self.driver.find_elements(*locator)
    def click(self, *locator):
        self.find_element(*locator).click()

    def store_current_window(self):
        current_window = self.driver.current_window_handle
        print(f'Current window: {current_window}')
        return current_window

    def switch_to_new_window(self):
        self.wait.until(EC.new_window_is_opened)
        all_windows = self.driver.window_handles
        print('ALL windows:', self.driver.window_handles)
        print('Switching to... ', all_windows[1])
        self.driver.switch_to.window(all_windows[1])

    def switch_window_by_id(self, window_id):
        print('Switching to... ', window_id)
        self.driver.switch_to.window(window_id)

    def input_text(self, text, *locator):
        self.find_element(*locator).send_keys(text)

    def verify_text(self, expected_text, *locator):
        actual_text = self.find_element(*locator).text
        assert actual_text == expected_text, f"Expected {expected_text}, but got {actual_text}"

    def verify_partial_text(self, expected_text, *locator):
        actual_text = self.find_element(*locator).text
        assert expected_text in actual_text, f"Expected {expected_text} but got {actual_text}"

    def verify_partial_url(self, expected_partial_url):
        self.wait.until(EC.url_contains(expected_partial_url), message=f'Url does not contain {expected_partial_url}')
    def verify_url(self, expected_url, *locator):
        self.wait.until(EC.url_matches(expected_url))

    def wait_to_click(self, *locator):
        self.wait.until(EC.element_to_be_clickable((locator))).click()

    def close(self):
        self.driver.close()