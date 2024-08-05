import os

import pytest

from FrameworkDesign.WebDriver.base import BaseClass
from FrameworkDesign.pageObjects.home_page import HomePage
from FrameworkDesign.utilities.customLogger import LogGeneration


@pytest.mark.usefixtures("setup")
class TestHome(BaseClass):
    logger = LogGeneration.get_info_log()

    def setup_method(self, method):
        self.driver.get(self.base_url)
        self.home_page = HomePage(driver=self.driver)

    @pytest.mark.regression
    def test_verify_title_page_home(self):
        self.logger.info("******** Started : test_verify_title_page_home ********")
        try:
            assert self.home_page.get_current_title() == "Your Store", "Title not as expected."
            self.logger.info("******** Finished : test_verify_title_page_home (PASSED) ********")
        except Exception as e:
            img_file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Screenshots', 'test_verify_title_page_home.jpg'))
            self.driver.save_screenshot(img_file_path)
            self.logger.error("******** Exception occurred in test_verify_title_page_home ********", exc_info=True)
            assert False

