import asyncio
from playwright.async_api import async_playwright, expect

async def keyboardactions():

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False, slow_mo=500)
        context = await browser.new_context()
        page = await context.new_page()

        await page.goto("https://testautomationpractice.blogspot.com/")

        input1 = page.locator("#input1")

        # 1. Focus on input1
        await input1.focus()

        # 2. Type text
        await page.keyboard.insert_text("welcome")

        # 3. Ctrl + A (Select all)
        await page.keyboard.press("Control+A")

        # 4. Ctrl + C (Copy)
        await page.keyboard.press("Control+C")

        # 5. Press Tab twice → move to input2
        await page.keyboard.press("Tab")
        await page.keyboard.press("Tab")

        # 6. Ctrl + V (Paste into input2)
        await page.keyboard.press("Control+V")

        # 7. Press Tab twice → move to input3
        await page.keyboard.press("Tab")
        await page.keyboard.press("Tab")

        # 8. Ctrl + V (Paste into input3)
        await page.keyboard.press("Control+V")

        input2 = page.locator("#input2")
        input3 = page.locator("#input3")

        await expect(input2).to_have_value("welcome")
        await expect(input3).to_have_value("welcome")

        await page.wait_for_timeout(5000)
        await browser.close()


asyncio.run(keyboardactions())
