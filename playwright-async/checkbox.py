import asyncio
from playwright.async_api import async_playwright, expect


async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()
        page = await context.new_page()

        await page.goto("https://testautomationpractice.blogspot.com/")

        # 1. Select specific checkbox (Sunday)
        sunday_checkbox = page.get_by_label("Sunday")
        await sunday_checkbox.check()
        await expect(sunday_checkbox).to_be_checked()
        await page.wait_for_timeout(2000)

        # 2. Count number of checkboxes
        days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
        checkboxes = [page.get_by_label(day) for day in days]

        print("Total number of checkboxes:", len(checkboxes))

        # 3. Select all checkboxes
        for checkbox in checkboxes:
            await checkbox.check()
            await expect(checkbox).to_be_checked()

        await page.wait_for_timeout(2000)

        # 4. Uncheck last 3 checkboxes
        for checkbox in checkboxes[-3:]:
            await checkbox.uncheck()
            await expect(checkbox).not_to_be_checked()

        await page.wait_for_timeout(2000)

        # 5. Toggle checkboxes
        for checkbox in checkboxes:
            if await checkbox.is_checked():
                await checkbox.uncheck()
                await expect(checkbox).not_to_be_checked()
            else:
                await checkbox.check()
                await expect(checkbox).to_be_checked()

        await page.wait_for_timeout(2000)

        # 6. Randomly check checkboxes (1,3,6)
        indexes = [1, 3, 6]

        for i in indexes:
            await checkboxes[i].check()
            await expect(checkboxes[i]).to_be_checked()

        await page.wait_for_timeout(2000)

        # 7. Select checkbox based on label choice
        weekday = "Friday"

        for label in days:
            if label == weekday:
                checkbox = page.get_by_label(label)
                await checkbox.check()
                await expect(checkbox).to_be_checked()

        await page.wait_for_timeout(5000)

        await browser.close()


asyncio.run(main())
