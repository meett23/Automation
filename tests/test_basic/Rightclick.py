from selenium import webdriver
from selenium.webdriver import ActionChains
import time

driver=webdriver.Chrome(executable_path="/Users/tagline_144/Documents/Meet/chromedriver")

driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")

element=driver.find_element_by_xpath("/html/body/div/section/div/div/div/p/span")

actions=ActionChains(driver)

actions.context_click(element).perform()
driver.find_element_by_xpath("/html/body/ul/li[1]").click()  #after right click choose option for this

time.sleep(2)
driver.switch_to_alert().accept()       #for click on alert box




