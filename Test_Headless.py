import os  
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import pytest
import unittest

# chrome_options = Options()
# chrome_options.add_argument("--headless")


# chrome_options.binary_location = '/Applications/Google Chrome   Canary.app/Contents/MacOS/Google Chrome Canary'

# wd = webdriver.Chrome(chrome_options=chrome_options)

wd = webdriver.Chrome()

class Test_Headless(unittest.TestCase):

    def test_google(self):

        wd.get("http://www.google.com")
        # Simple testing webpage title
        assert "Google" in wd.title
        if "Google" in wd.title:
            print("Pass")
        else:
            print("Failed")
        wd.close()
        wd.quit()


if __name__ == '__main__':
    unittest.main()






