from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

driver= webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://demo.automationtesting.in/Windows.html")
time.sleep(5)

driver.find_element(By.XPATH, "//a[@href='http://www.selenium.dev']//button[@class='btn btn-info'][normalize-space()='click']").click()
time.sleep(2)

print(driver.current_window_handle)

handles=driver.window_handles

for handle in handles:
    driver.switch_to.window(handle)
    print(driver.title)

driver.quit()