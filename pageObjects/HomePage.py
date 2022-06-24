from selenium.webdriver.common.by import By

from pageObjects.CheckoutPage import CheckoutPage


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    # self.driver.find_elements(By.XPATH, "//div[@class='inventory_item_description']/div[1]/a/div")
    #  self.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    # self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    Products = (By.XPATH, "//div[@class='inventory_item_description']/div[1]/a/div")
    ProductsList = (By.ID, "add-to-cart-sauce-labs-backpack")
    cart = (By.CLASS_NAME, "shopping_cart_link")

    def getProducts(self):
        return self.driver.find_elements(*HomePage.Products)

    def getProductsList(self):
        return self.driver.find_element(*HomePage.ProductsList)

    def cartButton(self, checkoutPage=None):
        self.driver.find_element(*HomePage.cart).click()
        checkoutPage = CheckoutPage(self.driver)
        return checkoutPage

