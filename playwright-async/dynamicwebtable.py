# import asyncio
# from playwright.async_api import async_playwright, expect
#
#
# async def verify_chrome_cpu_load(page):
#     await page.goto("https://practice.expandtesting.com/dynamic-table")
#
#     table = page.locator("table.table tbody")
#     rows = await table.locator("tr").all()
#
#     cpu_load = ""
#
#     for row in rows:
#         process_name = await row.locator("td").nth(0).inner_text()
#
#         if process_name == "Chrome":
#             cpu_load = await row.locator("td:has-text('%')").inner_text()
#             print("CPU Load of Chrome:", cpu_load)
#             break
#
#     await expect(page.locator("#chrome-cpu")).to_contain_text(cpu_load)
#     await page.wait_for_timeout(3000)
#
#
# async def main():
#     async with async_playwright() as p:
#         browser = await p.chromium.launch(headless=False, slow_mo=300)
#         context = await browser.new_context()
#         page = await context.new_page()
#
#         await verify_chrome_cpu_load(page)
#
#         await browser.close()
#
#
# if __name__ == "__main__":
#     asyncio.run(main())


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

import asyncio
from playwright.async_api import async_playwright, expect


async def main():

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False, slow_mo=300)
        context = await browser.new_context()
        page = await context.new_page()

        # await main(page)
        #
        # #await browser.close()
        await page.goto("https://practice.expandtesting.com/dynamic-table")

        table = page.locator("table.table tbody")
        rows = await table.locator("tr").all()

        cpu_load = ""

        for row in rows:
            process_name = await row.locator("td").nth(0).inner_text()

            if process_name == "Chrome":
                cpu_load = await row.locator("td:has-text('%')").inner_text()
                print("CPU Load of Chrome:", cpu_load)
                break

        await expect(page.locator("#chrome-cpu")).to_contain_text(cpu_load)
        await page.wait_for_timeout(3000)
        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())
