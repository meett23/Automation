from gettext import install
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://login-staging.gwork.io/")
driver.maximize_window()

driver.find_element(By.XPATH, "//button[@id='gdpr-cookie-accept']").click()
time.sleep(1)

driver.find_element(By.XPATH, "//input[@id='identity']").send_keys("ankita@gmail.com")
driver.find_element(By.XPATH, "//input[@id='password']").send_keys("123456")
driver.find_element(By.XPATH, "//button[@type='submit']").click()  

# driver.find_element(By.XPATH, "//*[@id='base_line']").click()
# time.sleep(2)
# driver.find_element(By.XPATH, "//*[@id='baseline_modal']/div/div/div[1]/button").click()
# time.sleep(2)
driver.find_element(By.XPATH, "//*[@id='pills-first-tab']").click()    #daily action par click
time.sleep(2)
# driver.find_element(By.XPATH, "//*[@id='pills-first']/div/div[1]/div[2]/div/div/div[1]/div[2]/div/a").click()   #click on applause
# time.sleep(2)
# driver.find_element(By.XPATH, "//*[@id='circle313']/div/canvas").click()  # user select
# time.sleep(2)
# driver.find_element(By.XPATH, "//*[@id='25']").click()  #select applause
# time.sleep(2)
# driver.find_element(By.XPATH, "//*[@id='give_applause_body']/div/div[2]/div/div/button").click()  #click on give applause
# time.sleep(15)

driver.find_element(By.CLASS_NAME, "task-area").click()  #For drag & drop
time.sleep(2)
driver.find_element(By.CLASS_NAME, "task-area").send_keys('Mobileteam')   #For drag & drop
time.sleep(2)

actions=ActionChains(driver)
time.sleep(2)
source=driver.find_element(By.XPATH, "//*[@id='sortable1']/div[1]/div/div[4]")
time.sleep(2)
destination=driver.find_element(By.XPATH, "//*[@id='sortable2']/div/div/div[5]")

actions.drag_and_drop(source,destination).perform()
time.sleep(5)

driver.find_element(By.XPATH, "//div[@class='d-flex w-100']//div[@class='box-right-icon']//img").click()      #click on side menu
time.sleep(2)
driver.find_element(By.XPATH, "//div[@class='dropdown-menu show']//a[@class='dropdown-item bg-orange'][normalize-space()='Working on it']").click()    #click on working on it
time.sleep(10)
driver.find_element(By.XPATH, "//button[normalize-space()='Save & Share']").click()   # click on save button
time.sleep(2)

# driver.find_element(By.XPATH, "//div[@id='19567']//i[@class='far fa-comment chat-box-open']")  # click on comment
# time.sleep(5)
# driver.find_element(By.XPATH, "//div[@placeholder='Write a comment']").send_keys("For Testing purpose")   #write in text box
# time.sleep(2)
# driver.find_element(By.XPATH, "//button[normalize-space()='Send']").click()   #click on send button
# time.sleep(2)

driver.find_element(By.XPATH, "//*[@id='sidebar']/ul/li[2]/a").click()   #click on My action
time.sleep(2)

driver.find_element(By.XPATH, "//*[@id='pills-second']/div/div[2]/div[1]/div/div/div[2]/div[2]/p/button").click()  #click on learning skill
time.sleep(2)
driver.find_element(By.XPATH, "//*[@id='assessment_schedule_modal']/div/div/div[1]/button").click()   # click on close button
time.sleep(2)

driver.find_element(By.XPATH, "//*[@id='select2-graph_type-container']").click()  # mouse over baki 6
time.sleep(2)
# over = driver.find_element(By.XPATH, '//*[@id="graph_type"]/option[2]').click()
driver.find_element(By.XPATH, '//*[@id="graph_type"]/option[2]').click()
time.sleep(2)

driver.execute_script("window.scrollTo(0,300)")
time.sleep(5)

driver.find_element(By.XPATH, "//*[@id='pills-second']/div/div[2]/div[2]/div/div[3]/div[2]/a").click()   # click on vciew assesmnet
time.sleep(2)
driver.find_element(By.XPATH, "//*[@id='sidebar']/ul/li[2]/a").click()  # click on my action
time.sleep(5)

driver.find_element(By.XPATH, "//*[@id='sidebar']/ul/li[3]/a").click()  # click on my perfomance
time.sleep(10)

driver.find_element(By.XPATH, "//*[@id='main-body']/div[1]/div/div/div/div[1]/div/div/div[1]/div/div/div[2]/div/div/div/div/div/div/div/div/div[2]/div/div/div[1]/div/div[1]/div/div/a").click()
time.sleep(3)    #click on slider 
driver.find_element(By.XPATH, "//*[@id='overview1']/div/div[1]/a").click()
time.sleep(3)    #close slider
driver.find_element(By.XPATH, "//*[@id='main-body']/div[1]/div/div/div/div[1]/div/div/div[1]/div/div/div[2]/div/div/div/div/div/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/a").click()
time.sleep(3)    #click on slider
driver.find_element(By.XPATH, "//*[@id='overview2']/div/div[1]/a").click()
time.sleep(3)    #close slider

