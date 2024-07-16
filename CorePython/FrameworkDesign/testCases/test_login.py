import pytest

from FrameworkDesign.pageObjects.login_page import LogInPage
from FrameworkDesign.utilities.base import BaseClass
from FrameworkDesign.utilities.readProperties import ReadConfig


@pytest.mark.usefixtures("setup")
class TestLogin(BaseClass):
    base_url = ReadConfig.get_base_url()
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()

    def setup_method(self, method):
        self.driver.get(self.base_url)
        self.login_page = LogInPage(driver=self.driver)

    def test_verify_title_page(self):
        try:
            self.driver.get(self.base_url)
            actual_title = self.driver.title
            assert actual_title == 'Account Logdxina', "Title is not as expected!"
        except Exception as e:
            self.driver.save_screenshot("./FrameworkDesign/Screenshots/test_verify_title_page.jpg")
            assert False

    def test_verify_login_elements_displayed(self):
        try:
            assert self.login_page.check_lbl_email_displayed(), "Label for email filed was not displayed."
            assert self.login_page.check_txt_email_displayed(), "Email textbox was not displayed."
            assert self.login_page.check_lbl_password_displayed(), "Label for password filed was not displayed."
            assert self.login_page.check_txt_password_displayed(), "Password textbox was not displayed."
        except Exception as e:
            self.driver.save_screenshot("./FrameworkDesign/Screenshots/test_verify_login_elements_displayed.jpg")
            assert False

    def test_verify_login_elements_text(self):
        try:
            assert self.login_page.get_lbl_txt_email() == "E-Mail Address", "Email label text as expected."
            assert self.login_page.get_lbl_txt_password() == "Password", "Password label text as expected."
        except Exception as e:
            self.driver.save_screenshot("./FrameworkDesign/Screenshots/test_verify_login_elements_text.jpg")
            assert False

    def test_verify_login_with_invalid_credentials(self):
        try:
            self.login_page.set_email(self.username)
            self.login_page.set_password(self.password)
            self.login_page.click_login_button()

            exp_warning_msg = "Warning: No match for E-Mail Address and/or Password."
            assert self.login_page.get_alert_warning_both_no_match() == exp_warning_msg, "Warning message not as expected for both invalid credentials."
        except Exception as e:
            self.driver.save_screenshot("./FrameworkDesign/Screenshots/test_verify_login_with_invalid_credentials.jpg")
            assert False
