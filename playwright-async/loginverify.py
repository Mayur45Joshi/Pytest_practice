import asyncio
from playwright.async_api import async_playwright, expect

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False, slow_mo=500)
        context = await browser.new_context()
        page = await context.new_page()

        # ---- Test 1: URL ----
        await page.goto("http://www.automationpractice.pl/index.php")
        print("Page URL:", page.url)
        await expect(page).to_have_url("http://www.automationpractice.pl/index.php")

        # ---- Test 2: Title ----
        await page.goto("http://www.automationpractice.pl/index.php")
        print("Page Title:", await page.title())
        await expect(page).to_have_title("My Shop")

        await browser.close()

asyncio.run(main())
