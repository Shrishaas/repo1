import pytest

from demowebshop.POM.homepage import HomePage
from demowebshop.POM.loginpage import LogIn

usernames = [("shrishaas88549@gmail.com","Shrisha@123"), ("abc@gmail.com","1234")]


@pytest.mark.parametrize("username,password", usernames)
def test_login_with_proper_credentials(driver):
    home = HomePage(driver)
    home.click_on_login()
    login = LogIn(driver)
    login.login_to_the_application("shrishaas88549@gmail.com", "Shrisha@123")
    assert driver.find_element("xpath", "//a[.='shrishaas88549@gmail.com']").is_displayed()

@pytest.mark.skip
def test_login_with_no_password(driver):
    home = HomePage(driver)
    home.click_on_login()
    login = LogIn(driver)
    login.login_to_the_application("shrishaas88549@gmail.com", "")
    assert driver.find_element("xpath", "//span[contains(.,'Login was unsuccessful')]").is_displayed()


def test_login_with_no_username(driver):
    home = HomePage(driver)
    home.click_on_login()
    login = LogIn(driver)
    login.login_to_the_application("", "Shrisha@123")
    assert driver.find_element("xpath", "//span[contains(.,'Login was unsuccessful')]").is_displayed()


def test_login_with_no_credntials(driver):
    home = HomePage(driver)
    home.click_on_login()
    login = LogIn(driver)
    login.login_to_the_application("", "")
    assert driver.find_element("xpath", "//span[contains(.,'Login was unsuccessful')]").is_displayed()


def test_login_with_invalid_credntials(driver):
    home = HomePage(driver)
    home.click_on_login()
    login = LogIn(driver)
    login.login_to_the_application("abc@gmail.com", "wastejava")
    assert driver.find_element("xpath", "//span[contains(.,'Login was unsuccessful')]").is_displayed()
