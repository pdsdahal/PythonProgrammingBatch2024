import pytest
from selenium import webdriver


class BaseClass:

    @pytest.fixture(scope="class")
    def setup(self, request):
        option = webdriver.ChromeOptions()
        option.add_argument("start-maximized")

        self.driver = webdriver.Chrome(options=option)
        request.cls.driver = self.driver
        yield

        self.driver.quit()
