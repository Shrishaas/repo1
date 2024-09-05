import pytest
from selenium.webdriver.chrome.webdriver import WebDriver

@pytest.fixture()
def driver():
    driver = WebDriver()
    driver.maximize_window()
    driver.get("https://demowebshop.tricentis.com/")
    yield driver
    driver.quit()