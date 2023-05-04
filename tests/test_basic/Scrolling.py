from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path="/Users/tagline_144/Documents/Meet/chromedriver")

driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")

driver.execute_script("window.scrollBy(0,2000)"," ") #scroll by pixel

#scroll, till the element will find
    #flag=driver.find_element_by_xpath("//*[@id='content']/div[2]/div[2]/table[1]/tbody/tr[86]/td[1]/img")

    #driver.execute_script("arguments[0].scrollIntoView();",flag)

#scroll till the end
    #driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")


