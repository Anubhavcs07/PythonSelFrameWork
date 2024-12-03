from Base.Base import BaseClass
from PageObject.LoginPage import LoginPage
import time

class TestLogin(BaseClass):
    def test_login(self):
        log = self.getLogger()
        login_page = LoginPage(self.driver)
        login_page.enter_username("rahulshettyacademy")
        login_page.enter_password("learning")
        login_page.click_checkbox()
        login_page.submit()
        time.sleep(5)
        log.info("Login Successfull")
        log.info(self.driver.title)
        assert self.driver.title == "ProtoCommerce", "Login Successful"