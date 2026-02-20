import asyncio
from playwright.async_api import async_playwright, expect

async def inputbox():

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False, slow_mo=1000)
        context = await browser.new_context()
        page = await context.new_page()

        await page.goto("https://testautomationpractice.blogspot.com/")

        text_box = page.locator("#name")

        # visibility of the element and enabled check
        await expect(text_box).to_be_visible()
        await expect(text_box).to_be_enabled()

        # check attribute
        await expect(text_box).to_have_attribute("maxlength", "15")

        # get attribute value
        maxlength = await text_box.get_attribute("maxlength")
        print("Maximum Length of inputbox:", maxlength)

        # fill input
        await text_box.fill("John Kenedy")

        # get entered value
        entered_value = await text_box.input_value()
        print("Value entered is:", entered_value)

        await page.wait_for_timeout(5000)

        await browser.close()

asyncio.run(inputbox())
