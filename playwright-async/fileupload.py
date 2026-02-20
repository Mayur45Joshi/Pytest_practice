import asyncio
from playwright.async_api import async_playwright, expect
import os


async def upload_single_file(page):
    await page.goto("https://testautomationpractice.blogspot.com/")

    # Upload single file
    await page.locator("#singleFileInput").set_input_files("uploads/Test1.txt")
    await page.locator("button:has-text('Upload Single File')").click()

    # Validation
    await expect(page.locator("#singleFileStatus")).to_contain_text("Test1.txt")

    print("✅ Single file uploaded successfully")

    await page.wait_for_timeout(3000)


async def upload_multiple_files(page):
    await page.goto("https://testautomationpractice.blogspot.com/")

    # Upload multiple files
    files = ["uploads/Test1.txt", "uploads/Test2.txt"]
    await page.locator("#multipleFilesInput").set_input_files(files)
    await page.locator("button:has-text('Upload Multiple Files')").click()

    # Validation
    msg = page.locator("#multipleFilesStatus")
    await expect(msg).to_contain_text("Test1.txt")
    await expect(msg).to_contain_text("Test2.txt")

    print("✅ Multiple files uploaded successfully")

    await page.wait_for_timeout(3000)


async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()
        page = await context.new_page()

        print("Running Single File Upload Test...")
        await upload_single_file(page)

        print("Running Multiple File Upload Test...")
        await upload_multiple_files(page)

        await browser.close()


if __name__ == "__main__":
    asyncio.run(main())
