import os
from pathlib import Path

import pytest

from FrameworkDesign.WebDriver.base import BaseClass
from FrameworkDesign.pageObjects.home_page import HomePage
from FrameworkDesign.pageObjects.register_page import RegisterPage
from FrameworkDesign.utilities.customLogger import LogGeneration
from FrameworkDesign.utilities.testUtil import TestUtil


@pytest.mark.usefixtures("setup")
class TestRegister(BaseClass):
    logger = LogGeneration.get_info_log()
    base_path = Path(__file__).resolve().parent.parent
    excel_file_path = base_path / 'TestData' / 'InputData.xlsx'

    def setup_method(self, method):

        self.home_page = HomePage(self.driver)
        self.home_page.hover_over_my_account_menu()
        self.home_page.click_register_menu()

        self.register_page = RegisterPage(self.driver)

    @pytest.mark.regression
    def test_verify_register_title_page(self):
        self.logger.info("******** Started : test_verify_register_title_page ********")
        try:
            assert self.register_page.get_title_register_page() == "Register Account", "Title of Register page not as expected."
            self.logger.info("******** Finished : test_verify_register_title_page (PASSED) ********")
        except Exception as e:
            img_file_path = os.path.abspath(
                os.path.join(os.path.dirname(__file__), '..', 'Screenshots', 'test_verify_register_title_page.jpg'))
            self.driver.save_screenshot(img_file_path)
            self.logger.error("******** Exception occurred in test_verify_register_title_page ********", exc_info=True)
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_verify_register_components_displayed(self):
        self.logger.info("******** Started : test_verify_register_components_displayed ********")
        try:
            assert self.register_page.check_heading_register_account_displayed(), "Heading tag of Register Account was not displayed."
            assert self.register_page.check_paragraph_already_account_displayed(), "Paragraph already have an account was not displayed."

            assert self.register_page.check_lbl_firstname_displayed(), "FirstName label was not displayed."
            assert self.register_page.check_txt_firstname_displayed(), "FirstName textbox was not displayed."

            assert self.register_page.check_lbl_lastname_displayed(), "LastName label was not displayed."
            assert self.register_page.check_txt_lastname_displayed(), "LastName textbox was not displayed."
            self.logger.info("******** Finished : test_verify_register_components_displayed (PASSED) ********")

        except Exception as e:
            img_file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Screenshots',
                                                         'test_verify_register_components_displayed.jpg'))
            self.driver.save_screenshot(img_file_path)
            self.logger.error("******** Exception occurred in test_verify_register_components_displayed ********",
                              exc_info=True)
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    @pytest.mark.parametrize('firstname,lastname,email,telephone,password,con_password,newsletter',
                             TestUtil.read_excel_data(excel_file_path, 'valid_register'))
    def test_verify_valid_registration(self, firstname, lastname, email, telephone, password, con_password, newsletter):
        self.logger.info("******** Started : test_verify_valid_registration ********")
        try:
            self.register_page.enter_txt_firstname(firstname)
            self.register_page.enter_txt_lastname(lastname)
            self.logger.info("******** Finished : test_verify_valid_registration (PASSED) ********")

        except Exception as e:
            img_file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Screenshots',
                                                         'test_verify_valid_registration.jpg'))
            self.driver.save_screenshot(img_file_path)
            self.logger.error("******** Exception occurred in test_verify_valid_registration ********",
                              exc_info=True)
            assert False
