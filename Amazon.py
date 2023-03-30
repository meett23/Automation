import imp
from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

driver= webdriver.Chrome(ChromeDriverManager().install())
# driver.get("https://www.amazon.in/")

# driver.implicitly_wait(10)
# driver.maximize_window()

# time.sleep(5)

# driver.find_element(By.XPATH, "//*[@id='twotabsearchtextbox']").click()
# driver.find_element(By.XPATH, "//*[@id='twotabsearchtextbox']").send_keys("Kurta for men")
# driver.find_element(By.XPATH, "//*[@id='nav-search-submit-button']").click()

# driver.execute_script("window.scrollTo(0,700)")

# driver.find_element(By.XPATH, "//*[@id='search']/div[1]/div[1]/div/span[3]/div[2]/div[5]/div/div/div/div/div[2]/div[2]/h2/a").click()
# time.sleep(60)



# Navigate to the Amazon website
driver.get('https://www.amazon.com')

# Search for T-shirts
search_bar = driver.find_element_by_id('twotabsearchtextbox')
search_bar.send_keys('T-shirt')
search_button = driver.find_element_by_xpath('//input[@value="Go"]')
search_button.click()

# Select a T-shirt
tshirt = driver.find_element_by_xpath('//div[@class="s-result-item"]/div/h2/a')
tshirt.click()

# Add the T-shirt to your cart
add_to_cart = driver.find_element_by_id('add-to-cart-button')
add_to_cart.click()

# Proceed to checkout
proceed_to_checkout = driver.find_element_by_id('hlb-ptc-btn-native')
proceed_to_checkout.click()

# Sign in (if necessary)
# Enter shipping and payment information
# Complete the purchase

# Quit the web browser
driver.quit()