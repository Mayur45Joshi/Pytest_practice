import asyncio
import re
from playwright.async_api import async_playwright, expect

async def locators():

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False, slow_mo=500)
        context = await browser.new_context()
        page = await context.new_page()

        # -------- Page 1 --------
        await page.goto("https://demo.nopcommerce.com/")

        await page.wait_for_timeout(5000)

        logo = page.get_by_alt_text("nopCommerce demo store")
        await expect(logo).to_be_visible()

        await expect(page.get_by_text("Welcome to our store")).to_be_visible()   # full text
        await expect(page.get_by_text("Welcome to")).to_be_visible()             # partial text
        await expect(page.get_by_text(re.compile(".*Welcome.*"))).to_be_visible()

        # -------- Page 2 --------
        await page.goto("https://demo.nopcommerce.com/register?returnUrl=%2F")

        await page.wait_for_timeout(5000)

        await expect(page.get_by_role("heading", name="Register")).to_be_visible()

        await page.get_by_label("First name:").fill("John")
        await page.get_by_label("Last name:").fill("Kenedy")
        await page.get_by_label("Email:").fill("abc@gmail.com")

        await page.wait_for_timeout(5000)

        await page.get_by_placeholder("Search store").fill("Apple MacBook Pro")

        await page.wait_for_timeout(5000)

        # -------- Page 3 --------
        await page.goto("https://testautomationpractice.blogspot.com/p/playwrightpractice.html")

        await expect(page.get_by_title("Home page link")).to_have_text("Home")
        await expect(page.get_by_title("HyperText Markup Language")).to_have_text("HTML")

        await page.wait_for_timeout(5000)

        await expect(page.get_by_test_id("profile-name")).to_have_text("John Doe")
        await expect(page.get_by_test_id("profile-email")).to_have_text("john.doe@example.com")

        await browser.close()


asyncio.run(locators())
