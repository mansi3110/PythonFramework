from selenium.webdriver.common.by import By

from pageObjects.CofirmPage import ConfirmPage


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver

        # self.driver.find_element(By.ID, "checkout").click()
        # self.driver.find_element(By.ID, "first-name").send_keys("Mansi")
        # self.driver.find_element(By.ID, "last-name").send_keys("Shah")
        # self.driver.find_element(By.ID, "postal-code").send_keys("M2M")
        # self.driver.find_element(By.ID, "continue").click()
        # self.driver.find_element(By.NAME, "finish").click()

    cart = (By.ID, "checkout")
    firstName = (By.ID, "first-name")
    lastName = (By.ID, "last-name")
    postalCode = (By.ID, "postal-code")
    continueBt = (By.ID, "continue")
    finish = (By.NAME, "finish")

    def cartButton(self):
        return self.driver.find_element(*CheckoutPage.cart)

    def getFirstname(self):
        return self.driver.find_element(*CheckoutPage.firstName)

    def getLastname(self):
        return self.driver.find_element(*CheckoutPage.lastName)

    def getPostalcode(self):
        return self.driver.find_element(*CheckoutPage.postalCode)

    def continueButton(self):
        return self.driver.find_element(*CheckoutPage.continueBt)

    def finishButton(self):
        self.driver.find_element(*CheckoutPage.finish).click()
        confirmPage = ConfirmPage(self.driver)
        return confirmPage



