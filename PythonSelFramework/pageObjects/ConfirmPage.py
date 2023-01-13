from selenium.webdriver.common.by import By


class ConfirmPage:
    def __init__(self, driver):
        self.driver = driver

    inputBox = (By.ID, "country")
    clickOnDrop = (By.LINK_TEXT, "India")
    purchaseButton = (By.CSS_SELECTOR, "[type='submit']")
    alert = (By.CSS_SELECTOR, "[class*='alert-success']")

    def searchLocation(self):
        return self.driver.find_element(*ConfirmPage.inputBox)

    def clickOnItem(self):
        return self.driver.find_element(*ConfirmPage.clickOnDrop)

    def clickOnPurchaseButton(self):
        return self.driver.find_element(*ConfirmPage.purchaseButton)

    def checkAlert(self):
        return self.driver.find_element(*ConfirmPage.alert)
