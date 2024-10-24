import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager



#1.Opens a webpage www.google.com/finance on a chrome browser

@pytest.fixture(scope="class")
def setUp(request):
    # options = Options()
    # options.binary_location = "C:\\Program Files\\Chrome\\chrome64_55.0.2883.75\\chrome.exe"
    # driver = webdriver.Chrome(chrome_options=options, executable_path=r'C:\path\to\chromedriver.exe')
    # driver.get('http://google.com/')
    # print("Chrome Browser Invoked")
    # driver.quit()
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = "C:\\Program Files\\Google\Chrome\\Application"  # Replace with your Chrome path
    #chrome_options = Options()
    chrome_options.add_argument("--headless")  # Uncomment if needed
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    # Initialize the Chrome driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    #driver = webdriver.Chrome(service=Service(), options=chrome_options)  # Add the path to ChromeDriver if necessary)
    driver.get("https://www.google.com/finance/")
    driver.maximize_window()
    request.cls.driver=driver
# closes the webpage after all tests are run
    yield
    driver.close()
