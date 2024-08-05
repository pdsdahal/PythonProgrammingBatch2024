from selenium import webdriver
from selenium.webdriver.common.by import By


class RegisterPage:
    heading_register_account = (By.TAG_NAME, "h1")
    paragraph_already_account = (By.CSS_SELECTOR, "div#content>p")

    lbl_firstname = (By.XPATH, "//label[@for='input-firstname']")
    txt_firstname = (By.ID, "input-firstname")

    lbl_lastname = (By.XPATH, "//label[@for='input-lastname']")
    txt_lastname = (By.ID, "input-lastname")

    def __init__(self, driver):
        self.driver = driver

    def get_title_register_page(self):
        return self.driver.title

    # check heading tag (Register Account)
    def check_heading_register_account_displayed(self):
        return self.driver.find_element(*self.heading_register_account).is_displayed()

    def get_heading_register_account_txt(self):
        return self.driver.find_element(*self.heading_register_account).text

    # check P (If you already have an account with us, please login at the login page.)
    def check_paragraph_already_account_displayed(self):
        return self.driver.find_element(*self.paragraph_already_account).is_displayed()

    def get_paragraph_already_account_txt(self):
        return self.driver.find_element(*self.paragraph_already_account).text

    # First Name label
    def check_lbl_firstname_displayed(self):
        return self.driver.find_element(*self.lbl_firstname).is_displayed()

    def get_lbl_firstname_txt(self):
        return self.driver.find_element(*self.lbl_firstname).text

    # First Name textbox
    def check_txt_firstname_displayed(self):
        return self.driver.find_element(*self.txt_firstname).is_displayed()

    def enter_txt_firstname(self, firstname):
        return self.driver.find_element(*self.txt_firstname).send_keys(firstname)

    # Last Name label
    def check_lbl_lastname_displayed(self):
        return self.driver.find_element(*self.lbl_lastname).is_displayed()

    def get_lbl_lastname_txt(self):
        return self.driver.find_element(*self.lbl_lastname).text

    # First Name textbox
    def check_txt_lastname_displayed(self):
        return self.driver.find_element(*self.txt_lastname).is_displayed()

    def enter_txt_lastname(self, firstname):
        return self.driver.find_element(*self.txt_lastname).send_keys(firstname)
