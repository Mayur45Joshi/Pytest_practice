import asyncio
from playwright.async_api import async_playwright, expect


async def pagination_table(page):
    await page.goto("https://datatables.net/examples/basic_init/zero_configuration.html")

    has_more_pages = True

    while has_more_pages:
        rows = await page.locator("#example tbody tr").all()

        for row in rows:
            print(await row.inner_text())

        next_button = page.locator("button[aria-label='Next']")
        class_value = await next_button.get_attribute("class")

        if "disabled" in class_value:
            has_more_pages = False
        else:
            await next_button.click()
            await page.wait_for_timeout(1000)


async def filter_rows(page):
    await page.goto("https://datatables.net/examples/basic_init/zero_configuration.html")

    dropdown = page.locator("#dt-length-0")
    await dropdown.select_option(label="25")

    rows = page.locator("#example tbody tr")

    row_count = await rows.count()
    print("Number of rows filtered:", row_count)

    await expect(rows).to_have_count(25)

    await page.wait_for_timeout(5000)


async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False, slow_mo=500)
        context = await browser.new_context()
        page = await context.new_page()

        print("---- Pagination Test ----")
        await pagination_table(page)

        print("---- Filter Rows Test ----")
        await filter_rows(page)

        await browser.close()


asyncio.run(main())
