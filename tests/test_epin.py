import pdb
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time


class TestCaseForEPIN(unittest.TestCase):
    def test_Buy_EPIN(self):
        self.driver= webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("https://sd-epin.bustto.com/")
        self.driver.maximize_window()
        time.sleep(2)

        self.driver.find_element(By.XPATH, "//*[@id='scrollable-auto-tabpanel-1']/h6/div/div[2]/div[1]/div/div/div[1]/button[2]").click()
        self.driver.find_element(By.XPATH, "//*[@id='scrollable-auto-tabpanel-1']/h6/div/div[2]/div[2]/div/div/button[2]").click()
        self.driver.find_element(By.XPATH, "//*[@id=':rb:']").send_keys("Meet")
        self.driver.find_element(By.XPATH, "//*[@id=':rc:']").send_keys("PRITESH")
        self.driver.find_element(By.XPATH, "//*[@id=':rd:']").send_keys("meet.tagline@gmail.com")
        self.driver.find_element(By.XPATH, "//*[@id=':re:']").send_keys("9106612343")
        self.driver.find_element(By.CSS_SELECTOR, "#scrollable-auto-tabpanel-1 > h6 > div > div.MuiGrid-root.MuiGrid-item.MuiGrid-grid-md-7.css-1odkrke > div:nth-child(4) > div > div:nth-child(4) > div > div > svg").click()

        element= self.driver.find_element(By.XPATH, "//*[@id='scrollable-auto-tabpanel-1']/h6/div/div[2]/div[6]/div/div[2]")
        # driver.execute_script("arguments[0].scrollIntoView();", element)                    # scroll till 'buy now' button is not find /
        self.driver.execute_script("window.scrollBy(0,1000)", " ")                       # scroll till 1000 pixel /

        self.driver.find_element(By.XPATH, "//*[@id='scrollable-auto-tabpanel-1']/h6/div/div[2]/div[6]/div/div[2]").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "/html/body/div[2]/div[3]/div/div/div[2]/button[2]").click()
        time.sleep(1)

        self.driver.close()


    def test_Buy_epin_with_enter_amount_above_100000(self):
        self.driver= webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("https://sd-epin.bustto.com/")
        self.driver.maximize_window()
        time.sleep(2)

        # self.driver.find_element(By.XPATH, "//*[@id='scrollable-auto-tabpanel-1']/h6/div/div[2]/div[1]/div/div/div[1]/button[2]").click()
        self.driver.find_element(By.XPATH, "//*[@id=':ra:']").send_keys("1000000")
        denomination=self.driver.find_element(By.XPATH, "//*[@id=':ra:']").get_attribute("value")

        if int(denomination) > 10000:
            print("***********************************")
            print("Please set denomination within Min. 10 INR , Max. 10000 INR")
            print("***********************************")

            return
        else:
            self.driver.find_element(By.XPATH, "//*[@id='scrollable-auto-tabpanel-1']/h6/div/div[2]/div[2]/div/div/button[2]").click()
            self.driver.find_element(By.XPATH, "//*[@id=':rb:']").send_keys("Meet")
            self.driver.find_element(By.XPATH, "//*[@id=':rc:']").send_keys("PRITESH")
            self.driver.find_element(By.XPATH, "//*[@id=':rd:']").send_keys("meet.tagline@gmail.com")
            self.driver.find_element(By.XPATH, "//*[@id=':re:']").send_keys("9106612343")
            self.driver.find_element(By.CSS_SELECTOR, "#scrollable-auto-tabpanel-1 > h6 > div > div.MuiGrid-root.MuiGrid-item.MuiGrid-grid-md-7.css-1odkrke > div:nth-child(4) > div > div:nth-child(4) > div > div > svg").click()

            element= self.driver.find_element(By.XPATH, "//*[@id='scrollable-auto-tabpanel-1']/h6/div/div[2]/div[6]/div/div[2]")
            # driver.execute_script("arguments[0].scrollIntoView();", element)                    # scroll till 'buy now' button is not find /
            self.driver.execute_script("window.scrollBy(0,1000)", " ")                       # scroll till 1000 pixel /
            time.sleep(3)

            self.driver.find_element(By.XPATH, "//*[@id='scrollable-auto-tabpanel-1']/h6/div/div[2]/div[6]/div/div[2]").click()
            time.sleep(2)
            self.driver.find_element(By.XPATH, "/html/body/div[2]/div[3]/div/div/div[2]/button[2]").click()
            time.sleep(2)

            self.driver.close()


    def test_buy_epin_sender_details_name(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("https://sd-epin.bustto.com/")
        self.driver.maximize_window()
        time.sleep(2)

        self.driver.find_element(
            By.XPATH,
            "//*[@id='scrollable-auto-tabpanel-1']/h6/div/div[2]/div[1]/div/div/div[1]/button[2]",
        ).click()
        self.driver.find_element(
            By.XPATH,
            "//*[@id='scrollable-auto-tabpanel-1']/h6/div/div[2]/div[2]/div/div/button[2]",
        ).click()

        # NAME FIELD IS BLANK OR # Fill in recipient information
        self.driver.find_element(By.XPATH, "//*[@id=':rb:']").send_keys("  ")

        self.driver.find_element(By.XPATH, "//*[@id=':rc:']").send_keys("PRITESH")
        self.driver.find_element(By.XPATH, "//*[@id=':rd:']").send_keys(
            "meet.tagline@gmail.com"
        )
        self.driver.find_element(By.XPATH, "//*[@id=':re:']").send_keys(
            "9106612343"
        )
        self.driver.find_element(
            By.CSS_SELECTOR,
            "#scrollable-auto-tabpanel-1 > h6 > div > div.MuiGrid-root.MuiGrid-item.MuiGrid-grid-md-7.css-1odkrke > div:nth-child(4) > div > div:nth-child(4) > div > div > svg",
        ).click()

        element = self.driver.find_element(
            By.XPATH,
            "//*[@id='scrollable-auto-tabpanel-1']/h6/div/div[2]/div[6]/div/div[2]",
        )
        # driver.execute_script("arguments[0].scrollIntoView();", element)                    # scroll till 'buy now' button is not find /
        self.driver.execute_script(
            "window.scrollBy(0,1000)", " "
        )  # scroll till 1000 pixel /
        time.sleep(3)

        self.driver.find_element(
            By.XPATH,
            "//*[@id='scrollable-auto-tabpanel-1']/h6/div/div[2]/div[6]/div/div[2]",
        ).click()
        time.sleep(2)

        button= self.driver.find_element(By.XPATH, "//*[@id='scrollable-auto-tabpanel-1']/h6/div/div[2]/div[6]/div/div[2]/button")
        
        if button.is_enabled():
            # Run the part when button is enabled
            button.click()
        else:
            # Run this part if button is disabled
            self.driver.close()

        
        
    def test_buy_epin_sender_details_receive_name(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("https://sd-epin.bustto.com/")
        self.driver.maximize_window()
        time.sleep(2)

        self.driver.find_element(
            By.XPATH,
            "//*[@id='scrollable-auto-tabpanel-1']/h6/div/div[2]/div[1]/div/div/div[1]/button[2]",
        ).click()
        self.driver.find_element(
            By.XPATH,
            "//*[@id='scrollable-auto-tabpanel-1']/h6/div/div[2]/div[2]/div/div/button[2]",
        ).click()

        
        self.driver.find_element(By.XPATH, "//*[@id=':rb:']").send_keys("")

        # RECEIVE NAME FIELD IS BLANK OR # Fill in recipient information
        self.driver.find_element(By.XPATH, "//*[@id=':rc:']").send_keys("")
        self.driver.find_element(By.XPATH, "//*[@id=':rd:']").send_keys(
            "meet.tagline@gmail.com"
        )
        self.driver.find_element(By.XPATH, "//*[@id=':re:']").send_keys(
            "9106612343"
        )
        self.driver.find_element(
            By.CSS_SELECTOR,
            "#scrollable-auto-tabpanel-1 > h6 > div > div.MuiGrid-root.MuiGrid-item.MuiGrid-grid-md-7.css-1odkrke > div:nth-child(4) > div > div:nth-child(4) > div > div > svg",
        ).click()

        element = self.driver.find_element(
            By.XPATH,
            "//*[@id='scrollable-auto-tabpanel-1']/h6/div/div[2]/div[6]/div/div[2]",
        )
        # driver.execute_script("arguments[0].scrollIntoView();", element)                    # scroll till 'buy now' button is not find /
        self.driver.execute_script(
            "window.scrollBy(0,1000)", " "
        )  # scroll till 1000 pixel /
        time.sleep(2)

        self.driver.find_element(
            By.XPATH,
            "//*[@id='scrollable-auto-tabpanel-1']/h6/div/div[2]/div[6]/div/div[2]",
        ).click()
        time.sleep(1)

        button = self.driver.find_element(By.XPATH, '//*[@id="scrollable-auto-tabpanel-1"]/h6/div/div[2]/div[6]/div/div[2]/button')
        
        if button.is_enabled():
            # Run the part when button is enabled
            button.click()
        else:
            # Run this part if button is disabled
            self.driver.close()


    def test_buy_epin_sender_details_email_address(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("https://sd-epin.bustto.com/")
        self.driver.maximize_window()
        time.sleep(2)

        self.driver.find_element(
            By.XPATH,
            "//*[@id='scrollable-auto-tabpanel-1']/h6/div/div[2]/div[1]/div/div/div[1]/button[2]",
        ).click()
        self.driver.find_element(
            By.XPATH,
            "//*[@id='scrollable-auto-tabpanel-1']/h6/div/div[2]/div[2]/div/div/button[2]",
        ).click()

        
        self.driver.find_element(By.XPATH, "//*[@id=':rb:']").send_keys("")

        # RECEIVE NAME FIELD IS BLANK OR # Fill in recipient information
        self.driver.find_element(By.XPATH, "//*[@id=':rc:']").send_keys("")
        self.driver.find_element(By.XPATH, "//*[@id=':rd:']").send_keys(
            ""
        )
        self.driver.find_element(By.XPATH, "//*[@id=':re:']").send_keys(
            "9106612343"
        )
        self.driver.find_element(
            By.CSS_SELECTOR,
            "#scrollable-auto-tabpanel-1 > h6 > div > div.MuiGrid-root.MuiGrid-item.MuiGrid-grid-md-7.css-1odkrke > div:nth-child(4) > div > div:nth-child(4) > div > div > svg",
        ).click()

        element = self.driver.find_element(
            By.XPATH,
            "//*[@id='scrollable-auto-tabpanel-1']/h6/div/div[2]/div[6]/div/div[2]",
        )
        # driver.execute_script("arguments[0].scrollIntoView();", element)                    # scroll till 'buy now' button is not find /
        self.driver.execute_script(
            "window.scrollBy(0,1000)", " "
        )  # scroll till 1000 pixel /
        time.sleep(2)

        self.driver.find_element(
            By.XPATH,
            "//*[@id='scrollable-auto-tabpanel-1']/h6/div/div[2]/div[6]/div/div[2]",
        ).click()
        time.sleep(1)

        button = self.driver.find_element(By.XPATH, '//*[@id="scrollable-auto-tabpanel-1"]/h6/div/div[2]/div[6]/div/div[2]/button')
        
        if button.is_enabled():
            # Run the part when button is enabled
            button.click()
        else:
            # Run this part if button is disabled
            self.driver.close()

    def test_buy_epin_sender_details_phone_number(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("https://sd-epin.bustto.com/")
        self.driver.maximize_window()
        time.sleep(2)

        self.driver.find_element(
            By.XPATH,
            "//*[@id='scrollable-auto-tabpanel-1']/h6/div/div[2]/div[1]/div/div/div[1]/button[2]",
        ).click()
        self.driver.find_element(
            By.XPATH,
            "//*[@id='scrollable-auto-tabpanel-1']/h6/div/div[2]/div[2]/div/div/button[2]",
        ).click()

        
        self.driver.find_element(By.XPATH, "//*[@id=':rb:']").send_keys("")

        # RECEIVE NAME FIELD IS BLANK OR # Fill in recipient information
        self.driver.find_element(By.XPATH, "//*[@id=':rc:']").send_keys("")
        self.driver.find_element(By.XPATH, "//*[@id=':rd:']").send_keys("")
        
        self.driver.find_element(By.XPATH, "//*[@id=':re:']").send_keys("")

# This is not required in web. It's optional.
        self.driver.find_element(
            By.CSS_SELECTOR,
            "#scrollable-auto-tabpanel-1 > h6 > div > div.MuiGrid-root.MuiGrid-item.MuiGrid-grid-md-7.css-1odkrke > div:nth-child(4) > div > div:nth-child(4) > div > div > svg",
        ).click()      

        element = self.driver.find_element(
            By.XPATH,
            "//*[@id='scrollable-auto-tabpanel-1']/h6/div/div[2]/div[6]/div/div[2]",
        )
    
# scroll till 'buy now' button is not find /
        self.driver.execute_script(
            "window.scrollBy(0,1000)", " "
        )  # scroll till 1000 pixel /
        time.sleep(2)

        self.driver.find_element(
            By.XPATH,
            "//*[@id='scrollable-auto-tabpanel-1']/h6/div/div[2]/div[6]/div/div[2]",
        ).click()
        time.sleep(1)

        button = self.driver.find_element(By.XPATH, '//*[@id="scrollable-auto-tabpanel-1"]/h6/div/div[2]/div[6]/div/div[2]/button')
        
        if button.is_enabled():
            # Run the part when button is enabled
            button.click()
        else:
            # Run this part if button is disabled
            self.driver.close()



#  Epin with buying for self



    def test_buy_epin_buying_for_self_data(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("https://sd-epin.bustto.com/")
        self.driver.maximize_window()
        time.sleep(1)

        self.driver.find_element(
            By.XPATH,
            "//*[@id='scrollable-auto-tabpanel-1']/h6/div/div[2]/div[1]/div/div/div[1]/button[2]",
        ).click()
        self.driver.find_element(
            By.XPATH,
            "//*[@id='scrollable-auto-tabpanel-1']/h6/div/div[2]/div[2]/div/div/button[2]",
        ).click()

        # Select to Buying for self
        self.driver.find_element(By.XPATH, "//*[@id='scrollable-auto-tabpanel-1']/h6/div/div[2]/div[3]/div/button[2]").click()

        # buying for self in all FIELD IS BLANK OR # Fill information in buying for self
        self.driver.find_element(By.XPATH, "//*[@id=':rb:']").send_keys("")     # enter name
        self.driver.find_element(By.XPATH, "//*[@id=':rc:']").send_keys("")     # enter email
        self.driver.find_element(By.XPATH, "//*[@id=':rp:']").send_keys("")      # enter phone number

        # This is not required in web. It's optional.
        # self.driver.find_element(
        #     By.CSS_SELECTOR,
        #     "#scrollable-auto-tabpanel-1 > h6 > div > div.MuiGrid-root.MuiGrid-item.MuiGrid-grid-md-7.css-1odkrke > div:nth-child(4) > div > div:nth-child(4) > div > div > svg",
        # ).click()      

        element = self.driver.find_element(
            By.XPATH,
            "//*[@id='scrollable-auto-tabpanel-1']/h6/div/div[2]/div[6]/div/div[2]",
        )
    
        # scroll till 'buy now' button is not find /
        self.driver.execute_script(
            "window.scrollBy(0,1000)", " "
        )  # scroll till 1000 pixel /
        time.sleep(2)

        self.driver.find_element(
            By.XPATH,
            "//*[@id='scrollable-auto-tabpanel-1']/h6/div/div[2]/div[6]/div/div[2]",
        ).click()
        time.sleep(1)

        button = self.driver.find_element(By.XPATH, '//*[@id="scrollable-auto-tabpanel-1"]/h6/div/div[2]/div[6]/div/div[2]/button')
        
        if button.is_enabled():
            # Run the part when button is enabled
            button.click()
        else:
            # Run this part if button is disabled
            self.driver.close()
        

    
    def test_success_buy_epin_buying_for_self_data(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("https://sd-epin.bustto.com/")
        self.driver.maximize_window()
        time.sleep(1)

        self.driver.find_element(
            By.XPATH,
            "//*[@id='scrollable-auto-tabpanel-1']/h6/div/div[2]/div[1]/div/div/div[1]/button[2]",
        ).click()
        self.driver.find_element(
            By.XPATH,
            "//*[@id='scrollable-auto-tabpanel-1']/h6/div/div[2]/div[2]/div/div/button[2]",
        ).click()

        # Select to Buying for self
        self.driver.find_element(By.XPATH, "//*[@id='scrollable-auto-tabpanel-1']/h6/div/div[2]/div[3]/div/button[2]").click()

        # buying for self in all FIELD IS BLANK OR # Fill information in buying for self
        self.driver.find_element(By.XPATH, "//*[@id=':rb:']").send_keys("Meet Thakkar")     # enter name
        self.driver.find_element(By.XPATH, "//*[@id=':rc:']").send_keys("meet164023@gmail.com")     # enter email
        self.driver.find_element(By.XPATH, "//*[@id=':rp:']").send_keys("9106612343")      # enter phone number

        # This is not required in web. It's optional.
        # self.driver.find_element(
        #     By.CSS_SELECTOR,
        #     "#scrollable-auto-tabpanel-1 > h6 > div > div.MuiGrid-root.MuiGrid-item.MuiGrid-grid-md-7.css-1odkrke > div:nth-child(4) > div > div:nth-child(4) > div > div > svg",
        # ).click()      

        element = self.driver.find_element(
            By.XPATH,
            "//*[@id='scrollable-auto-tabpanel-1']/h6/div/div[2]/div[6]/div/div[2]",
        )
    
        # scroll till 'buy now' button is not find /
        self.driver.execute_script(
            "window.scrollBy(0,1000)", " "
        )  # scroll till 1000 pixel /
        time.sleep(2)

        self.driver.find_element(
            By.XPATH,
            "//*[@id='scrollable-auto-tabpanel-1']/h6/div/div[2]/div[6]/div/div[2]",
        ).click()
        time.sleep(1)

        # button = self.driver.find_element(By.XPATH, '//*[@id="scrollable-auto-tabpanel-1"]/h6/div/div[2]/div[6]/div/div[2]')
        # button.click()
        # if button.is_enabled():
        #     # Run the part when button is enabled
        #     button.click()
        # else:
        #     # Run this part if button is disabled
        #     self.driver.close()
        
        self.driver.find_element(By.XPATH, "/html/body/div[2]/div[3]/div/div/div[2]/button[2]").click()
        time.sleep(3)
        self.driver.close()

    

    def test_buy_epin_buying_for_self_email(self):           # Entered wrong email
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("https://sd-epin.bustto.com/")
        self.driver.maximize_window()
        time.sleep(1)

        self.driver.find_element(
            By.XPATH,
            "//*[@id='scrollable-auto-tabpanel-1']/h6/div/div[2]/div[1]/div/div/div[1]/button[2]",
        ).click()
        self.driver.find_element(
            By.XPATH,
            "//*[@id='scrollable-auto-tabpanel-1']/h6/div/div[2]/div[2]/div/div/button[2]",
        ).click()

        # Select to Buying for self
        self.driver.find_element(By.XPATH, "//*[@id='scrollable-auto-tabpanel-1']/h6/div/div[2]/div[3]/div/button[2]").click()

        # buying for self in all FIELD IS BLANK OR # Fill information in buying for self
        self.driver.find_element(By.XPATH, "//*[@id=':rb:']").send_keys("Meet Thakkar")     # enter name
        self.driver.find_element(By.XPATH, "//*[@id=':rc:']").send_keys("meet164023@")     # enter email
        self.driver.find_element(By.XPATH, "//*[@id=':rp:']").send_keys("9106612343")      # enter phone number

                                            # This is not required in web. It's optional.
                                            # self.driver.find_element(
                                            #     By.CSS_SELECTOR,
                                            #     "#scrollable-auto-tabpanel-1 > h6 > div > div.MuiGrid-root.MuiGrid-item.MuiGrid-grid-md-7.css-1odkrke > div:nth-child(4) > div > div:nth-child(4) > div > div > svg",
                                            # ).click()      

        element = self.driver.find_element(
            By.XPATH,
            "//*[@id='scrollable-auto-tabpanel-1']/h6/div/div[2]/div[6]/div/div[2]",
        )
    
        # scroll till 'buy now' button is not find /
        self.driver.execute_script(
            "window.scrollBy(0,1000)", " "
        )  # scroll till 1000 pixel /
        time.sleep(2)

        # self.driver.find_element(
        #     By.XPATH,
        #     "//*[@id='scrollable-auto-tabpanel-1']/h6/div/div[2]/div[6]/div/div[2]",
        # ).click()
        # time.sleep(1)

        button = self.driver.find_element(By.XPATH, '//*[@id="scrollable-auto-tabpanel-1"]/h6/div/div[2]/div[6]/div/div[2]')
        # button.click()
        if button.is_enabled():
            # Run the part when button is enabled
            button.click()
            print(" "*200)
            print(" "*200)
            print("*"*200)
            print(" "*200)
            print(" "*200)
        else:
            # Run this part if button is disabled
            self.driver.close()
    

    def test_buy_epin_buying_for_self_mobile(self):           # Entered wrong mobile
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("https://sd-epin.bustto.com/")
        self.driver.maximize_window()
        time.sleep(1)

        self.driver.find_element(
            By.XPATH,
            "//*[@id='scrollable-auto-tabpanel-1']/h6/div/div[2]/div[1]/div/div/div[1]/button[2]",
        ).click()
        self.driver.find_element(
            By.XPATH,
            "//*[@id='scrollable-auto-tabpanel-1']/h6/div/div[2]/div[2]/div/div/button[2]",
        ).click()

        # Select to Buying for self
        self.driver.find_element(By.XPATH, "//*[@id='scrollable-auto-tabpanel-1']/h6/div/div[2]/div[3]/div/button[2]").click()

        # buying for self in all FIELD IS BLANK OR # Fill information in buying for self
        self.driver.find_element(By.XPATH, "//*[@id=':rb:']").send_keys("Meet Thakkar")     # enter name
        self.driver.find_element(By.XPATH, "//*[@id=':rc:']").send_keys("meet164023@gmail.com")     # enter email
        self.driver.find_element(By.XPATH, "//*[@id=':rp:']").send_keys("91066")      # enter phone number

                                            # This is not required in web. It's optional.
                                            # self.driver.find_element(
                                            #     By.CSS_SELECTOR,
                                            #     "#scrollable-auto-tabpanel-1 > h6 > div > div.MuiGrid-root.MuiGrid-item.MuiGrid-grid-md-7.css-1odkrke > div:nth-child(4) > div > div:nth-child(4) > div > div > svg",
                                            # ).click()      

        element = self.driver.find_element(
            By.XPATH,
            "//*[@id='scrollable-auto-tabpanel-1']/h6/div/div[2]/div[6]/div/div[2]",
        )
    
        # scroll till 'buy now' button is not find /
        self.driver.execute_script(
            "window.scrollBy(0,1000)", " "
        )  # scroll till 1000 pixel /
        time.sleep(2)

        # self.driver.find_element(
        #     By.XPATH,
        #     "//*[@id='scrollable-auto-tabpanel-1']/h6/div/div[2]/div[6]/div/div[2]",
        # ).click()
        # time.sleep(1)

        button = self.driver.find_element(By.XPATH, '//*[@id="scrollable-auto-tabpanel-1"]/h6/div/div[2]/div[6]/div/div[2]')
        # button.click()
        if button.is_enabled():
            # Run the part when button is enabled
            button.click()
            print(" "*200)
            print(" "*200)
            print("*"*200)
            print(" "*200)
            print(" "*200)
        else:
            # Run this part if button is disabled
            self.driver.close()


# denominaton test greater than 10000


    def test_denomination_limit_in_buying_for_self(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("https://sd-epin.bustto.com/")
        self.driver.maximize_window()
        time.sleep(1)

        self.driver.find_element(
            By.XPATH,
            "//*[@id=':ra:']",
        ).send_keys("000")
        # time.sleep(3)
        
        # Quantity_button = self.driver.find_element(
        #     By.XPATH,
        #     "//*[@id='scrollable-auto-tabpanel-1']/h6/div/div[2]/div[2]/div/div/button[2]",
        # )



if __name__ == "__main__":
    unittest.main()



























# class TestBuyNow(unittest.TestCase):
#     def setUp(self) -> None:
#         self.driver = self.driver = webdriver.Chrome(ChromeDriverManager().install())
#         return super().setUp()
    
#     def tearDown(self) -> None:
#         return super().tearDown()
    