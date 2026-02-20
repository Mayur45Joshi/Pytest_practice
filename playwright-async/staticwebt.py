import asyncio
from playwright.async_api import async_playwright, expect


async def static_web_table():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False, slow_mo=200)
        context = await browser.new_context()
        page = await context.new_page()

        await page.goto("https://testautomationpractice.blogspot.com/")

        # locating table
        table = page.locator("table[name='BookTable'] tbody")
        await expect(table).to_be_visible()

        # 1. count total number of rows
        rows = table.locator("tr")
        await expect(rows).to_have_count(7)

        row_count = await rows.count()
        print("Number of rows in a table:", row_count)

        # 2. count total columns / headers
        columns = rows.locator("th")
        await expect(columns).to_have_count(4)

        column_count = await columns.count()
        print("Number of columns:", column_count)

        # 3. Read all data from 2nd row
        second_row_cells = rows.nth(2).locator("td")
        second_row_texts = await second_row_cells.all_inner_texts()

        print("2nd row data ===== >:", second_row_texts)

        await expect(second_row_cells).to_have_text(
            ['Learn Java', 'Mukesh', 'Java', '500']
        )

        print("Printing 2nd row data ....... ")
        for text in second_row_texts:
            print(text)

        # 4. Read all table data (excluding header)
        all_rows = await rows.all()

        print("\nPrinting all table data:")
        for row in all_rows[1:]:
            cols = await row.locator('td').all_inner_texts()
            print(cols)

        # 5. Print book names where author = Mukesh
        print("\nBooks written by Mukesh:")
        for row in all_rows[1:]:
            author = await row.locator('td').nth(1).inner_text()
            if author == 'Mukesh':
                book = await row.locator('td').nth(0).inner_text()
                print(f"{author}  ->  {book}")

        # 6. Calculate total price
        total_price = 0
        for row in all_rows[1:]:
            price = await row.locator('td').nth(3).inner_text()
            total_price += int(price)

        print("\nTotal price:", total_price)

        await page.wait_for_timeout(5000)
        await browser.close()


asyncio.run(static_web_table())
