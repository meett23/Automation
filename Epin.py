from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

driver= webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://sd-epin.bustto.com/")
time.sleep(2)

driver.find_element(By.XPATH, "//*[@id='scrollable-auto-tabpanel-1']/h6/div/div[2]/div[1]/div/div/div[1]/button[2]").click()
driver.find_element(By.XPATH, "//*[@id='scrollable-auto-tabpanel-1']/h6/div/div[2]/div[2]/div/div/button[2]").click()
driver.find_element(By.XPATH, "//*[@id=':rb:']").send_keys("Meet")
driver.find_element(By.XPATH, "//*[@id=':rc:']").send_keys("PRITESH")
driver.find_element(By.XPATH, "//*[@id=':rd:']").send_keys("meet.tagline@gmail.com")
driver.find_element(By.XPATH, "//*[@id=':re:']").send_keys("9106612343")
driver.find_element(By.CSS_SELECTOR, "#scrollable-auto-tabpanel-1 > h6 > div > div.MuiGrid-root.MuiGrid-item.MuiGrid-grid-md-7.css-1odkrke > div:nth-child(4) > div > div:nth-child(4) > div > div > svg").click()


element= driver.find_element(By.XPATH, "//*[@id='scrollable-auto-tabpanel-1']/h6/div/div[2]/div[6]/div/div[2]")
# driver.execute_script("arguments[0].scrollIntoView();", element)                    # scroll till 'buy now' button is not find /
driver.execute_script("window.scrollBy(0,1000)", " ")                       # scroll till 1000 pixel /

driver.find_element(By.XPATH, "//*[@id='scrollable-auto-tabpanel-1']/h6/div/div[2]/div[6]/div/div[2]").click()
time.sleep(2)
driver.find_element(By.XPATH, "/html/body/div[2]/div[3]/div/div/div[2]/button[2]").click()





# driver.find_element(By.XPATH, "").click()
# driver.find_element(By.XPATH, "").click()








# driver.find_element(By.XPATH, "").click()
time.sleep(10)