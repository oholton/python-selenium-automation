from selenium.webdriver.common.by import By
from time import sleep
from pages.base_page import Base
from selenium.webdriver.support.ui import Select

HEADER_RETURN = (By.XPATH, ("//h1[text()=' Returns']"))
TOPIC_SELECT = (By.CSS_SELECTOR, "select[id*='ViewHelpTopics']")
HEADER_GIFTCARD = (By.XPATH, "//h1[text()=' Target GiftCard balance']")




class HelpPage(Base):
    def open_page(self):
        self.open('https://help.target.com/help/SubCategoryArticle?childcat=Returns&parentcat=Returns+%26+Exchanges')

    def verify_help_page(self):
        self.verify_partial_text('Returns', *HEADER_RETURN)


    def select_drop(self):
        topic_sd = self.find_element(*TOPIC_SELECT)
        select = Select(topic_sd)
        select.select_by_value('Gift Cards')
        sleep(3)


    def verify_gift_card(self):
        self.verify_text('Target GiftCard balance', *HEADER_GIFTCARD)


