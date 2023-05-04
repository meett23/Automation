from selenium import webdriver
from selenium.webdriver import ActionChains

driver=webdriver.Chrome(executable_path="/Users/tagline_144/Documents/Meet/chromedriver")

driver.get("http://demo.automationtesting.in/Static.html")

source=driver.find_element_by_xpath("//*[@id='mongo']")
destination=driver.find_element_by_xpath("//*[@id='droparea']")

actions=ActionChains(driver)

actions.drag_and_drop(source,destination).perform()

