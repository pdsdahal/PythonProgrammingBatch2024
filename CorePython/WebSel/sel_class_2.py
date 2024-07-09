import time

from selenium import webdriver
from selenium.webdriver.common.by import By

option = webdriver.ChromeOptions()
option.add_argument("start-maximized")

web_driver = webdriver.Chrome(options=option)
web_driver.get("https://ecommerce-playground.lambdatest.io/index.php?route=account/register")

actual_title = web_driver.title
print("Current Title : ", actual_title)
expected_title = "Register Account"
if actual_title == expected_title:
    print("title is as expected.")
else:
    print("title is not as expected.")


web_elm_firstname = web_driver.find_element(by=By.ID, value="input-firstname")

# check whether element is displayed or not in the browser
act_web_elm_firstname_di = web_elm_firstname.is_displayed()
exp_web_elm_firstname_di = True

if act_web_elm_firstname_di == exp_web_elm_firstname_di:
    print("Element is present.")
else:
    print("Element is not present.")

# check whether element is enabled or disabled
act_web_elm_firstname_en = web_elm_firstname.is_enabled()
exp_web_elm_firstname_en = True

if act_web_elm_firstname_en == exp_web_elm_firstname_en:
    print("Element is Enabled.")
else:
    print("Element is Disabled.")

# allow to enter the value in text field
web_elm_firstname.send_keys("Ram")

web_driver.find_element(by=By.ID, value="input-lastname").send_keys("Pandey")

time.sleep(3)