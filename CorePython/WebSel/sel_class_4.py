import time

from selenium import webdriver
from selenium.webdriver.common.by import By

option = webdriver.ChromeOptions()
option.add_argument("start-maximized")

web_driver = webdriver.Chrome(options=option)
web_driver.get("https://ecommerce-playground.lambdatest.io/index.php?route=account/register")
web_driver.delete_all_cookies()

# Absolute XPath
web_elm_rg_h1 = web_driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[5]/div[1]/div/div/h1')
print("Actual Text : ",web_elm_rg_h1.text)

web_elm_first_name = web_driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[5]/div[1]/div/div/form/fieldset[1]/div[2]/div/input')
web_elm_first_name.send_keys("Roshan")

# Relative XPath
print("Content of H1 Tag : ",web_driver.find_element(by=By.XPATH, value='//div[@id="content"]//h1').text)

# Attribute-based XPath
web_elm_last_name = web_driver.find_element(by=By.XPATH, value='//input[@id="input-lastname"]')
web_elm_last_name.send_keys("Pandey")

# Text-based XPath
web_elm_email_lbl = web_driver.find_element(by=By.XPATH, value='//label[contains(text(),"E-Mail")]')
print("Actual Email Text Label : ", web_elm_email_lbl.text)
print("Is Present Check : ",web_elm_email_lbl.is_displayed())

# following XPath
web_elm_email = web_driver.find_element(by=By.XPATH, value='//label[@for="input-email"]//following::input[@placeholder="E-Mail"]')
web_elm_email.send_keys('abc@gmail.com')

# Following-sibling XPath
web_elm_pri_policy_lbl = web_driver.find_element(by=By.XPATH, value="//input[@id='input-agree']/following-sibling::label")
print("Actual Text Value of Privacy Policy : ",web_elm_pri_policy_lbl.text)

time.sleep(4)