import asyncio
from playwright.async_api import async_playwright, expect


async def select_date(page, target_year, target_month, target_day):

    while True:
        headers = await page.locator("h3[aria-live='polite']").all_text_contents()

        if f"{target_month} {target_year}" in headers:
            index = headers.index(f"{target_month} {target_year}")
            break
        else:
            await page.locator('button[aria-label="Next month"]').click()
            await page.wait_for_timeout(800)

    # Pick correct calendar and select day
    dates = page.locator("table.b8fcb0c66a tbody").nth(index).locator("td")

    count = await dates.count()
    for i in range(count):
        if await dates.nth(i).inner_text() == target_day:
            await dates.nth(i).click()
            break


async def main():
    async with async_playwright() as p:

        browser = await p.chromium.launch(headless=False, slow_mo=100)
        context = await browser.new_context()
        page = await context.new_page()

        await page.goto("https://www.booking.com/")
        await page.wait_for_timeout(3000)

        await page.get_by_test_id("searchbox-dates-container").click()

        await select_date(page, "2025", "December", "25")
        await select_date(page, "2025", "December", "31")

        checkin_text = await page.locator(
            "span[data-testid='date-display-field-start']"
        ).inner_text()

        checkout_text = await page.locator(
            "span[data-testid='date-display-field-end']"
        ).inner_text()

        print("Check-in date  :===>", checkin_text)
        print("Check-out date :===>", checkout_text)

        await expect(
            page.locator("span[data-testid='date-display-field-start']")
        ).to_contain_text(checkin_text)

        await expect(
            page.locator("span[data-testid='date-display-field-end']")
        ).to_contain_text(checkout_text)

        await page.wait_for_timeout(5000)
        await browser.close()


asyncio.run(main())
