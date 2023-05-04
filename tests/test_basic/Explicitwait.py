import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome(executable_path="/Users/tagline_144/Documents/Meet/chromedriver")

driver.implicitly_wait(5)

driver.maximize_window()
driver.get("https://www.yatra.com/")

driver.find_element_by_id("BE_flight_origin_city").send_keys("BLR")

time.sleep(2)

driver.find_element_by_id("BE_flight_arrival_city").send_keys("MAA")

time.sleep(2)


#driver.find_element_by_id("BE_flight_origin_date").clear()
driver.find_element_by_id("BE_flight_origin_date").send_keys("28/01/2022")
time.sleep(2)
driver.find_element_by_id("28/01/2022").click()
time.sleep(2)

#driver.find_element_by_id("BE_flight_arrival_date").clear()
driver.find_element_by_id("BE_flight_arrival_date").send_keys("30/01/2022")
time.sleep(2)
driver.find_element_by_id("30/01/2022").click()
time.sleep(2)


driver.find_element_by_id("BE_flight_flsearch_btn").click()



#data-stid="location-field-leg1-origin-menu-trigger"