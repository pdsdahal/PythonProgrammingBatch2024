import time

import requests as requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

option = webdriver.ChromeOptions()
option.add_argument("start-maximized")

web_driver = webdriver.Chrome(options=option)
web_driver.get('https://ecommerce-playground.lambdatest.io/index.php?route=common/home')

time.sleep(2)
links = web_driver.find_elements(by=By.TAG_NAME, value='a')
print(len(links))

for link in links:
    url = link.get_attribute("href")
    try:
        res = requests.head(url)
        if res.status_code >= 400:
            print(f"{link} is broken.")
        else:
            print(f"{link} is good.")

    except Exception as e:
        print("Error : ",e)

time.sleep(2)