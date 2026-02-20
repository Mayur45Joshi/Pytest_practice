import asyncio
from playwright.async_api import async_playwright

async def handle_tabs():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()
        parent_page = await context.new_page()

        await parent_page.goto("https://testautomationpractice.blogspot.com/")

        # Wait for new tab to open
        async with context.expect_page() as new_tab:
            await parent_page.locator("button:has-text('New Tab')").click()

        child_page = await new_tab.value
        await child_page.wait_for_load_state()

        all_pages = context.pages
        print("Number of tabs/pages :==== >", len(all_pages))

        print("Title of parent page:", await parent_page.title())
        print("Title of child page/tab:", await child_page.title())

        print("URL of child page/tab:", child_page.url)

        await browser.close()

asyncio.run(handle_tabs())
