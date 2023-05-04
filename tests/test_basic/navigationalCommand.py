from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome(executable_path="/Users/tagline_144/Documents/Meet/chromedriver")

driver.get("https://www.yatra.com/")
time.sleep(5)
driver.get("https://www.selenium.dev/")

time.sleep(5)
driver.back()

time.sleep(5)
driver.forward()
time.sleep(5)
driver.close()


