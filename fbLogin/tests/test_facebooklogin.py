import time

from selenium.webdriver.common.by import By


def test_fblogin(setup):
    driver=setup
    driver.get("https://www.facebook.com/")
    time.sleep(3)
    driver.find_element(By.ID, "email").send_keys("testuser@gmail.com")
    driver.find_element(By.ID, "pass").send_keys("dummyPassword")
    driver.find_element(By.NAME, "login").click()
    time.sleep(3)
    title = driver.title
    print(f"Page title is: {title}")

    # Validate title contains "Facebook"
    assert "Facebook" in title