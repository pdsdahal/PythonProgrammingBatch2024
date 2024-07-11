import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

option = webdriver.ChromeOptions()
option.add_argument("start-maximized")

web_driver = webdriver.Chrome(options=option)
web_driver.get('https://www.hyperlinkinfosystem.com/contact.html')


web_elm_choose_file = web_driver.find_element(by=By.ID, value='files_doc')
# web_driver.execute_script("arguments[0].scrollIntoView(true);", web_elm_choose_file)
web_driver.execute_script("""
    var element = arguments[0];
    var viewportHeight = window.innerHeight;
    var elementPosition = element.getBoundingClientRect().top + window.scrollY;
    var scrollPosition = elementPosition - (viewportHeight / 2);
    window.scrollTo(0, scrollPosition);
""", web_elm_choose_file)
time.sleep(3)
web_elm_choose_file.send_keys('/Users/sdahal/GitRepos/PythonProgrammingBatch2024/CorePython/Resources/Student.csv')

# slider
web_elm_knob = web_driver.find_element(by=By.XPATH, value="//span[contains(@class,'ui-slider-handle ui-corner-all')]")
action = ActionChains(driver=web_driver)
action.drag_and_drop_by_offset(web_elm_knob,100,0).perform()

time.sleep(5)