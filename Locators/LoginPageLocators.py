from selenium.webdriver.common.by import By


class LoginPageLocators:
    USERNAME=(By.ID, "username")
    PASSWORD=(By.ID, "password")
    TERMS=(By.ID, "terms")
    SUBMIT=(By.ID, "signInBtn")