from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="/Users/tagline_144/Documents/Meet/chromedriver")

driver.get("http://testautomationpractice.blogspot.com/")

driver.find_element_by_xpath("//*[@id='HTML9']/div[1]/button").click()

time.sleep(2)
driver.switch_to_alert().accept()
#driver.switch_to_alert().dismiss()

