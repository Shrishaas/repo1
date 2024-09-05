from demowebshop.POM.homepage import HomePage

class LogIn(HomePage):
    email_locator = ("id", "Email")
    password_locator = ("id", "Password")
    login_btn = ("xpath", "//input[@value='Log in']")

    def login_to_the_application(self, username, password):
        self.send_text_to_an_element(self.email_locator, username)
        self.send_text_to_an_element(self.password_locator, password)
        self.click_on_an_element(self.login_btn)
