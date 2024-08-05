from time import sleep

from selenium.webdriver.common.by import By

from FrameworkDesign.utilities.testUtil import TestUtil


class HomePage:
    menu_home = (By.LINK_TEXT, "Home")
    menu_blog = (By.LINK_TEXT, "Blog")
    menu_my_account = (By.LINK_TEXT, "My account")
    submenu_login = (By.PARTIAL_LINK_TEXT, "Login")
    submenu_register = (By.LINK_TEXT, "Register")

    def __init__(self, driver):
        self.driver = driver

    def get_current_title(self):
        return self.driver.title

    # home
    def is_home_menu_displayed(self):
        return self.driver.find_element(*self.menu_home).is_displayed()

    def click_home_menu(self):
        self.driver.find_element(*self.menu_home).click()

    # blog
    def is_blog_menu_displayed(self):
        return self.driver.find_element(*self.menu_blog).is_displayed()

    # my account
    def is_my_account_menu_displayed(self):
        return self.driver.find_element(*self.menu_my_account).is_displayed()

    # my account hover
    def hover_over_my_account_menu(self):
        sleep(3)
        TestUtil.mouse_hover(driver=self.driver,
                             web_element=self.driver.find_element(*self.menu_my_account))

    # login
    def is_login_menu_displayed(self):
        return self.driver.find_element(*self.submenu_login).is_displayed()

    def click_login_menu(self):
        sleep(3)
        self.driver.find_element(*self.submenu_login).click()

    # register
    def is_register_menu_displayed(self):
        return self.driver.find_element(*self.submenu_register).is_displayed()

    def click_register_menu(self):
        self.driver.find_element(*self.submenu_register).click()
