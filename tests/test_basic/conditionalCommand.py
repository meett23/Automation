

# Site is not working because they have demo site and there have some changes on sites

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome(executable_path="/Users/tagline_144/Documents/Meet/chromedriver")

driver.get("https://demo.guru99.com/test/newtours/index.php/")

user_ele=driver.find_element_by_name("userName")
print(user_ele.is_displayed())
print(user_ele.is_enabled())

pass_ele=driver.find_element_by_name("password")
print(pass_ele.is_displayed())
print(pass_ele.is_enabled())

user_ele.send_keys("meet")
pass_ele.send_keys("Test@123")

driver.find_element_by_name("submit").click()

roundtrip_radio=driver.find_element_by_css_selector("input[value=roundtrip]")

print("status of roundtrip radio button",roundtrip_radio.is_selected())

onetrip_radio=driver.find_element_by_css_selector("input[value=oneway]")
print("status of oneway radio button",onetrip_radio.is_selected())






