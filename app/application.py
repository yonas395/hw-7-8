from pages.header import header
from pages.main_page import MainPage
from pages.search_result_page import SearchResultPage
from pages.hw7_page_object_pattern import ClickAmazonOrderslink
from pages.hw7_signin_page_opens import SigninPageOpens
from pages.hw7_cart_icon import ClickOnCartIcon
from pages.hw7_cart_empty import CartEmpty
from pages.hw8_department import Dept



class Application:

    def __init__(self, driver):
        self.driver = driver

        self.header = header(self.driver)
        self.main_page = MainPage(self.driver)
        self.search_result_page = SearchResultPage(self.driver)
        self.hw7_page_object_pattern = ClickAmazonOrderslink(self.driver)
        self.hw7_signin_page_opens = SigninPageOpens(self.driver)
        self.hw7_cart_icon = ClickOnCartIcon(self.driver)
        self.hw7_cart_empty = CartEmpty(self.driver)
        self.hw8_department = Dept(self.driver)


