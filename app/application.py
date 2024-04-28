# from pages.main_page import Base
from pages.main_page import MainPage
from pages.header import Header
from pages.search_results_page import SearchResultsPage
from pages.cart_page import Cart
from pages.nav_menu import NavMenu
from pages.sign_in_page import SignInPage
from pages.terms_and_conditons_page import TermsAndConditions



class Application:
    def __init__(self, driver):
        self.main_page = MainPage(driver)
        self.cart_page = Cart(driver)
        self.header = Header(driver)
        self.search_results_page = SearchResultsPage(driver)
        self.nav_menu = NavMenu(driver)
        self.sign_in_page = SignInPage(driver)
        self.terms_and_conditions_page = TermsAndConditions(driver)


# app = Application(driver)
# app.main_page
# app.header
# app.search_results_page