
from selenium.webdriver import ActionChains

class Base:
    def __init__(self, driver):
        self.driver = driver

    def search_for_an_element(self, locator):
        element = self.driver.find_element(*locator)
        return element

    def click_on_an_element(self, locator):
        element = self.search_for_an_element(locator)
        element.click()

    def double_click_on_an_element(self, locator):
        actions = ActionChains(self.driver)
        element = self.search_for_an_element(*locator)
        actions.double_click(element)

    def send_text_to_an_element(self, locator, text):
        element = self.search_for_an_element(locator)
        element.send_keys(text)