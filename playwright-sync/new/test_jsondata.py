import pytest
from playwright.sync_api import expect, Page
import json

#Read json file
file=open("data.json","r")
login_data=json.load(file)

# email id

@pytest.mark.parametrize("email, password, validity",[
    (data["email"], data["password"], data["validity"]) for data in login_data
    ])

def test_login_data_driven(email, password, validity, page:Page):
    page.goto("https://demowebshop.tricentis.com/login")

    #fill teh login form
    page.locator("#Email"). fill(email)
    page.locator("#Password").fill(password) #password
    page.locator("input[value='Log in']").click()

    #validation
    if validity == "valid":
        logout_link=page.locator("a[href='/logout']")
        expect(logout_link).to_be_visible(timeout=5000)
    else:
        error_message=page. locator(".validation-summary-errors")
        expect(error_message).to_be_visible(timeout=5000) # checking error message
        expect(page).to_have_url("https://demowebshop.tricentis.com/login") # checking same Login page