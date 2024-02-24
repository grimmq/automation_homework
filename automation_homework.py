from appium import webdriver
from appium.options.android import UiAutomator2Options
from selenium.webdriver.support.ui import WebDriverWait
import time
import locators
from utils import *

def init_driver():
    appium_server_url = 'http://localhost:4723'
    capabilities = {
        "platformName": "Android",
        "automationName": "uiautomator2",
        "deviceName": "Android",
        "appPackage": "com.android.chrome", 
        "appActivity": "com.google.android.apps.chrome.Main", 
        "noReset": True,
        "language":'en',
    }
    driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))
    return driver

def home_page(driver, url):
    driver.get(url)
    time.sleep(6)
    # 首頁截圖
    take_screenshot(driver, 'home_cathaybk')

def interact_with_elements(driver):
    wait = WebDriverWait(driver, 10)
    click_element(wait, locators.home_page_menu)
    click_element(wait, locators.click_product_description)
    click_element(wait, locators.click_credit_card)
    time.sleep(1)
    # 截圖列表
    take_screenshot(driver, 'product_list')

def count_credit_cards_and_swipe(driver, wait):
    # 信用卡數量
    project_count = credit_card_list(wait)
    print(f"信用卡數量: {project_count}")
    click_element(wait, locators.click_credit_introduce)
    time.sleep(5)
    swipe_up(driver, num=7)
    card_count = swip_left_and_take_screenshot(driver, num=10)
    print(f"停發卡數量:{card_count}")

def main():
    driver = init_driver()
    home_page(driver, 'https://www.cathaybk.com.tw/cathaybk/')
    interact_with_elements(driver)
    wait = WebDriverWait(driver, 10) 
    count_credit_cards_and_swipe(driver, wait)
    driver.quit()

if __name__ == "__main__":
    main()
