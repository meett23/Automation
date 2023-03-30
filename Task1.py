from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains
import time

driver=webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://login-staging.gwork.io/")

driver.maximize_window()

driver.find_element(By.XPATH, "//button[@id='gdpr-cookie-accept']").click()
time.sleep(1)
driver.find_element(By.XPATH, "//input[@id='identity']").send_keys("harshvaddoriya21@gmail.com")
driver.find_element(By.XPATH, "//input[@id='password']").send_keys("123456")
driver.find_element(By.XPATH, "//button[@type='submit']").click()
time.sleep(2)

driver.find_element(By.XPATH, "//a[@href='https://login-staging.gwork.io/my_growth']").click()
time.sleep(1)

driver.find_element(By.XPATH, "//a[@role='button']").click()
time.sleep(1)

driver.find_element(By.XPATH, "//input[@id='select_user']").click()
time.sleep(1)

driver.find_element(By.XPATH, "//*[@id='learning-nugget']/div/div[1]/div/div/div/div[2]/ul/li[5]/a/div/img").click()
time.sleep(1)

driver.find_element(By.XPATH, "//textarea[@id='title']").send_keys("Nothing")
time.sleep(1)

driver.find_element(By.XPATH, "//*[@id='learning-nugget']/div/div[2]/div[2]/div[2]/div/div/select/option[2]").click()
time.sleep(1)

driver.find_element(By.XPATH, "//textarea[@id='description']").send_keys("Nothing")
time.sleep(1)

driver.find_element(By.XPATH, "//input[@id='assignee']").click()
time.sleep(1)

driver.find_element(By.XPATH, "//*[@id='learning-nugget']/div/div[2]/div[2]/div[4]/div/div/div/div[2]/ul/li[4]/a").click()
time.sleep(1)

driver.find_element(By.XPATH, "//*[@id='learning-nugget']/div/div[2]/div[2]/div[5]/div/div/select/option[3]").click()
time.sleep(1)

driver.find_element(By.XPATH, "//button[@id='btn_submit']").click()
time.sleep(1)

driver.find_element(By.XPATH, "//*[@id='vetting-form']/table/tbody/tr[1]/td[2]/label[1]/input").click()
time.sleep(1)

driver.find_element(By.XPATH, "//*[@id='vetting-form']/table/tbody/tr[2]/td[2]/label[1]/input").click()
time.sleep(1)

driver.find_element(By.XPATH, "//*[@id='vetting-form']/button").click()
time.sleep(7)

driver.find_element(By.XPATH, "//a[@id='profileDropdown']").click()
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div[1]/nav/div[2]/ul/li[3]/div/a[2]").click()
time.sleep(10)
