import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


#1.Opens a webpage www.google.com/finance on a chrome browser

@pytest.fixture(scope="class")
def setUp(request):
    # Configure Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Uncomment this line if you want to run tests in headless mode
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    # Initialize the Chrome driver
    driver = webdriver.Chrome(service=Service(), options=chrome_options)  # Add the path to ChromeDriver if necessary)
    driver.get("https://www.google.com/finance/")
    driver.maximize_window()
    request.cls.driver=driver
# closes the webpage after all tests are run
    yield
    driver.close()
