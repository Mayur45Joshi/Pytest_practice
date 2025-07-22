from selenium.webdriver.chrome.service import Service
from selenium import webdriver
import pytest
#from pageobject import Loginpageobject

from pytestproject.pageobject.Loginpageobject import LoginPage


class TestLogin:

    def test_logint(self):
        self.serv_obj = Service("C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python312\\chromedriver.exe")
        self.driver = webdriver.Chrome(service=self.serv_obj)
        self.driver.get("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F")
        self.driver.maximize_window()

        self.lp=LoginPage(self.driver)
        self.lp.setUserName("admin@yourstore.com")
        self.lp.setPassword("admin")
        self.lp.clicklogin()
        self.act_title=self.driver.title
        self.driver.close()
        assert self.act_title =="Dashboard / nopCommerce administration"


