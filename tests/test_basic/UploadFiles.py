from selenium import webdriver

driver = webdriver.Chrome(executable_path="/Users/tagline_144/Documents/Meet/chromedriver")

driver.get("https://www.filemail.com/share/upload-file")

driver.find_element_by_xpath("//*[@id='addBtn']/span").send_keys("/Users/tagline_144/Downloads/Somnath.jpeg")