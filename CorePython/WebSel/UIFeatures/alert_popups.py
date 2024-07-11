import time

from selenium import webdriver
from selenium.webdriver.common.by import By

option = webdriver.ChromeOptions()
option.add_argument("start-maximized")

web_driver = webdriver.Chrome(options=option)
web_driver.get('https://mail.rediff.com/cgi-bin/login.cgi')

web_elm_signin = web_driver.find_element(by=By.NAME, value='proceed')
web_elm_signin.click()
time.sleep(1)

# handle alert
# switch the alert
alert = web_driver.switch_to.alert
actual_alert_msg = alert.text
print("Actual Alert Message : ",actual_alert_msg)
alert.accept()

time.sleep(3)
