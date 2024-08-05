from selenium.webdriver import ActionChains


class TestUtil:

    @staticmethod
    def mouse_hover(driver, web_element):
        action = ActionChains(driver)
        action.move_to_element(web_element).perform()
