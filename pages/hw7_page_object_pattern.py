from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import page

class ClickAmazonOrderslink(page):
    ORDER_BTN = (By.CSS_SELECTOR, "[id*='nav-orders'] [class*='nav-line-2']")

    def Click_Amazon_Orders_link(self):
        self.driver.find_element(*self.ORDER_BTN)
        self.click(*self.ORDER_BTN)
        sleep(3)


