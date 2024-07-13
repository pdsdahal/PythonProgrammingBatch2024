import pytest

from FrameworkDesign.pageObjects.login_page import LogInPage
from FrameworkDesign.utilities.base import BaseClass


@pytest.mark.usefixtures("setup")
class TestLogin(BaseClass):
    base_url = "https://ecommerce-playground.lambdatest.io/index.php?route=account/login"
    username = "ram@gmail.com"
    password = "1234"

    def test_verify_title_page(self):
        self.driver.get(self.base_url)
        actual_title = self.driver.title
        print(actual_title)

    def test_verify_login_with_credentials(self):
        self.driver.get(self.base_url)
        login_page = LogInPage(driver=self.driver)
        login_page.set_email(self.username)
        login_page.set_password(self.password)
        login_page.click_login_button()
