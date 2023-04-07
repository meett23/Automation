import pdb
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time


class TestCaseForEPIN(unittest.TestCase):
    # def test_Buy_EPIN(self):
    #     self.driver= webdriver.Chrome(ChromeDriverManager().install())
    #     self.driver.get("https://sd-epin.bustto.com/")
    #     self.driver.maximize_window()
    #     time.sleep(2)

    #     self.driver.find_element(By.XPATH, "//*[@id='scrollable-auto-tabpanel-1']/h6/div/div[2]/div[1]/div/div/div[1]/button[2]").click()
    #     self.driver.find_element(By.XPATH, "//*[@id='scrollable-auto-tabpanel-1']/h6/div/div[2]/div[2]/div/div/button[2]").click()
    #     self.driver.find_element(By.XPATH, "//*[@id=':rb:']").send_keys("Meet")
    #     self.driver.find_element(By.XPATH, "//*[@id=':rc:']").send_keys("PRITESH")
    #     self.driver.find_element(By.XPATH, "//*[@id=':rd:']").send_keys("meet.tagline@gmail.com")
    #     self.driver.find_element(By.XPATH, "//*[@id=':re:']").send_keys("9106612343")
    #     self.driver.find_element(By.CSS_SELECTOR, "#scrollable-auto-tabpanel-1 > h6 > div > div.MuiGrid-root.MuiGrid-item.MuiGrid-grid-md-7.css-1odkrke > div:nth-child(4) > div > div:nth-child(4) > div > div > svg").click()

    #     element= self.driver.find_element(By.XPATH, "//*[@id='scrollable-auto-tabpanel-1']/h6/div/div[2]/div[6]/div/div[2]")
    #     # driver.execute_script("arguments[0].scrollIntoView();", element)                    # scroll till 'buy now' button is not find /
    #     self.driver.execute_script("window.scrollBy(0,1000)", " ")                       # scroll till 1000 pixel /

    #     self.driver.find_element(By.XPATH, "//*[@id='scrollable-auto-tabpanel-1']/h6/div/div[2]/div[6]/div/div[2]").click()
    #     time.sleep(2)
    #     self.driver.find_element(By.XPATH, "/html/body/div[2]/div[3]/div/div/div[2]/button[2]").click()
    #     time.sleep(2)

    # def test_Buy_epin_with_enter_amount_above_100000(self):
    #     self.driver= webdriver.Chrome(ChromeDriverManager().install())
    #     self.driver.get("https://sd-epin.bustto.com/")
    #     self.driver.maximize_window()
    #     time.sleep(2)

    #     # self.driver.find_element(By.XPATH, "//*[@id='scrollable-auto-tabpanel-1']/h6/div/div[2]/div[1]/div/div/div[1]/button[2]").click()
    #     self.driver.find_element(By.XPATH, "//*[@id=':ra:']").send_keys("1000000")
    #     denomination=self.driver.find_element(By.XPATH, "//*[@id=':ra:']").get_attribute("value")

    #     if int(denomination) > 10000:
    #         print("***********************************")
    #         print("Please set denomination within Min. 10 INR , Max. 10000 INR")
    #         print("***********************************")

    #         return
    #     else:
    #         self.driver.find_element(By.XPATH, "//*[@id='scrollable-auto-tabpanel-1']/h6/div/div[2]/div[2]/div/div/button[2]").click()
    #         self.driver.find_element(By.XPATH, "//*[@id=':rb:']").send_keys("Meet")
    #         self.driver.find_element(By.XPATH, "//*[@id=':rc:']").send_keys("PRITESH")
    #         self.driver.find_element(By.XPATH, "//*[@id=':rd:']").send_keys("meet.tagline@gmail.com")
    #         self.driver.find_element(By.XPATH, "//*[@id=':re:']").send_keys("9106612343")
    #         self.driver.find_element(By.CSS_SELECTOR, "#scrollable-auto-tabpanel-1 > h6 > div > div.MuiGrid-root.MuiGrid-item.MuiGrid-grid-md-7.css-1odkrke > div:nth-child(4) > div > div:nth-child(4) > div > div > svg").click()

    #         element= self.driver.find_element(By.XPATH, "//*[@id='scrollable-auto-tabpanel-1']/h6/div/div[2]/div[6]/div/div[2]")
    #         # driver.execute_script("arguments[0].scrollIntoView();", element)                    # scroll till 'buy now' button is not find /
    #         self.driver.execute_script("window.scrollBy(0,1000)", " ")                       # scroll till 1000 pixel /
    #         time.sleep(3)

    #         self.driver.find_element(By.XPATH, "//*[@id='scrollable-auto-tabpanel-1']/h6/div/div[2]/div[6]/div/div[2]").click()
    #         time.sleep(2)
    #         self.driver.find_element(By.XPATH, "/html/body/div[2]/div[3]/div/div/div[2]/button[2]").click()
    #         time.sleep(2)

    def test_buy_epin_sender_details(self):
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
        name_field = self.driver.find_element(By.XPATH, "//*[@id=':rb:']")
        name_field.send_keys("  ")

        name_field_value = name_field.get_attribute("value")

        # 1. main element -- > key
        # 2. next first class --> content -- > error c
        # # PAGE SOURECH
        # # jss138 --> Content --> FAILED

        if "":
            print("************************************************")
            print("Please enter recipient name")
            print("************************************************")
            return
        else:
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
            self.driver.find_element(
                By.XPATH, "/html/body/div[2]/div[3]/div/div/div[2]/button[2]"
            ).click()
            time.sleep(2)


if __name__ == "__main__":
    unittest.main()


# driver.find_element(By.XPATH, "").click()
# time.sleep(10)
