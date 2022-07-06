
from selenium.webdriver.common.by import By
from pages.base_page import page



class SearchResultPage(page):
    SEARCH_RESULT = (By.CSS_SELECTOR, "div[class*='a-section'] [class*='a-color-state']")

    def verify_search_result(self,expected_result):
        # actual_result = self.driver.find_element(*self.SEARCH_RESULT).text
       # assert expected_result == actual_result,f'Error!Actual text {actual_result} does not match expected {expected_result}'
        self.verify_text(expected_result, *self.SEARCH_RESULT)