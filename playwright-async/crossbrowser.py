import asyncio
from playwright.async_api import async_playwright


async def run_test(browser_type):
    browser = await browser_type.launch(headless=False)
    page = await browser.new_page()
    await page.goto("https://www.saucedemo.com/")

    print(f"Title in {browser_type.name}: ", await page.title())

    await browser.close()


async def main():
    async with async_playwright() as p:
        await run_test(p.chromium)
        await run_test(p.firefox)
        await run_test(p.webkit)


asyncio.run(main())