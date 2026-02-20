import asyncio
from playwright.async_api import async_playwright, expect


async def bootstrapdropdown(page):

    # Launch URL
    await page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    # Login
    await page.locator('input[name="username"]').fill('Admin')
    await page.locator('input[name="password"]').fill('admin123')
    await page.locator('button[type="submit"]').click()
    await page.wait_for_timeout(3000)

    # Click on PIM
    await page.get_by_text('PIM').click()

    # Click dropdown
    await page.locator("form i").nth(2).click()

    # Capture all dropdown options
    options = page.locator("div[role='listbox'] span")
    await page.wait_for_timeout(3000)

    counts = await options.count()
    print("Number of options in dropdown:", counts)

    await expect(options).to_have_count(counts)

    print("All dropdown options =====>", await options.all_text_contents())

    for i in range(counts):
        print(await options.nth(i).text_content())

    # Select specific option
    for i in range(counts):
        text = await options.nth(i).inner_text()
        print("Checking option:", text)
        if text == "Finance Manager":
            print("Matching success...")
            await options.nth(i).click()
            break

    await page.wait_for_timeout(5000)


async def comparisonofmethods(page):

    await page.goto("https://demowebshop.tricentis.com/")

    products = page.locator(".product-title")

    print("Using inner_text() ===>", await products.nth(1).inner_text())
    print("Using text_content() ===>", await products.nth(1).text_content())

    count = await products.count()

    for i in range(count):
        product_name = await products.nth(i).text_content()
        print(product_name.strip())

    # all_inner_texts vs all_text_contents
    product_names = await products.all_inner_texts()
    print("All inner texts:", product_names)

    trimmed = [text.strip() for text in product_names]
    print("Trimmed:", trimmed)

    # all()
    product_locators = await products.all()

    for loc in product_locators:
        print(await loc.inner_text())


async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False, slow_mo=500)
        context = await browser.new_context()
        page = await context.new_page()

        print("Running dropdown test...")
        await bootstrapdropdown(page)

        print("Running text comparison test...")
        await comparisonofmethods(page)

        await browser.close()


if __name__ == "__main__":
    asyncio.run(main())
