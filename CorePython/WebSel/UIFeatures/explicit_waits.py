from selenium import webdriver
from selenium.common import NoSuchElementException, ElementNotVisibleException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

option = webdriver.ChromeOptions()
option.add_argument("start-maximized")

web_driver = webdriver.Chrome(options=option)
web_driver.get('https://www.hyperlinkinfosystem.com/contact.html')
web_driver.delete_all_cookies()

# Once set, the implicit wait is set for the life of the WebDriver object.
web_driver.implicitly_wait(2)

current_title_page = web_driver.title
print("Actual Title Page : ", current_title_page)

# Explicit Wait
try:
    web_elm = (WebDriverWait(driver=web_driver, timeout=10, poll_frequency=2, ignored_exceptions=[NoSuchElementException,ElementNotVisibleException,Exception]).
               until(EC.presence_of_element_located((By.CSS_SELECTOR, "span.ui-slider-handle.ui-corner-all.ui-state-default"))))
    print("Is Web Element is displayed : ",web_elm.is_displayed())

except Exception as e:
    print("Error : ", e)
