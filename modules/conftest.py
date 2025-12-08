# import pytest
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
#
# # @pytest.fixture()  # decorators
# # def setup():
# #     print("befor launching browser")
# #     print("before opem application")
# #     yield
# #     print("after test case")
#
#
# # #for single chrome web drver initiate
# # @pytest.fixture()  # decorators
# # def setup():
# #     serv_obj = Service("C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python312\\chromedriver.exe")
# #     driver = webdriver.Chrome(service=serv_obj)
# #     return driver
# #     # print("launching browser")
# #     # return "chrome"
#
#
#
# @pytest.fixture()  # decorators
# def setup(browser):
#     if browser=="chrome":
#         serv_obj = Service("C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python312\\chromedriver.exe")
#         driver = webdriver.Chrome(service=serv_obj)
#
#     elif browser=="edge":
#         serv_obj = Service("C:\\Users\\HP\\Downloads\\edgedriver_win64\\msedgedriver.exe")
#         driver = webdriver.Edge(service=serv_obj)
#
#     elif browser=="firefox":
#         serv_obj = Service("C:\\Users\\HP\\Downloads\\geckodriver-v0.34.0-win64\\geckodriver.exe")
#         driver = webdriver.Firefox(service=serv_obj)
#
#     return driver
#
# def pytest_addoption(parser):  #this will get value from CLI
#     parser.addoption("--browser")
#
# @pytest.fixture()
# def browser(request):       #retrun browser valuee to setup method
#     return request.config.getoption("--browser")
#
#
# #customise html report
# #it is a hook for adding enviroment info to html report
# # def pytest_configure(config):
# #     config._metadata['project name'] = "Orage HRM"
# #     config._metadata['module name'] = "login app"
# #     config._metadata['tester'] = "mayur"
#
#
# #it is hook for to delete / modify env info on html report
# # @pytest.mark.optionalhook
# # def pytest_metadata(metadata):
# #     metadata.pop("JAVA_HOME", None)
# #     metadata.pop("Plugins",None)
#
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.firefox.service import Service as FirefoxService

@pytest.fixture()
def setup(browser):
    driver = None  # Initialize to avoid UnboundLocalError

    if browser.lower() == "chrome":
        serv_obj = Service(r"C:\Users\HP\AppData\Local\Programs\Python\Python312\chromedriver.exe")
        driver = webdriver.Chrome(service=serv_obj)

    elif browser.lower() == "edge":
        serv_obj = EdgeService(r"C:\Users\HP\Downloads\edgedriver_win64\msedgedriver.exe")
        driver = webdriver.Edge(service=serv_obj)

    elif browser.lower() == "firefox":
        serv_obj = FirefoxService(r"C:\Users\HP\Downloads\geckodriver-v0.34.0-win64\geckodriver.exe")
        driver = webdriver.Firefox(service=serv_obj)

    else:
        raise ValueError(f"Browser '{browser}' is not supported. Use chrome/edge/firefox.")

    driver.maximize_window()
    yield driver
    driver.quit()

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Browser to run tests on")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")
