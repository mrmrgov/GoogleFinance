import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager



#1.Opens a webpage www.google.com/finance on a chrome browser

@pytest.fixture(scope="class")
def setUp(request):
# Initialize the Chrome driver
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")  # running headless
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# open the webpage
    driver.get("https://www.google.com/finance/")
    driver.maximize_window()
    request.cls.driver=driver

# closes the webpage after all tests are run
    yield
    driver.close()
