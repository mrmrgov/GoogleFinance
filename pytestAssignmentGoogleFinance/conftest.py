import pytest
from selenium import webdriver
#Opens a webpage www.google.com/finance on a chrome browser

@pytest.fixture(scope="class")
def setUp(request):
    driver = webdriver.Chrome()
    driver.get("https://www.google.com/finance/")
    driver.maximize_window()
    request.cls.driver=driver
# closes the webpage after all tests are run
    yield
    driver.close()
