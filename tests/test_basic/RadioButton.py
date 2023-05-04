from selenium import webdriver

driver=webdriver.Chrome(executable_path="/Users/tagline_144/Documents/Meet/chromedriver")

driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")

# working with radio button

status=driver.find_element_by_id("RESULT_RadioButton-7_0").is_selected()
print(status)

driver.find_element_by_xpath("//*[@id='q26']/table/tbody/tr[1]/td/label").click()

status=driver.find_element_by_id("RESULT_RadioButton-7_0").is_selected()
print(status)