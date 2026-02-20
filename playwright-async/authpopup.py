import asyncio
from playwright.async_api import async_playwright, expect


async def main():
    async with async_playwright() as p:

        browser = await p.chromium.launch(headless=False)

        # ============================
        # Method 1: Credentials in URL
        # ============================
        context1 = await browser.new_context()
        page1 = await context1.new_page()

        await page1.goto("https://admin:admin@the-internet.herokuapp.com/basic_auth")
        await expect(page1.locator("text=Congratulations")).to_be_visible()

        print("✅ Basic Auth using URL passed")

        await page1.wait_for_timeout(3000)
        await context1.close()

        # ==================================
        # Method 2: Using Browser Context
        # ==================================
        context2 = await browser.new_context(
            http_credentials={"username": "admin", "password": "admin"}
        )

        page2 = await context2.new_page()
        await page2.goto("https://the-internet.herokuapp.com/basic_auth")

        await expect(page2.locator("text=Congratulations")).to_be_visible()

        print("✅ Basic Auth using browser context")

        await page2.wait_for_timeout(3000)
        await context2.close()

        await browser.close()


asyncio.run(main())
