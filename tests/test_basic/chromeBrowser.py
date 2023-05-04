from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome(executable_path="/Users/tagline_144/Documents/Meet/chromedriver")

driver.get("https://www.yatra.com/")

driver.find_element_by_xpath("//*[@id='BE_flight_flsearch_btn']").click()

driver.find_element_by_xpath("//*[@id='DELBOMG8334SA20220122_G8API']/div/div[2]/div[4]/div/div[2]/button").click()

driver.find_element_by_xpath("//*[@id='fare-DELBOMG8334SA20220122_G8API']/div[2]/button").click()

time.sleep(15)




