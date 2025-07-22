import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

class Testclass:


    def test_logo(self,setup):

        self.driver = setup
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        time.sleep(5)
        try:
            self.status=self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div/div[1]/div/div[1]/img").is_selected()
            self.driver.close()
            assert self.status==True

        except:
            self.driver.close()
            assert False

    def test_login(self,setup):

        # print(setup)
        # self.serv_obj = Service("C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python312\\chromedriver.exe")
        # self.driver = webdriver.Chrome(service=self.serv_obj)
        self.driver=setup
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("Admin")
        self.driver.find_element(By.XPATH, "//input[@name='password']").send_keys("admin123")
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(5)
        try:
            self.status=self.driver.find_element(By.XPATH,"//h6[normalize-space()='Dashboard']").is_displayed()
            self.driver.close()
            assert self.status==True

        except:
            self.driver.close()
            assert False