from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains
import time

driver=webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://login-staging.gwork.io/")

driver.implicitly_wait(10)

driver.maximize_window()

driver.find_element(By.XPATH, "//button[@id='gdpr-cookie-accept']").click()

driver.find_element(By.XPATH, "//input[@id='identity']").send_keys("harshvaddoriya21@gmail.com")
driver.find_element(By.XPATH, "//input[@id='password']").send_keys("123456")
driver.find_element(By.XPATH, "//button[@type='submit']").click()

driver.find_element(By.XPATH, "//button[normalize-space()='Edit']").click()

driver.find_element(By.XPATH, "//*[@id='sortable1']/div[1]/div/div[2]/textarea").send_keys("Need AC")

s=driver.find_element(By.XPATH, "//*[@id='sortable1']/div[1]/div/div[4]")
d=driver.find_element(By.XPATH, "//*[@id='sortable2']")

actions=ActionChains(driver)

actions.drag_and_drop(s,d).perform()
time.sleep(3)

driver.find_element(By.XPATH, "//button[normalize-space()='Save & Share']").click()
time.sleep(2)

driver.find_element(By.XPATH, "//button[normalize-space()='Edit']").click()
time.sleep(2)

driver.find_element(By.XPATH, '//*[@id="sortable2"]/div/div/div[5]').click()
time.sleep(2)

driver.find_element(By.XPATH, '//*[@id="sortable2"]/div/div/div[5]/div/div[2]/a[4]').click()
time.sleep(2)

driver.find_element(By.XPATH, "//button[normalize-space()='Save & Share']").click()
time.sleep(10)