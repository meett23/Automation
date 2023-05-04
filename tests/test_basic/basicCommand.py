from selenium import webdriver
from selenium.webdriver.common.keys import Keys



driver=webdriver.Chrome(executable_path="/Users/tagline_144/Documents/Meet/chromedriver")

driver.get("http://demo.automationtesting.in/Windows.html")

print (driver.title)

driver.find_element_by_xpath("//*[@id='Tabbed']/a/button").click()

