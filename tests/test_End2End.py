import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from pageObjects.CheckoutPage import CheckoutPage
from pageObjects.CofirmPage import ConfirmPage
from pageObjects.HomePage import HomePage
from pageObjects.LoginPage import LoginPage
from utilities.BaseClass import BaseClass



#@pytest.mark.usefixtures("getLoginData")
class TestOne(BaseClass):
    def test_e2e(self):
        log = self.getLogger()
        loginPage = LoginPage(self.driver)
        # homePage = HomePage(self.driver)
        # checkoutPage = CheckoutPage(self.driver)
        # confirmPage = ConfirmPage(self.driver)
        log.info("Customer's login info")
        loginPage.nameInfo().send_keys("standard_user")
        loginPage.passwordInfo().send_keys("secret_sauce")
        homePage=loginPage.submitButton()

        Products = homePage.getProducts()
        i = -1
        for product in Products:
            i = i + 1
            ProductName = product.text
            log.info(ProductName)
            if ProductName == "Sauce Labs Backpack":
                homePage.getProductsList().click()

        checkoutPage = homePage.cartButton()

        checkoutPage.cartButton().click()
        log.info("Customer's Personal Details")
        checkoutPage.getFirstname().send_keys("Mansi")
        checkoutPage.getLastname().send_keys("Shah")
        checkoutPage.getPostalcode().send_keys("M2M")
        checkoutPage.continueButton().click()
        confirmPage = checkoutPage.finishButton()
        DispatchedMessage = confirmPage.getMessage().text
        log.info("Text received from Application: "+ DispatchedMessage)

        assert "order has been dispatched" in DispatchedMessage

        self.driver.get_screenshot_as_file("screen.png")




