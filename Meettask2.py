from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
import time

driver= webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")

element= driver.find_element(By.ID, "RESULT_RadioButton-9")
drp= Select(element)

# count of drop-down
print(len(drp.options))

# Display the all option which is available in the page
all_options=drp.options

for option in all_options:
    print(option.text)