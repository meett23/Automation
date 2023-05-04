from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time

driver=webdriver.Chrome(executable_path="/Users/tagline_144/Documents/Meet/chromedriver")

driver.implicitly_wait(5)

driver.maximize_window()
driver.get("https://www.trivago.com/")

driver.find_element_by_xpath("//*[@id='__next']/div[1]/div[4]/header/div[1]/nav/ul/li[4]/a/span[2]").click()
time.sleep(2)
driver.find_elements_by_xpath("//*[@id='q93k-origin-airport-display-multi-container']").click()
time.sleep(2)
#driver.find_elements_by_name("origin").send_keys("AMD")

