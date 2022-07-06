from pages.base_page import page
from selenium.webdriver.common.by import By

class MainPage(page):

    def open_main_page(self):
        self.open_page("https://www.amazon.com/")
