from pages.base_page import page
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select


class Dept(page):
    DEPARTMENT = (By.ID, "searchDropdownBox")
    DEPT_VERIFY = (By.CSS_SELECTOR, "[data-category*='{SUBSTRING}']")
    NEW_ARRIVAL = (By.CSS_SELECTOR, "[href='/New-Arrivals/b/?_encoding=UTF8&node=17020138011&ref_=sv_sl_6']")
    ARRIVAL_VERIFY = (By.CSS_SELECTOR, "[class*='nav-fullWidthSubnavFlyout nav-flyout']")

    def get_dpt_sub_nav_locator(self, department):
        return [self.DEPT_VERIFY[0], self.DEPT_VERIFY[1].replace('{SUBSTRING}', department)]


    #def Select_AWS_dept(self):
        #select = Select(self.find_element(*self.DEPARTMENT))
        #select.select_by_value("search-alias=courses")

    #def verify_dept(self):
        #self.wait_for_element_appear(*self.DEPT_VERIFY)

    def Select_AWS_dept(self, alias):
        select = Select(self.find_element(*self.DEPARTMENT))
        select.select_by_value(f"search-alias={alias}")

    def verify_dept(self, department):
        department_locator = self.get_dpt_sub_nav_locator(department)
        self.wait_for_element_appear(*department_locator)

    def open_amazon_product(self):
        self.open_page("https://www.amazon.com/gp/product/B074TBCSC8")

    def hover_New_Arrivals(self):
        actions =ActionChains(self.driver)
        newarival = self.find_element(*self.NEW_ARRIVAL)
        actions.move_to_element(newarival)
        actions.perform()

    def verify_user_see_the_deals(self):
        self.wait_for_element_appear(*self.ARRIVAL_VERIFY)


