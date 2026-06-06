from playwright.sync_api import Playwright, expect

def test_Login(playwright:Playwright):

    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    page = context.new_page()
    page.goto('https://www.demoblaze.com/index.html')
    page.wait_for_timeout(5000)
    page.locator('#login2').click()
    page.locator('#loginusername').fill('pavanol')
    page. locator('#loginpassword').fill('test@123')
    page.locator("button:has-text('Log in')").click()
    page.wait_for_timeout(10000)
    expect(page.locator("#logout2")).to_be_visible()
    expect(page. locator('#nameofuser')).to_contain_text('Welcome pavanol')

 #pytest test_flacky.py --headed --reruns 3 --reruns-delay 2