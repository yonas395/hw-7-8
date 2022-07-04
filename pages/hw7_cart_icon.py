from pages.base_page import page
from selenium.webdriver.common.by import By


class ClickOnCartIcon(page):
    CART_ICON = (By.CSS_SELECTOR, "[id*='nav-cart'] [class='nav-cart-icon nav-sprite']")

    def Click_on_cart_icon(self):
        self.driver.find_element(*self.CART_ICON)
        self.click(*self.CART_ICON)