import asyncio

from playwright.async_api import async_playwright


async def main():
    async with async_playwright() as p:

        browser= await p.chromium.launch(headless=False)
        context= await browser.new_context()
        page= await context.new_page()


        await page.goto("https://testautomationpractice.blogspot.com/")
        page.once("dialog",lambda dialog: asyncio.create_task(dialog.accept()))
        await page.click("#alertBtn")
        await page.wait_for_timeout(2000)


asyncio.run(main())




