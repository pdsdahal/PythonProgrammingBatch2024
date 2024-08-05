import pytest
import os

from FrameworkDesign.WebDriver.base import BaseClass
from FrameworkDesign.pageObjects.home_page import HomePage
from FrameworkDesign.pageObjects.login_page import LogInPage
from FrameworkDesign.utilities.readProperties import ReadConfig
from FrameworkDesign.utilities.customLogger import LogGeneration


@pytest.mark.usefixtures("setup")
class TestLogin(BaseClass):
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()
    logger = LogGeneration.get_info_log()

    def setup_method(self, method):
        self.driver.get(self.base_url)
        self.home_page = HomePage(driver=self.driver)
        self.home_page.hover_over_my_account_menu()
        self.home_page.click_login_menu()
        self.login_page = LogInPage(driver=self.driver)

    def test_verify_title_page(self):
        self.logger.info("******** Started : test_verify_title_page ********")
        try:
            actual_title = self.driver.title
            assert actual_title == 'Account Login', "Title is not as expected!"
            self.logger.info("******** Finished : test_verify_title_page (PASSED) ********")
        except Exception as e:
            img_file_path = os.path.abspath(
                os.path.join(os.path.dirname(__file__), '..', 'Screenshots', 'test_verify_title_page.jpg'))
            self.driver.save_screenshot(img_file_path)
            self.logger.error("******** Exception occurred in test_verify_title_page ********", exc_info=True)
            assert False

    def test_verify_login_elements_displayed(self):
        try:
            self.logger.info("******** Started : test_verify_login_elements_displayed ********")
            assert self.login_page.check_lbl_email_displayed(), "Label for email field was not displayed."
            assert self.login_page.check_txt_email_displayed(), "Email textbox was not displayed."
            assert self.login_page.check_lbl_password_displayed(), "Label for password field was not displayed."
            assert self.login_page.check_txt_password_displayed(), "Password textbox was not displayed."
            self.logger.info("******** Finished : test_verify_login_elements_displayed (PASSED) ********")
        except Exception as e:
            img_file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Screenshots',
                                                         'test_verify_login_elements_displayed.jpg'))
            self.driver.save_screenshot(img_file_path)
            self.logger.exception("******** Exception occurred in test_verify_login_elements_displayed ********",
                                  exc_info=True)
            assert False

    def test_verify_login_elements_text(self):
        try:
            self.logger.info("******** Started : test_verify_login_elements_text ********")
            assert self.login_page.get_lbl_txt_email() == "E-Mail Address", "Email label text is not as expected."
            assert self.login_page.get_lbl_txt_password() == "Password", "Password label text is not as expected."
            self.logger.info("******** Finished : test_verify_login_elements_text (PASSED) ********")
        except Exception as e:
            img_file_path = os.path.abspath(
                os.path.join(os.path.dirname(__file__), '..', 'Screenshots', 'test_verify_login_elements_text.jpg'))
            self.driver.save_screenshot(img_file_path)
            self.logger.exception("******** Exception occurred in test_verify_login_elements_text ********",
                                  exc_info=True)
            assert False

    def test_verify_login_with_invalid_credentials(self):
        try:
            self.logger.info("******** Started : test_verify_login_with_invalid_credentials ********")
            self.login_page.set_email(self.username)
            self.login_page.set_password(self.password)
            self.login_page.click_login_button()

            exp_warning_msg = "Warning: No match for E-Mail Address and/or Password."
            assert self.login_page.get_alert_warning_both_no_match() == exp_warning_msg, "Warning message not as expected for invalid credentials."
            self.logger.info("******** Finished : test_verify_login_with_invalid_credentials (PASSED) ********")
        except Exception as e:
            img_file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Screenshots',
                                                         'test_verify_login_with_invalid_credentials.jpg'))
            self.driver.save_screenshot(img_file_path)
            self.logger.exception("******** Exception occurred in test_verify_login_with_invalid_credentials ********",
                                  exc_info=True)
            assert False
