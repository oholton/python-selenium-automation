from selenium.webdriver.common.by import By
from pages.base_page import Base


class SearchResultsPage(Base):
    SEARCH_RESULT = (By.XPATH, "//div[@data-test='resultsHeading']")

    def verify_search(self, expected_item):
        actual_text = self.driver.find_element(*self.SEARCH_RESULT).text
        assert expected_item in actual_text, f"Error! Text {expected_item} not found in {actual_text}"
