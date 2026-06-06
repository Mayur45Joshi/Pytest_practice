from playwright.async_api import async_playwright

async def run():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()

        await page.goto("https://example.com")

        # Access shadow DOM element directly
        await page.locator("custom-element >> #shadow-btn").click()

        await browser.close()