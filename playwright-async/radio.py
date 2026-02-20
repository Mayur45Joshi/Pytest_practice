import asyncio
from playwright.async_api import async_playwright, expect


async def radio_buttons():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False, slow_mo=300)
        context = await browser.new_context()
        page = await context.new_page()

        await page.goto("https://testautomationpractice.blogspot.com/")

        male_radio = page.locator("#male")

        # visibility of element and enable check
        await expect(male_radio).to_be_visible()
        await expect(male_radio).to_be_enabled()

        # default → should NOT be checked
        await expect(male_radio).not_to_be_checked()

        # select radio button
        await male_radio.check()

        # validation → should be checked
        await expect(male_radio).to_be_checked()

        await page.wait_for_timeout(5000)

        await browser.close()


asyncio.run(radio_buttons())
