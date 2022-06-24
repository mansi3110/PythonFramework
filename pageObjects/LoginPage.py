import pytest
from selenium.webdriver.common.by import By

from pageObjects.HomePage import HomePage


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    # self.driver.find_element(By.ID, "user-name").send_keys("standard_user")
    # self.driver.find_element(By.NAME, "password").send_keys("secret_sauce")
    # self.driver.find_element(By.CLASS_NAME, "submit-button").click()
    userName = (By.ID, "user-name")
    password = (By.NAME, "password")
    submit = (By.CLASS_NAME, "submit-button")

    #@pytest.fixture(params=[("standard_user", "secret_sauce")])
    #def getLoginData(self, request):
        #return request.param

    def nameInfo(self):
        return self.driver.find_element(*LoginPage.userName)

    def passwordInfo(self):
        return self.driver.find_element(*LoginPage.password)

    def submitButton(self):
        self.driver.find_element(*LoginPage.submit).click()
        homePage = HomePage(self.driver)
        return homePage






