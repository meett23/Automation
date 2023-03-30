# from selenium.webdriver.support.ui import Select
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver import ActionChains
# import time
# from selenium.webdriver.support.ui import Select


# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC



# driver=webdriver.Chrome(ChromeDriverManager().install())
# driver.get("https://login-staging.gwork.io/")

# driver.maximize_window()

# driver.find_element(By.XPATH, "//button[@id='gdpr-cookie-accept']").click()
# time.sleep(1)
# driver.find_element(By.XPATH, "//input[@id='identity']").send_keys("harshvaddoriya21@gmail.com")
# driver.find_element(By.XPATH, "//input[@id='password']").send_keys("123456")
# driver.find_element(By.XPATH, "//button[@type='submit']").click()
# time.sleep(15)

# element=driver.find_element(By.XPATH, '//*[@id="main-body"]/div[1]/nav/div[2]/ul/li[3]')
# drp=Select (element)
# time.sleep(2)

# drp.select_by_visible_text(' Signout ')
# time.sleep(10)

# WebDriverWait(driver, 20).until(EC.element_to_be_clickable(By.XPATH, "//*[@id='main-body']/div[1]/nav/div[2]/ul/li[3]/span")).click()
# time.sleep(10)

# //*[@id="profileDropdown"]/div/img

# //*[@id="main-body"]/div[1]/nav/div[2]/ul/li[3]/div/a[2]/iframe

from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains
import time
from selenium.webdriver.support.ui import Select


from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



driver=webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://login-staging.gwork.io/")

driver.find_element(By.XPATH, "//button[@id='gdpr-cookie-accept']").click()
time.sleep(1)
driver.find_element(By.XPATH, "//input[@id='identity']").send_keys("harshvaddoriya21@gmail.com")
driver.find_element(By.XPATH, "//input[@id='password']").send_keys("123456")
driver.find_element(By.XPATH, "//button[@type='submit']").click()
time.sleep(5)

driver.find_element(By.ID, 'profileDropdown').click()
time.sleep(2)
driver.find_element(By.XPATH, "/html/body/div[1]/nav/div[2]/ul/li[3]/div/a[2]").click()
time.sleep(10)
