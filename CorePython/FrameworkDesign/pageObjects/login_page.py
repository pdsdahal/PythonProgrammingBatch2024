import time
from selenium.webdriver.common.by import By


class LogInPage:
    lbl_email = (By.XPATH, "//label[@for='input-email']")
    txt_email = (By.ID, "input-email")

    lbl_password = (By.XPATH, "//label[@for='input-password']")
    txt_password = (By.ID, "input-password")

    btn_login = (By.XPATH, "//input[@class='btn btn-primary']")

    alert_no_match_both_login = (By.CSS_SELECTOR, "div.alert.alert-danger")

    def __init__(self, driver):
        self.driver = driver

    def check_lbl_email_displayed(self):
        return self.driver.find_element(*self.lbl_email).is_displayed()

    def get_lbl_txt_email(self):
        return self.driver.find_element(*self.lbl_email).text

    def check_txt_email_displayed(self):
        return self.driver.find_element(*self.txt_email).is_displayed()

    def set_email(self, email):
        email_field = self.driver.find_element(*self.txt_email)
        email_field.clear()
        email_field.send_keys(email)

    def check_lbl_password_displayed(self):
        return self.driver.find_element(*self.lbl_password).is_displayed()

    def get_lbl_txt_password(self):
        return self.driver.find_element(*self.lbl_password).text

    def check_txt_password_displayed(self):
        return self.driver.find_element(*self.txt_password).is_displayed()

    def set_password(self, password):
        password_field = self.driver.find_element(*self.txt_password)
        password_field.clear()
        password_field.send_keys(password)

    def click_login_button(self):
        self.driver.find_element(*self.btn_login).click()
        time.sleep(2)

    def get_alert_warning_both_no_match(self):
        return self.driver.find_element(*self.alert_no_match_both_login).text
