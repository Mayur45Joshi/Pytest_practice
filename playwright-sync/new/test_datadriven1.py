login_test_Data=[ ("Laura.taylor1234@example.com", "test123", "valid"),
                    ("invaliduser@example.com", "test321", "invalid"),
                    ("validuser@example.com", "testxyz", "invalid"),
                    ("", "", "invalid")]

import pytest
from playwright.sync_api import expect,Page

@pytest.mark.parametrize("email,password, validity", login_test_Data)
def test_login_data_driven(email, password, validity, page:Page):
    page. goto("https://demowebshop.tricentis.com/login")

    #fill teh Login form
    page.locator("#Email").fill(email) # email id
    page.locator("#Password").fill(password) #password
    page.locator ("input[value='Log in' ]").click()

    # validation
    if validity == "valid":
        logout_link = page.locator("a[href='/logout']")
        expect(logout_link).to_be_visible(timeout=5000)

    else:
        error_message = page.locator(".validation-summary-errors")
        expect(error_message).to_be_visible(timeout=5000)  # checking error wessage
        expect(page).to_have_url("https://demowebshop,tricentis.com/login")  # checking same login page



