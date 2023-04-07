from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

driver= webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://sd-topup.bustto.com/")
time.sleep(1)
driver.maximize_window()

# # Scroll to end
# driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")  

# # Select Ludo club
# driver.find_element(By.XPATH, "//*[@id='root']/div/div/div/div[3]/div/div/div[1]/div/div").click()

# # Scroll to top
# driver.execute_script("scroll(0, 0)")  

driver.find_element(By.XPATH, "//*[@id=':r0:']").send_keys("1006074560857")
driver.find_element(By.XPATH, "//*[@id='scrollable-auto-tabpanel-0']/h6/div/div[2]/div[3]/div/div/div[2]/div").click()
driver.find_element(By.XPATH, "//*[@id=':r5:']").send_keys("meet.tagline@gmail.com")
driver.find_element(By.XPATH, "//*[@id='scrollable-auto-tabpanel-0']/h6/div/div[2]/div[5]/div/label[1]/span[1]/input").click()
driver.find_element(By.XPATH, "//*[@id='scrollable-auto-tabpanel-0']/h6/div/div[2]/div[6]/div/div[2]/button").click()
driver.find_element(By.XPATH, "/html/body/div[2]/div[3]/div/div/div[2]/button[2]").click()
time.sleep(2)
driver.find_element(By.XPATH, "//*[@id='keep-mounted-modal-title']/span").click()

# Login
driver.find_element(By.XPATH, "//*[@id='root']/div/header/div/button").click()
driver.find_element(By.XPATH, "//*[@id='email']").send_keys("priteshsuvagiya@gmail.com")
driver.find_element(By.XPATH, "//*[@id='password']").send_keys("Admin@123")
driver.find_element(By.XPATH, "//*[@id='root']/div/div/form/div[2]/button").click()

# move to transaction tab
driver.find_element(By.XPATH, "//*[@id='root']/div/div[1]/ul/div[2]/div[2]/span").click()
time.sleep(2)
driver.find_element(By.XPATH, "//*[@id='search']").send_keys("0736308173811373")
driver.find_element(By.XPATH, "//*[@id='root']/div/div[2]/div[2]/div[1]/table/tbody/tr/th[8]/div/button").click()
# driver.find_element(By.XPATH, "").click()
# driver.find_element(By.XPATH, "").click()
# driver.find_element(By.XPATH, "").click()
# driver.find_element(By.XPATH, "").click()




time.sleep(10)