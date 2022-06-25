from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


COLOR_OPT = (By.CSS_SELECTOR, "#inline-twister-expander-content-color_name li[class*='desktop']")
COLOR_NAME = (By.CSS_SELECTOR, "#inline-twister-dim-title-color_name [id*='inline-twister-expanded-dimension-text-color_name']")


@then('verify user can click through colors')
def verify_colors(context):
    expected_colors = ['Light Wash, black', 'Blue, Over Dye', 'White', 'Dark Blue Vintage']
    actual_colors = []

    color_options = context.driver.find_elements(*COLOR_OPT)
    for option in color_options:
        option.click()
        sleep(5)
        color_name = context.driver.find_element(*COLOR_NAME).text
        actual_colors += [color_name]


        assert actual_colors == expected_colors, f'Error! Expected {expected_colors}, but got {actual_colors}'


        #$$("ul[class*='a'] li[class*='dimension']")