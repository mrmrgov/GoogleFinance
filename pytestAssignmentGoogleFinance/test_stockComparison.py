import time

from selenium.webdriver.common.by import By

from utilities.BaseClass import BaseClass


class TestTwo(BaseClass):

#locate the "you may be interested in" text
    def test_symbolComparison(self):
        time.sleep(10)
        section = self.driver.find_element(By.XPATH,"//div[contains(text(),'You may be interested in')]/following-sibling::div")
#4.Compare the stock symbols retrieved from (3) with given test data

        stock_symbols=[]
        symbols = section.find_elements(By.TAG_NAME,"a")
        for symbol in symbols:
            stock_symbols.append(symbol.text)
        print(stock_symbols)
        test_data = ["NFLX", "MSFT", "TSLA"]
#5. Print all stock symbols that are in (3) but not in given test data

        symbols_not_in_testdata =[]
        for symbol in stock_symbols:
            if symbol not in test_data:
                symbols_not_in_testdata.append(symbol)
        print(f"These are the symbols in {stock_symbols} but not in {test_data}")
#6. Print all stock symbols that are in given test data but not in (3)
        symbols_in_testdata = []
        for symbol in test_data:
            if symbol not in stock_symbols:
                symbols_in_testdata.append(symbol)
        print(f"These are the symbols in {test_data} but not in {stock_symbols}")
