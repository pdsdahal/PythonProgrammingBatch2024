from selenium.webdriver.common.by import By


class LogInPage:
    lbl_email_css = "label[for='input-email']"
    txt_email_id = "input-email"

    lbl_password_css = "label[for='input-password']"
    txt_password_id = "input-password"

    btn_login_xpath = "//input[@class='btn btn-primary']"

    def __init__(self, driver):
        self.driver = driver

    def set_email(self, email):
        email_field = self.driver.find_element(by=By.ID, value=self.txt_email_id)
        email_field.clear()
        email_field.send_keys(email)

    def set_password(self, password):
        password_field = self.driver.find_element(by=By.ID, value=self.txt_password_id)
        password_field.clear()
        password_field.send_keys(password)

    def click_login_button(self):
        self.driver.find_element(by=By.XPATH, value=self.btn_login_xpath).click()
