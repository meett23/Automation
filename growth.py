from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains
import time

driver= webdriver.Chrome (ChromeDriverManager().install())

driver.get("https://login-staging.gwork.io/")
driver.maximize_window()

driver.find_element(By.XPATH, "//button[@id='gdpr-cookie-accept']").click()
time.sleep(1)

driver.find_element(By.XPATH, "//input[@id='identity']").send_keys("ankita@gmail.com")
driver.find_element(By.XPATH, "//input[@id='password']").send_keys("123456")
driver.find_element(By.XPATH, "//button[@type='submit']").click() 

# driver.find_element(By.XPATH, "//span[normalize-space()='My Growth']").click()   
# time.sleep(2)
# driver.find_element(By.XPATH, "//*[@id='heading-322']/div/div[2]").click()   
# time.sleep(2)

# actions=ActionChains(driver)
# time.sleep(2)
# source= driver.find_element(By.XPATH, "//a[@id='title1535']")
# time.sleep(2)
# dest= driver.find_element(By.XPATH, "//*[@id='accordion_learning']")
# time.sleep(2)

# actions=ActionChains(driver)
# time.sleep(1)
# actions.drag_and_drop(source,dest).perform()
# time.sleep(5)

# source= driver.find_element(By.XPATH, "//a[@id='title1535']")
# time.sleep(2)
# dest= driver.find_element(By.XPATH, "//*[@id='accordion_learnt']")
# time.sleep(2)

# actions=ActionChains(driver)
# time.sleep(1)
# actions.drag_and_drop(source,dest).perform()
# time.sleep(10)

    # driver.find_element(By.XPATH, "//a[@href='https://login-staging.gwork.io/insights']").click()
    # time.sleep(1)

    # s=driver.find_element(By.XPATH, "//*[@id='674']")
    # time.sleep(1)
    # d=driver.find_element(By.XPATH, "//*[@id='tag_dragable_proposed_1']/img")
    # time.sleep(1)

    # actions=ActionChains(driver)
    # time.sleep(2)
    # actions.drag_and_drop(s,d).perform()
    # time.sleep(2)

driver.find_element(By.XPATH, "//a[@href='https://login-staging.gwork.io/team']").click()
time.sleep(1)
driver.execute_script("window.scrollTo(0, 200)") 
time.sleep(10)

