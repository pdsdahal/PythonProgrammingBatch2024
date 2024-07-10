import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.window import WindowTypes

option = webdriver.ChromeOptions()
option.add_argument("start-maximized")

# Initialize the WebDriver
web_driver = webdriver.Chrome(options=option)

# Navigate to the main URL
web_driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
print("Title : ", web_driver.title)

web_driver.implicitly_wait(time_to_wait=0.5)

web_driver.find_element(by=By.NAME, value='username').send_keys("Admin")
web_driver.find_element(by=By.NAME, value='password').send_keys("admin123")
web_driver.find_element(by=By.TAG_NAME, value='button').click()

# Store the handle of the main window
main_window = web_driver.current_window_handle

# Open a new window
web_driver.switch_to.new_window(WindowTypes.WINDOW)
web_driver.get("https://ecommerce-playground.lambdatest.io/index.php?route=common/home")

# pause execution
time.sleep(5)

web_driver.close()

# Switch back to the main window
web_driver.switch_to.window(main_window)
# pause execution
time.sleep(5)

web_driver.quit()