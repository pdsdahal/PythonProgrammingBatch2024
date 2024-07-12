import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

option = webdriver.ChromeOptions()
option.add_argument("start-maximized")

web_driver = webdriver.Chrome(options=option)
web_driver.get('https://ecommerce-playground.lambdatest.io/index.php')

web_elm_my_account = web_driver.find_element(by=By.LINK_TEXT, value='My account')

# mouse hover
action = ActionChains(driver=web_driver)
action.move_to_element(web_elm_my_account).perform()
time.sleep(1)

web_elm_register = web_driver.find_element(by=By.LINK_TEXT, value='Register')
web_elm_register.click()
time.sleep(4)