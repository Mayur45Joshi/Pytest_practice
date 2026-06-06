import allure
from selenium.webdriver.common.by import By

@allure.feature("Login Feature")
def test_valid_login(driver):
    """Successful login on SauceDemo"""
    driver.get("https://www.saucedemo.com")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    assert "inventory.html" in driver.current_url

@allure.feature("Failure Analysis Demo")
def test_broken_element(driver):
    """This test will fail, triggering the AI hook in conftest.py"""
    driver.get("https://www.saucedemo.com")
    # Intentional wrong ID to trigger AI root cause analysis
    driver.find_element(By.ID, "non_existent_id_123").click()