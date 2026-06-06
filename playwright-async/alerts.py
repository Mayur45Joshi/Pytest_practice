import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()
        page = await context.new_page()

        await page.goto("https://testautomationpractice.blogspot.com/")

        # -------- Normal Alert --------
        #page.once("dialog", lambda dialog: asyncio.create_task(dialog.accept()))
        page.once("dialog", lambda dialog : dialog.accept())
        await page.click("#alertBtn")
        await page.wait_for_timeout(2000)

        # -------- Confirmation Alert --------
        #page.once("dialog", lambda dialog: asyncio.create_task(dialog.dismiss()))
        page.once("dialog", lambda dialog: dialog.dismiss())
        await page.click("#confirmBtn")
        await page.wait_for_timeout(2000)

        text = await page.locator("#demo").inner_text()
        print("Confirm result:", text)

        # -------- Prompt Alert --------
        #page.once("dialog", lambda dialog: asyncio.create_task(dialog.accept("Mayur")))
        page.once("dialog", lambda dialog: dialog.accept("mayur"))
        await page.click("#promptBtn")
        await page.wait_for_timeout(2000)

        text = await page.locator("#demo").inner_text()
        print("Prompt result:", text)

        await browser.close()

asyncio.run(main())
