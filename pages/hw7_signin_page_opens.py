from pages.base_page import page
from selenium.webdriver.common.by import By

class SigninPageOpens(page):
  SIGNIN_PAGE = (By.CSS_SELECTOR, "div[class='a-section a-spacing-base']")

  def Verify_Sign_In_page_opened(self):
      actual_result = self.driver.find_element(*self.SIGNIN_PAGE)
      expected_result = self.driver.find_element(*self.SIGNIN_PAGE)
      assert expected_result == actual_result, f'Error! Actual result{actual_result} does not match with expected {expected_result}'




