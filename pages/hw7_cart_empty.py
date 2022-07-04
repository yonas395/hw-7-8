from pages.base_page import page
from selenium.webdriver.common.by import By


class CartEmpty(page):
    CART_EMPTY = (By.CSS_SELECTOR, "[class*='a-row sc-your-amazon-cart-is-empty'] h2")

    def Verify_Cart_IS_Empty(self, expected_result):
        actual_result = self.driver.find_element(*self.CART_EMPTY).text
        assert expected_result == actual_result, f'Error! Actual result{actual_result} does not match with expected {expected_result}'
