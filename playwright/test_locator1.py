import time
import re

from playwright.sync_api import Page, expect

#page.get_by_alt_text()

def test_locators(page:Page):
    page.goto("https://demo.nopcommerce.com/")
    time.sleep(5) # seconds
    page.wait_for_timeout(5000) # 500 ms = 5 secs

    logo=page.get_by_alt_text("nopCommerce demo store")
    expect(logo).to_be_visible()

    expect(page.get_by_text("Welcome to our store")).to_be_visible()  # full text
    expect(page.get_by_text("Welcome to")).to_be_visible()  # partial text
    expect(page.get_by_text(re.compile(" .* Welcome .* "))).to_be_visible()

    page.goto("https://demo.nopcommerce.com/register?returnUrl=%2F")
    page.wait_for_timeout(5000)  # 568 ms = 5 secs
    expect(page.get_by_role("heading", name = "Register")).to_be_visible()

    page.get_by_label("First name:").fill("John")
    page.get_by_label("Last name:").fill("Kenedy")
    page.get_by_label("Email:").fill("abc@gmail.com")
    page.wait_for_timeout(5000)

    page.get_by_placeholder("Search store").fill("Apple MacBook Pro")
    page.wait_for_timeout(5000)

    page.goto("https://testautomationpractice.blogspot.com/p/playwrightpractice.html")
    expect(page.get_by_title("Home page link")).to_have_text("Home")
    expect(page.get_by_title("HyperText Markup Language")).to_have_text("HTML")
    page.wait_for_timeout(5000)

    expect(page.get_by_test_id("profile-name")).to_have_text("John Doe")
    expect(page.get_by_test_id("profile-email")).to_have_text("john.doe@example.com")

    page.close()



