from appium.webdriver.common.appiumby import AppiumBy
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


def click_element(wait, xpath):
    element = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, xpath)))
    element.click()


def take_screenshot(driver, image_name):
    screenshot_file_path = f"C:/Users/grimm/OneDrive/桌面/homework/screenshot/{image_name}.png"
    driver.get_screenshot_as_file(screenshot_file_path)


def credit_card_list(wait):
    creditcard_list = [
    "卡片介紹",
    "刷卡優惠",
    "小樹點(信用卡)",
    "卡友登錄專區",
    "卡友理財服務",
    "卡友權益",
    "行動支付",
    "申請信用卡",
    ]

    creditcard_list_count  = 0
    for product_list in creditcard_list:
        try:
            elements = wait.until(EC.presence_of_all_elements_located((AppiumBy.XPATH, f'//android.view.View[@content-desc="{product_list}"]')))
            if elements:
                creditcard_list_count+=1
        except TimeoutException:
                print(f'缺少項目: "{product_list}"')

    return creditcard_list_count


def swipe_up(driver, num=1, duration=500):
    size = driver.get_window_size()
    width = size['width']
    height = size['height']

    start_x = width * 0.5
    start_y = height * 0.75
    end_y = height * 0.25

    for i in range(num):
        driver.swipe(start_x, start_y, start_x, end_y, duration)


def swip_left_and_take_screenshot(driver, num=1, duration=500):
    size = driver.get_window_size()
    width = size['width']
    height = size['height']

    start_x = width * 0.75
    start_y = height * 0.5
    end_y = height * 0.05

    card_count = 0
    for i in range(num):
        time.sleep(3)
        screenshot_path = f"C:/Users/grimm/OneDrive/桌面/homework/screenshot/card_{i+1}.png"
        driver.get_screenshot_as_file(screenshot_path)
        driver.swipe(start_x, start_y, end_y, start_x, duration)
        card_count += 1

    return card_count

