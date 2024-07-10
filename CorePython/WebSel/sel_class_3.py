import time
from selenium import webdriver
from selenium.webdriver.common.by import By

option = webdriver.ChromeOptions()
option.add_argument("start-maximized")

web_driver = webdriver.Chrome(options=option)
web_driver.get("https://ecommerce-playground.lambdatest.io/index.php?route=account/register")
web_driver.delete_all_cookies()

#1. Select element by using tag
web_elm_reg_acc = web_driver.find_element(by=By.TAG_NAME, value="h1")
actual_text = web_elm_reg_acc.text
print(actual_text)

# 1. Selects elements based on their tag name using css
web_elms_lbls = web_driver.find_elements(by=By.CSS_SELECTOR, value= "label")
web_elm_email_lbl = None
for web_elm_lbl in web_elms_lbls:
    actual_lbl_txt = web_elm_lbl.text
    if actual_lbl_txt == "E-Mail":
        web_elm_email_lbl = web_elm_lbl
        break

if web_elm_email_lbl:
    print("Actual Text : ",web_elm_email_lbl.text)
else:
    print("Label with E-Mail text not found!")

# 2. ID Selector: Syntax: #id
web_driver.find_element(by=By.CSS_SELECTOR, value="#input-firstname").send_keys("Ramhari")

# 3. Class Selector: Syntax: .className
web_elm_txt_flds = web_driver.find_elements(by=By.CSS_SELECTOR, value=".form-control")
for index,web_elm_txt_fld in enumerate(web_elm_txt_flds):
    if index == 1:
        web_elm_txt_fld.send_keys("Dahal")
        break

# 4. Attribute Selector: Syntax: [attribute=‘value’]
web_driver.find_element(by=By.CSS_SELECTOR, value='[id="input-email"]').send_keys('abc@gmail.com')

# 5. Child Selector: Syntax: parent > child
web_driver.find_element(by=By.CSS_SELECTOR, value='[class="col-sm-10"] > [id="input-telephone"]').send_keys('0123456789')

# 6. Descendant Selector: Syntax: ancestor descendant
web_driver.find_element(by=By.CSS_SELECTOR, value='.float-right [value="Continue"]').click()

time.sleep(4)