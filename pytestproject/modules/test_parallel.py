import time

import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver

class TestLogin:
    def test_login_chrome(self):
        #from selenium.webdriver.chrome import webdriver
        from selenium.webdriver.chrome.service import Service
        self.serv_obj=Service("C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python312\\chromedriver.exe")
        #self.serv_obj = Service("C:\\Users\\HP\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")
        #C:\Users\HP\Downloads\chromedriver - win64\chromedriver - win64
        self.driver=webdriver.Chrome(service=self.serv_obj)
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        time.sleep(5)
        self.driver.find_element(By.XPATH,"//input[@placeholder='Username']").send_keys("Admin")
        self.driver.find_element(By.XPATH, "//input[@name='password']").send_keys("admin123")
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()

    def test_login_Firefox(self):
        # from selenium.webdriver.chrome import webdriver
        from selenium.webdriver.firefox.service import Service
        self.serv_obj = Service("C:\\Users\\HP\\Downloads\\geckodriver-v0.34.0-win64\\geckodriver.exe")
        # self.serv_obj = Service("C:\\Users\\HP\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")
        # C:\Users\HP\Downloads\chromedriver - win64\chromedriver - win64
        self.driver = webdriver.Firefox(service=self.serv_obj)
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("Admin")
        self.driver.find_element(By.XPATH, "//input[@name='password']").send_keys("admin123")
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()

    def test_login_Edge(self):
        # from selenium.webdriver.chrome import webdriver
        from selenium.webdriver.edge.service import Service
        self.serv_obj = Service("C:\\Users\\HP\\Downloads\\edgedriver_win64\\msedgedriver.exe")
        # self.serv_obj = Service("C:\\Users\\HP\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")
        # C:\Users\HP\Downloads\chromedriver - win64\chromedriver - win64
        self.driver = webdriver.Edge(service=self.serv_obj)
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("Admin")
        self.driver.find_element(By.XPATH, "//input[@name='password']").send_keys("admin123")
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()