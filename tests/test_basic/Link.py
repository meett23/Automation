from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(executable_path="/Users/tagline_144/Documents/Meet/chromedriver")

driver.get("https://www.yatra.com/")

links = driver.find_elements(By.TAG_NAME, "a")
print(len(links))

for link in links:
    print(link.text)

driver.find_element(By.LINK_TEXT,"Offers").click()

#driver.find_element(By.PARTIAL_LINK_TEXT,"off").click()