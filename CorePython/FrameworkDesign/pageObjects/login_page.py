import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class LogInPage:
    lbl_email_css = "label[for='input-email']"
    txt_email_id = "input-email"

    lbl_password_css = "label[for='input-password']"
    txt_password_id = "input-password"

    btn_login_xpath = "//input[@class='btn btn-primary']"

    alert_no_match_both_login_css = "div.alert.alert-danger"

    def __init__(self, driver):
        self.driver = driver

    def check_lbl_email_displayed(self):
        return self.driver.find_element(by=By.CSS_SELECTOR, value=self.lbl_email_css).is_displayed()

    def get_lbl_txt_email(self):
        return self.driver.find_element(by=By.CSS_SELECTOR, value=self.lbl_email_css).text

    def check_txt_email_displayed(self):
        return self.driver.find_element(by=By.ID, value=self.txt_email_id).is_displayed()

    def set_email(self, email):
        email_field = self.driver.find_element(by=By.ID, value=self.txt_email_id)
        email_field.clear()
        email_field.send_keys(email)

    def check_lbl_password_displayed(self):
        return self.driver.find_element(by=By.CSS_SELECTOR, value=self.lbl_password_css).is_displayed()

    def get_lbl_txt_password(self):
        return self.driver.find_element(by=By.CSS_SELECTOR, value=self.lbl_password_css).text

    def check_txt_password_displayed(self):
        return self.driver.find_element(by=By.ID, value=self.txt_password_id).is_displayed()

    def set_password(self, password):
        password_field = self.driver.find_element(by=By.ID, value=self.txt_password_id)
        password_field.clear()
        password_field.send_keys(password)

    def click_login_button(self):
        self.driver.find_element(by=By.XPATH, value=self.btn_login_xpath).click()
        time.sleep(2)

    def get_alert_warning_both_no_match(self):
        return self.driver.find_element(by=By.CSS_SELECTOR, value=self.alert_no_match_both_login_css).text