from Base.Base import BaseClass
from Locators.LoginPageLocators import LoginPageLocators

class LoginPage(BaseClass):
    def __init__(self, driver):
        self.driver = driver
        self.loginPageLocators = LoginPageLocators()

    def enter_username(self, username):
        self.enter_text(self.loginPageLocators.USERNAME, username)

    def enter_password(self, password):
        self.enter_text(self.loginPageLocators.PASSWORD, password)

    def click_checkbox(self):
        self.click(self.loginPageLocators.TERMS)

    def submit(self):
        self.click(self.loginPageLocators.SUBMIT)