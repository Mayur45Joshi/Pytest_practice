import asyncio
from playwright.async_api import async_playwright, expect

async def select_date(page, target_year, target_month, target_date, is_future):

    # selecting month and year from the date picker
    while True:
        current_month = await page.locator('.ui-datepicker-month').text_content()
        current_year = await page.locator('.ui-datepicker-year').text_content()

        if current_month == target_month and current_year == target_year:
            break

        if is_future:
            await page.locator(".ui-datepicker-next").click()   # future date
        else:
            await page.locator(".ui-datepicker-prev").click()   # past date

    all_dates = await page.locator(".ui-datepicker-calendar td").all()

    # selecting date
    for dt in all_dates:
        date_text = await dt.inner_text()
        if date_text == target_date:
            await dt.click()
            break


async def jquery_datepicker():

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False, slow_mo=1000)
        context = await browser.new_context()
        page = await context.new_page()

        await page.goto("https://testautomationpractice.blogspot.com/")

        date_input = page.locator("#datepicker")

        is_future = True
        year = "2026"
        month = "October"
        date = "15"

        await date_input.click()
        await select_date(page, year, month, date, is_future)

        print("Selected date ==== >:", await date_input.input_value())
        await expect(date_input).to_have_value("10/15/2026")

        await page.wait_for_timeout(5000)
        await browser.close()


asyncio.run(jquery_datepicker())
