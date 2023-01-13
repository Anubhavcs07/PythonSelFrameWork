import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from TestData.HomePage import HomePageData
from pageObjects.CheckoutPage import CheckOutPage
from pageObjects.ConfirmPage import ConfirmPage
from pageObjects.HomePage import HomePage
from tests.utilities.BaseClass import BaseClass
import time


class TestOne(BaseClass):

    def test_e2e(self, getData):
        log = self.getlogger()
        homePage = HomePage(self.driver)
        # homePage.shopItems().click()
        checkOutPage = homePage.shopItems()
        log.info("getting all cards titles")
        cards = checkOutPage.getCardTitles()
        # confirmPage = ConfirmPage(self.driver)

        print(cards)
        i = -1
        print(len(cards))
        for card in cards:
            i = i + 1
            cardText = card.text
            log.info(cardText)
            if cardText == "Blackberry":
                checkOutPage.getCardFooter()[i].click()
        checkOutPage.clickCheckoutButton().click()
        confirmPage = checkOutPage.successfulCheckout()
        log.info("entering country name")
        confirmPage.searchLocation().send_keys(getData["value"])
        # WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.LINK_TEXT, "India")))
        self.verifyLinkPresence("India")
        confirmPage.clickOnItem().click()
        confirmPage.clickOnPurchaseButton().click()
        textMatch = confirmPage.checkAlert().text
        log.info("text received from application is", textMatch)
        assert ("xsfsdf" in textMatch)

    # @pytest.fixture(params=[("ind")])
    # @pytest.fixture(params=[{"value":"ind"}])
    @pytest.fixture(params=HomePageData.test_HomePage_data)
    def getData(self, request):
        return request.param
