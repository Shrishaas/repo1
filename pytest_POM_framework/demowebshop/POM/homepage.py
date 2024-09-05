from demowebshop.Lib.library import Base


class HomePage(Base):
    login_link_locator = ("xpath", "//a[.='Log in']")
    register_link_locator = ("xpath", "//a[.='Register']")

    def click_on_login(self):
        self.click_on_an_element(self.login_link_locator)

    def click_on_register(self):
        self.click_on_an_element(self.register_link_locator)
