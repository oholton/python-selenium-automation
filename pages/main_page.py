from pages.base_page import Base

class MainPage(Base):

    def open_main(self):
        self.driver.get('https://www.target.com/')

