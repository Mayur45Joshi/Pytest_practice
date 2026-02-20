import asyncio
from playwright.async_api import async_playwright, expect


async def main():
    async with async_playwright() as p:

        # Launch browser
        browser = await p.chromium.launch(headless=False)

        # Create context
        context = await browser.new_context()

        # Create multiple pages
        page1 = await context.new_page()
        page2 = await context.new_page()

        # Page 1
        await page1.goto("https://playwright.dev/")
        await page1.wait_for_timeout(3000)
        await expect(page1).to_have_title(
            "Fast and reliable end-to-end testing for modern web apps | Playwright"
        )

        # Page 2
        await page2.goto("https://www.selenium.dev/")
        await page2.wait_for_timeout(3000)
        await expect(page2).to_have_title("Selenium")

        print("✅ Browser Context with Multiple Pages executed successfully")

        await browser.close()


asyncio.run(main())
