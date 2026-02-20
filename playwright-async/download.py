import asyncio
import os
from playwright.async_api import async_playwright


async def main():
    async with async_playwright() as p:

        browser = await p.chromium.launch(headless=False, slow_mo=100)
        context = await browser.new_context(accept_downloads=True)
        page = await context.new_page()

        download_path = "downloads/testfile.txt"
        os.makedirs("downloads", exist_ok=True)

        await page.goto("https://testautomationpractice.blogspot.com/p/download-files_25.html")

        await page.fill("#inputText", "welcome")
        await page.click("#generateTxt")

        # 🔹 Proper Playwright download handling
        async with page.expect_download() as download_info:
            await page.click("#txtDownloadLink")

        download = await download_info.value
        await download.save_as(download_path)

        await page.wait_for_timeout(2000)

        # 🔹 Verify file exists
        if os.path.exists(download_path):
            print("✅ File downloaded successfully:", download_path)
        else:
            print("❌ File download failed")

        await browser.close()


asyncio.run(main())
