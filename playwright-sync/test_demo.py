import time

from playwright.sync_api import expect,Page
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


def test_demoexam(page:Page):

    page.goto("https://blazedemo.com/")
    page.locator("//select[@name='fromPort']").select_option('Boston')
    page.locator("select[name=toPort]").select_option('London')
    page.locator("input[value='Find Flights']").click()

    table=page.locator("table tbody")
    rows=table.locator("tr").all()

    prices=[]
    for i,row in enumerate(rows):
        price_txt=row.locator("td").nth(5).inner_text()
        price_val=float(price_txt.replace("$",""))
        prices.append((price_txt,i))

    low_pr,index=sorted(prices)[0]
    print(low_pr)
    rows[index].locator("td [value='Choose This Flight']").click()
    page.wait_for_timeout(10000)


def test_withselenium():

    driver=webdriver.Chrome()
    driver.get("https://blazedemo.com/")
    from_d=Select(driver.find_element(By.XPATH,"//select[@name='fromPort']"))
    from_d.select_by_value("Boston")
    tod=Select(driver.find_element(By.XPATH,"//select[@name='toPort']"))
    tod.select_by_value("Berlin")
    driver.find_element(By.XPATH,"//input[@value='Find Flights']").click()
    time.sleep(2)
    table=driver.find_element(By.CSS_SELECTOR,"table tbody")
    rows=table.find_elements(By.CSS_SELECTOR,"tr")
    prices=[]
    for i,row in enumerate(rows):
        price_txt=row.find_element(By.XPATH,"td[6]").text
        price=float(price_txt.replace("$",""))
        prices.append((price_txt,i))

    low_p,index=sorted(prices)[1]
    rows[index].find_element(By.CSS_SELECTOR,"td [value='Choose This Flight']").click()

    time.sleep(10)

