import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_titleCheck(self):

        title_text = self.driver.title
        print(title_text)
        expected_title="Google Finance - Stock Market Prices, Real-time Quotes & Business News"
        assert title_text==expected_title,f"Titles do not match, incorrect webpage, expected : {expected_title}"




