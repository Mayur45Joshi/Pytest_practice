import asyncio
from playwright.async_api import async_playwright, expect


async def main():
    async with async_playwright() as p:

        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()
        page = await context.new_page()

        await page.goto("https://demowebshop.tricentis.com/")

        # ---------------- Tag + ID ----------------
        await page.locator("#small-searchterms").fill("T-Shirts")
        await page.wait_for_timeout(3000)

        # ---------------- Tag + Class ----------------
        await page.locator("input.search-box-text").fill("T-Shirts")
        # await page.locator(".search-box-text").fill("T-Shirts")
        await page.wait_for_timeout(3000)

        # ---------------- Tag + Attribute ----------------
        await page.locator("input[name=q]").fill("T-Shirts")
        await page.locator("[name=q]").fill("7-Shirts")
        await page.wait_for_timeout(3000)

        # ---------------- Class + Attribute ----------------
        await page.locator(".search-box-text[value='Search store']").fill("T-Shirts")
        await page.wait_for_timeout(3000)

        print("✅ CSS Locator test executed successfully")

        await browser.close()


asyncio.run(main())
