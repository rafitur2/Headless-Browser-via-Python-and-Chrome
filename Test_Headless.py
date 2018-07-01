import os  
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import pytest
import unittest
import time

chrome_options = Options()

##Using headless option



# chrome_options.binary_location = '/Applications/Google Chrome   Canary.app/Contents/MacOS/Google Chrome Canary'

# wd = webdriver.Chrome(chrome_options=chrome_options)

wd = webdriver.Chrome()

class Test_Headless(unittest.TestCase):

    def test_google_GUI(self):

        print("Starting GUI Browser Testing")
        start =time.time()
        wd.get("http://www.google.com")
        assert "Google" in wd.title
        if "Google" in wd.title:
            print("GUI browser testing has passed")
        else:
            print("GUI browser testing has passed failed")
        print ("Screen Shot was taken for GUI")
        wd.get_screenshot_as_file("ScreenShotGUI.png")
        wd.close()
        wd.quit()
        end=time.time()
        print("GUI Performance time is:",end-start)
        print("---------------------------------------------")

    def test_google_head_less(self):
        print("Starting headless Browser Testing")
        chrome_options.add_argument("--headless")
        wd = webdriver.Chrome(options=chrome_options)
        start =time.time()
        wd.get("http://www.google.com")
        # Simple testing webpage title
        assert "Google" in wd.title
        if "Google" in wd.title:
            print("Headless browser testing has passed")
        else:
            print("Headless browser testing has passed failed")
        print ("Screen Shot was taken for headless")
        wd.get_screenshot_as_file("ScreenShot_headless.png")
        wd.close()
        wd.quit()
        end=time.time()
        print("Headless Performance time is:",end-start)


if __name__ == '__main__':
    unittest.main()






