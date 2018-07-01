import os  
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

chrome_options = Options()  
chrome_options.add_argument("--headless")  
# chrome_options.binary_location = '/Applications/Google Chrome   Canary.app/Contents/MacOS/Google Chrome Canary'

wd = webdriver.Chrome(chrome_options=chrome_options)
wd.get("http://www.google.com")




#Simple testing webpage title
assert "Google" in wd.title
if "Google" in wd.title:
    print ("Pass")
else:
    print ("Failed")




