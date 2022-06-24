import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
serv_Chromeobj = Service("C:\\chromedriver.exe")
serv_EdgeObj = Service("C:\\msedgedriver.exe")
#driver=webdriver.Chrome(service=serv_obj)
#driver=webdriver.Edge(service=serv_obj)


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome(service=serv_Chromeobj)

    elif browser_name == "microsoft-edge":
        driver = webdriver.Edge(service=serv_EdgeObj)

    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()

