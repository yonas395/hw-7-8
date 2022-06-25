from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


BST_SELL = (By.CSS_SELECTOR, "#zg_header a")
BST_HEADERS = (By.CSS_SELECTOR, "div[class='celwidget c-f'] [id*='zg_banner_text']")
PRI_NOT = (By.CSS_SELECTOR, "[class*='help-service-content'] a[href='https://www.amazon.com/privacy']")
NEW_RELEASE_LINKS = (By.CSS_SELECTOR, "[class*='_p13n-zg-nav-tab-all_style_zg-tabs__EYPLq'] a")
NEWR_HEADER = (By.CSS_SELECTOR, "[class*='celwidget c-f'] [id*='zg_banner_text']")


@given('Open Amazon T&C page')
def open_amazon_TC(context):
    context.driver.get("https://www.amazon.com/gp/help/customer/display.html/"
                       "ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088")


@given('open Amazon Bestsllers')
def open_amazon_best_seller_page(context):
    context.driver.get("https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers")


@given('open amazon new release')
def open_amazon_new_release(context):
    context.driver.get("https://www.amazon.com/gp/new-releases/?ref_=nav_cs_newreleases")


@when('Store original windows')
def store_window(context):
    context.original_window = context.driver.current_window_handle
    print(context.original_window)
    print(context.driver.current_window_handle)


@then('Click on Amazon Privacy Notice link')
def click_privacy_notice(context):
    context.driver.find_element(*PRI_NOT).click()


@then('Switch to the newly opened window')
def switch_to_new_window(context):
    context.driver.wait.until(EC.new_window_is_opened)
    print("\nAfter click, window:", context.driver.current_window_handle)
    all_window = context.driver.window_handles
    context.driver.switch_to.window(all_window[1])
    sleep(3)

@then('Verify Amazon Privacy Notice page is opened')
def verify_pn_opend(context):
    context.driver.wait.until(EC.url_contains("https://www.amazon.com/gp/help/customer/display."
                                              "html?nodeId=GX7NJQ4ZB8MHFRNJ"))
    sleep(3)


@then('User can close new window')
def close_new_window(context):
    context.driver.close()


@then('switch back to original window')
def switch_back_to_original_window(context):
    context.driver.switch_to.window(context.original_window)



@then("User can click through top links and verify correct page opens")
def click_thru_top_links(context):
    top_links = context.driver.find_elements(*BST_SELL)# counts the amounts of the link

    for x in range(len(top_links)):# from 0 to 4th
        link_to_click = context.driver.find_elements(*BST_SELL)[x]
        link_text = link_to_click.text
        link_to_click.click()
        sleep(2)
        header_text = context.driver.find_element(*BST_HEADERS).text
        assert link_text in header_text, f'Expected{link_text} to be in {header_text}'



@then("user can click through the links in side")
def click_the_links_in_coupon(context):
    coupon_links = context.driver.find_elements(*NEW_RELEASE_LINKS)

    for X in range(len(coupon_links)):
        clink_to_click = context.driver.find_elements(*NEW_RELEASE_LINKS)[X]
        linkk_text = clink_to_click.text
        clink_to_click.click()
        sleep(2)
        top_text = context.driver.find_element(*NEWR_HEADER).text
        assert linkk_text in top_text, f'Expected{linkk_text} to be in {top_text}'