driver.execute_script("window.scrollTo(0,300)")
time.sleep(3)

driver.find_element(By.XPATH, "//*[@id='performance_tab']/div[1]/div/div[3]/a").click()  #click on create perfomance objective
time.sleep(3)

driver.find_element(By.XPATH, "//*[@id='performance_from']/div/div[2]/div[1]/div[1]/div/div/div/select").click()    #click on option menu
time.sleep(2)
driver.find_element(By.XPATH, "//*[@id='performance_from']/div/div[2]/div[1]/div[1]/div/div/div/select/option[2]").click()     #click on option
time.sleep(2)
driver.find_element(By.XPATH, "//*[@id='performance_from']/div/div[2]/div[1]/div[2]/div/div/div[1]/select").click()    #click on select day option menu
time.sleep(2)
driver.find_element(By.XPATH, "//*[@id='performance_from']/div/div[2]/div[1]/div[2]/div/div/div[1]/select/option[4]").click()    #click on option
time.sleep(2)
driver.find_element(By.XPATH, "//*[@id='performance_from']/div/div[2]/div[1]/div[2]/div/div/div[2]/select").click()     #click on select day option menu
time.sleep(2)
driver.find_element(By.XPATH, "//*[@id='performance_from']/div/div[2]/div[1]/div[2]/div/div/div[2]/select/option[8]").click()    #click on option
time.sleep(2)
driver.find_element(By.XPATH, "//*[@id='performance_from']/div/div[2]/div[1]/div[3]/div/div/div/input").click()    #click on date
time.sleep(2)
driver.find_element(By.XPATH, "//*[@id='main-body']/div[6]/div[1]/table/tbody/tr[5]/td[1]").click()    #select date
time.sleep(2)
driver.find_element(By.XPATH, "//*[@id='performance_from']/div/div[3]/button[2]").click()    #click on Next button
time.sleep(5)

driver.find_element(By.XPATH, "//*[@id='performance_from']/div/div[2]/div[2]/div[1]/div/div[1]/div/div/div[1]/input").send_keys("Add Home theater in OFFICE")  #click on Name the performance objective
time.sleep(2)
driver.find_element(By.XPATH, "//*[@id='performance_from']/div/div[2]/div[2]/div[1]/div/div[1]/div/div/div[2]/input").send_keys("100")  # click on Weight
time.sleep(2)
driver.find_element(By.XPATH, "//*[@id='performance_from']/div/div[2]/div[2]/div[1]/div/div[2]/div/div/div/textarea").send_keys("Test")  # click on discription
time.sleep(2)
driver.find_element(By.XPATH, "//*[@id='performance_from']/div/div[2]/div[2]/div[1]/div/div[2]/div/div/div/input").send_keys("Test")
time.sleep(2) 

driver.find_element(By.XPATH, "//*[@id='performance_from']/div/div[2]/div[2]/div[1]/div/div[3]/div/div/div/div/div/div/div[1]/input").send_keys("Add Home Theater")
time.sleep(2) 
driver.find_element(By.XPATH, "//*[@id='performance_from']/div/div[2]/div[2]/div[1]/div/div[3]/div/div/div/div/div/div/div[2]/input").send_keys("100")
time.sleep(2) 
driver.find_element(By.XPATH, "//*[@id='performance_from']/div/div[2]/div[2]/div[1]/div/div[5]/div/div/div/input").send_keys("www.google.com")
time.sleep(2) 
driver.find_element(By.XPATH, "//*[@id='performance_from']/div/div[3]/button[2]").click()   #Click on Next buton
time.sleep(5) 
driver.find_element(By.XPATH, "//*[@id='performance_from']/button[2]").click()   #click on confirm button
time.sleep(5)

driver.find_element(By.XPATH, "//a[@href='https://login-staging.gwork.io/user/my_learning']").click()   # click on my growth
time.sleep(3)
actions=ActionChains(driver)
time.sleep(2)
a=driver.find_element(By.XPATH, "//a[@id='title1147']")     #drag growth
b=driver.find_element(By.XPATH, "//div[@id='accordion_learnt']")     #drop growth
time.sleep(3)
actions.drag_and_drop(a,b).perform()
time.sleep(7)

driver.find_element(By.XPATH, "//a[@role='button']").click()    # click on Give growth nugget
time.sleep(2)
driver.find_element(By.XPATH, "//textarea[@id='title']").click()
time.sleep(2)