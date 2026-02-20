import asyncio
from playwright.async_api import async_playwright


async def main():
    async with async_playwright() as p:

        browser = await p.chromium.launch(headless=False, slow_mo=100)
        context = await browser.new_context()
        page = await context.new_page()

        await page.goto("https://blazedemo.com/")

        # Select dropdown values
        await page.locator("select[name='fromPort']").select_option("Boston")
        await page.locator("select[name='toPort']").select_option("London")

        await page.locator("input[value='Find Flights']").click()

        # Get all table rows
        rows = page.locator("table tbody tr")
        row_count = await rows.count()

        prices = []

        for i in range(row_count):
            price_text = await rows.nth(i).locator("td").nth(5).inner_text()
            price_value = float(price_text.replace("$", ""))
            prices.append((price_value, i))

        # Get lowest price row
        lowest_price, index = min(prices)

        print(f"Lowest Price: ${lowest_price}")

        # Click corresponding "Choose This Flight" button
        await rows.nth(index).locator("input[value='Choose This Flight']").click()

        await page.wait_for_timeout(5000)
        await browser.close()


asyncio.run(main())
