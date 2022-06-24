from selenium.webdriver.common.by import By


class ConfirmPage:
    def __init__(self, driver):
        self.driver = driver

    # self.driver.find_element(By.XPATH, "//div[@id='checkout_complete_container']/div").text
    message = (By.XPATH, "//div[@id='checkout_complete_container']/div")

    def getMessage(self):
        return self.driver.find_element(*ConfirmPage.message)