from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://ravina.myglobal.app/login")

driver.implicitly_wait(10)

driver.find_element(By.XPATH, "//input[@placeholder='Email']").send_keys("ravina.tagline@gmail.com")
driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("Test@123")
driver.find_element(By.XPATH, "//button[@type='button']").click()
time.sleep(5)

driver.find_element(By.XPATH, "//*[@id='root']/div/div[2]/div[1]/header/nav/div[1]/a/img").click()
time.sleep(4)

driver.find_element(By.XPATH, "//label[@for='currency_options_6']").click()
time.sleep(1)
driver.find_element(By.XPATH, "//li[contains(text(),'40')]").click()
time.sleep(1)

driver.find_element(By.XPATH, "//input[@name='to']").send_keys("Meet")
time.sleep(1)

driver.find_element(By.XPATH, "//input[@name='from']").send_keys("Ravina")
time.sleep(1)

driver.find_element(By.XPATH, "//input[@name='email']").send_keys("ravina.tagline@gmail.com")
time.sleep(1)

driver.find_element(By.XPATH, "//button[@class='btn-block btn btn-default']").click()
time.sleep(1)

driver.find_element(By.XPATH, "//button[normalize-space()='Proceed to Checkout']").click()
time.sleep(1)

driver.find_element(By.XPATH, "//*[@id='root']/div/div[2]/div[3]/div/form/div[1]/input").send_keys('Meet')
time.sleep(1)

# WebDriverWait(driver, 20).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,"iframe_xpath")))
# # driver.switchTo().frame(driver.findElement(By.xpath("//iframe"))).send_keys("4000000000003220")
# WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='root']/form/span[2]/div/div[2]/input"))).click()
# time.sleep(3)
# WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='root']/form/span[2]/div/div[2]/input"))).send_keys("4000000000003220")
# time.sleep(3)

# driver.find_element(By.XPATH, "//input[@placeholder='Card number']").click()
# time.sleep(3)
driver.find_element(By.XPATH, "//*[@id='root']/div/div[2]/div[3]/div/form/div[2]/div/div/iframe").send_keys('4000000000003220')
time.sleep(2)

driver.find_element(By.XPATH, "//*[@id='root']/div/div[2]/div[3]/div/form/div[3]/div[1]/div/iframe").send_keys('00000126')
time.sleep(3)

# driver.find_element(By.XPATH, "//*[@id='root']/form/span[2]/span/input").send_keys('123')
driver.find_element(By.XPATH, "//*[@id='root']/div/div[2]/div[3]/div/form/div[3]/div[2]/div/iframe").send_keys('00000100')
time.sleep(3)

driver.find_element(By.XPATH, "//button[@type='submit']").click()
time.sleep(2)

driver.find_element(By.XPATH, "//*[@id='challengeFrame']").click()
time.sleep(2)

driver.find_element(By.XPATH, "//button[normalize-space()='OK']").click()
time.sleep(2)




