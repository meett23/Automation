from selenium import webdriver
from selenium.webdriver import ActionChains

driver=webdriver.Chrome(executable_path="/Users/tagline_144/Documents/Meet/chromedriver")

driver.get("http://testautomationpractice.blogspot.com/")

element=driver.find_element_by_xpath("//*[@id='HTML10']/div[1]/button")

actions=ActionChains(driver)

actions.double_click(element).perform()


