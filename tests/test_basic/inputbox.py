from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver=webdriver.Chrome(executable_path="/Users/tagline_144/Documents/Meet/chromedriver")

driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")

ss=driver.find_element(By.ID,'RESULT_TextField-1').is_displayed()
print("Displayed", ss)
ss=driver.find_element(By.ID,'RESULT_TextField-1').is_enabled()
print("enabled", ss)



#how to find how many inputboxes in web page

inputboxes=driver.find_elements(By.CLASS_NAME, 'text_field')
print(len(inputboxes))

driver.find_element(By.ID,'RESULT_TextField-1').send_keys("Meet")
driver.find_element(By.ID,'RESULT_TextField-2').send_keys("Thakkar")

driver.find_element_by_id("RESULT_TextField-3").send_keys("9090909090")

driver.find_element(By.ID,'RESULT_TextField-4').send_keys("India")

driver.find_element(By.ID,'RESULT_TextField-5').send_keys("Surat")

driver.find_element(By.ID,'RESULT_TextField-6').send_keys("meet")

# working with radio button

status=driver.find_element_by_id("RESULT_RadioButton-7_0").is_selected()
print(status)

driver.find_element_by_xpath("//*[@id='q26']/table/tbody/tr[1]/td/label").click()

status=driver.find_element_by_id("RESULT_RadioButton-7_0").is_selected()
print(status)

#working with checkboxes

driver.find_element_by_xpath("//*[@id='q15']/table/tbody/tr[1]/td/label").click()
driver.find_element_by_xpath("//*[@id='q15']/table/tbody/tr[2]/td/label").click()

# working with drop-down

drp=Select(driver.find_element_by_id("RESULT_RadioButton-9"))
drp.select_by_visible_text('Morning')

#count no of options
print(len(drp.options))

#print all the options
all_options=drp.options

for option in all_options:
    print(option.text)















