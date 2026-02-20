import asyncio
from playwright.async_api import async_playwright, expect


async def handle_popups():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False, slow_mo=300)
        context = await browser.new_context()
        page = await context.new_page()

        await page.goto("https://testautomationpractice.blogspot.com/")

        # Handle popup event
        page.on("popup", lambda popup: asyncio.create_task(popup.wait_for_load_state()))

        # Click button that opens popup
        await page.locator("#PopUp").click()
        await page.wait_for_timeout(5000)

        # Get all opened pages (main + popups)
        all_pages = context.pages
        print("Total number of popups/pages:", len(all_pages))

        # Capture URLs and work on required popup
        for pw in all_pages:
            print("Popup/Page URL ======>", pw.url)
            title = await pw.title()

            if "Playwright" in title:
                await pw.locator(".getStarted_Sjon").click()
                await pw.wait_for_timeout(3000)
                await expect(pw).to_have_title("Installation | Playwright")
                await pw.close()

        await page.wait_for_timeout(5000)
        await context.close()
        await browser.close()


asyncio.run(handle_popups())
