import time

from selenium import webdriver
from selenium.webdriver.common.by import By

option = webdriver.ChromeOptions()
option.add_argument("start-maximized")

# Initialize the WebDriver
web_driver = webdriver.Chrome(options=option)

# Navigate to the main URL
web_driver.get('https://ecommerce-playground.lambdatest.io/index.php?route=account/register')
web_driver.delete_all_cookies()

# ID Locator
web_elm_firstname = web_driver.find_element(by=By.ID, value='input-firstname')
web_elm_firstname.send_keys("Ramhari")

# Name Locator
web_elm_lastname = web_driver.find_element(by=By.NAME, value='lastname')
web_elm_lastname.send_keys("Gajurel")

# Class Name Locator
web_elms = web_driver.find_elements(by=By.CLASS_NAME, value='form-control')
for index, web_elm in enumerate(web_elms):
    if index == 2:
        web_elm.send_keys('abc@gmail.com')
        break

# Tag Name Locator
web_elm_h1_register_acc = web_driver.find_element(by=By.TAG_NAME, value='h1')
print("Actual Text : ",web_elm_h1_register_acc.text)

# Link Text Locator
web_driver.find_element(by=By.LINK_TEXT, value='Home').click()


# Partial Link Text Locator
web_driver.find_element(by=By.PARTIAL_LINK_TEXT, value='Blo').click()

time.sleep(5)