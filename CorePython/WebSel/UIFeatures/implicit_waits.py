from selenium import webdriver
from selenium.webdriver.common.by import By

option = webdriver.ChromeOptions()
option.add_argument("start-maximized")

web_driver = webdriver.Chrome(options=option)
web_driver.get('https://ecommerce-playground.lambdatest.io/index.php')
web_driver.delete_all_cookies()

# Once set, the implicit wait is set for the life of the WebDriver object.
web_driver.implicitly_wait(2)

current_title_page = web_driver.title
print("Actual Title Page : ",current_title_page)

web_elm_lbl_h4 = web_driver.find_element(by=By.XPATH, value="//h4[contains(text(),'Upto 50%')]")
print("Actual Label : ",web_elm_lbl_h4.text)