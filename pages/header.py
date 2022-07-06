from pages.base_page import page
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select


class header(page):
    #SEARCH_INPUT = (By.XPATH, "//input[@type='search']")
    SEARCH_INPUT =(By.ID, 'twotabsearchtextbox')
   # SEARCH_BTN = (By.CSS_SELECTOR, "div.a-box-inner .help-content")
    SEARCH_BTN = (By.ID, 'nav-search-submit-button')
    ORDER_BTN = (By.CSS_SELECTOR, "#nav-orders")
    FLAG = (By.CSS_SELECTOR, "[id*='icp-nav-flyout'] [class*='icp-nav-f']")
    SPANISH_LANG = (By.CSS_SELECTOR, "[href='#switch-lang=es_US']")
    DEPARTMENT = (By.ID, "searchDropdownBox")
    DEP_VERIFIC = (By.CSS_SELECTOR, "[data-category='books']")


    def Search_amazon(self, search_word):
        self.input_text(search_word, *self.SEARCH_INPUT)
        self.click(*self.SEARCH_BTN)

    def hover_over_language(self):
        actions = ActionChains(self.driver)
        flag = self.find_element(*self.FLAG)
        actions.move_to_element(flag)
        actions.perform()

    def verify_spanish_lang_present(self):
        self.wait_for_element_appear(*self.SPANISH_LANG)


    def Select_department(self):
        select = Select(self.find_element(*self.DEPARTMENT))
        select.select_by_value('search-alias=stripbooks')


    def verify_department(self):
        self.wait_for_element_appear(*self.DEP_VERIFIC)


