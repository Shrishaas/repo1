from demowebshop.POM.homepage import HomePage


def test_check_for_login(driver):
    home_page_obj = HomePage(driver)
    home_page_obj.click_on_login()


def test_check_for_register(driver):
    home_page_obj = HomePage(driver)
    home_page_obj.click_on_register()
