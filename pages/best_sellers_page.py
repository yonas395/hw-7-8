from selenium.webdriver.common.by import By
from pages.base_page import page


class BestSellersPage(page):
    BST_SELL = (By.CSS_SELECTOR, "#zg_header a")
    BEST_SELLER = (By.CSS_SELECTOR, "a[href='/gp/bestsellers/?ref_=nav_cs_bestsellers']")


    def open_bestsellers(self):
        self.open_page("https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers")

    def verify_links_present(self):
        header_links = self.driver.find_elements(*self.BST_SELL)
        expected_amount = self.driver.find_elements(*self.BST_SELL)
        assert len(header_links) == len( expected_amount),\
            f'Expected {expected_amount} links, but got {len(header_links)}'
