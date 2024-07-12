import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

option = webdriver.ChromeOptions()
option.add_argument("start-maximized")

web_driver = webdriver.Chrome(options=option)
web_driver.get('https://ecommerce-playground.lambdatest.io/index.php?route=product/manufacturer/info&manufacturer_id=8')

time.sleep(2)
# drop down
web_elm_show = web_driver.find_element(by=By.ID, value='input-limit-212433')
select = Select(web_elm_show)
select.select_by_visible_text('75')

# bootstrap drop down
web_elm_btn_dd = web_driver.find_element(by=By.XPATH, value="(//button[@type='button'])[1]")
web_elm_btn_dd.click()

web_elms_categories = web_driver.find_elements(by=By.XPATH, value="//div[@class='dropdown-menu dropdown-menu-left show']/a[@class='dropdown-item']")
for index,web_elms_category in enumerate(web_elms_categories):
    if index == 2:
        web_elms_category.click()
        break

time.sleep(4)