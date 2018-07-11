
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
#Add comments in GitHub


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--window-size=1420,1080')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
driver = webdriver.Chrome(chrome_options=chrome_options)



Value = "Under 20"
driver.get("http://www.teachmeselenium.com/automation-practice/")
time.sleep(10)
dropdown = Select(driver.find_element_by_name("age"))
dropdown.select_by_value(Value)
