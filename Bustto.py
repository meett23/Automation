from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

driver= webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://app-dev.bustto.com/")
time.sleep(1)

driver.execute_script("window.scrollBy(0,500)", " ")

driver.find_element(By.XPATH, "//*[@id='popular-0']/div/div[1]/div[2]/div/div").click()
driver.find_element(By.ID, "playerId").send_keys("100285765104")
driver.find_element(By.XPATH, "//*[@id='root']/div/div/div[1]/div/div/div[3]/div/div[5]/div/div[1]/label[1]/span[1]/input").click()
driver.find_element(By.XPATH, "//*[@id='email']").send_keys("meet.tagline@gmail.com")
driver.find_element(By.XPATH, "//*[@id='root']/div/div/div[1]/div/div/div[3]/div/div[6]/div/div[2]/button").click()
driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div/div/div[2]/button[2]").click()
time.sleep(3)
# driver.find_element(By.CLASS_NAME, "MuiSvgIcon-root MuiSvgIcon-fontSizeMedium css-vubbuv").click()

time.sleep(10)

