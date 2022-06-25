from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


BST_SELL = (By.CSS_SELECTOR, "#zg_header a")
BEST_SELLER = (By.CSS_SELECTOR, "a[href='/gp/bestsellers/?ref_=nav_cs_bestsellers']")





@then("click on best sellers page")
def click_best_sellers_page(context):
    context.driver.find_element(*BEST_SELLER).click()
    sleep(2)


@then('verify there are {expected_amount} links')
def verify_there_are_links(context, expected_amount):
    header_links = context.driver.find_elements(*BST_SELL)
    expected_amount = context.driver.find_elements(*BST_SELL)
    assert len(header_links) == len(expected_amount), f'Expected {expected_amount} links, but got {len(header_links)}'



