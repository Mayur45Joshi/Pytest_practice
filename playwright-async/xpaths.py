import asyncio
import re
from playwright.async_api import async_playwright, expect


async def verify_xpath_locators(page):

    await page.goto("https://demowebshop.tricentis.com/")

    # 1. Absolute xpath (Not recommended)
    logo = page.locator("//html/body/div[4]/div[1]/div[1]/div[1]/a/img")
    await expect(logo).to_be_visible()

    # 2. Relative xpath
    await expect(page.locator("//img[@alt='Tricentis Demo Web Shop']")).to_be_visible()
    await page.wait_for_timeout(5000)

    # 3. xpath with contains()
    products = page.locator("//h2//a[contains(@href,'computer')]")
    products_count = await products.count()
    print("Products count:", products_count)
    await expect(products).to_have_count(products_count)

    print("First computer product:", await products.first.text_content())
    print("Last computer product:", await products.last.text_content())
    print("N-th computer product:", await products.nth(3).text_content())

    product_titles = await products.all_text_contents()
    print("Product titles --- >:", product_titles)

    print("Printing product tiles using looping statement...........")
    for i in product_titles:
        print(i)

    # xpath with starts-with
    building_products = page.locator("//h2//a[starts-with(@href,'/build')]")
    count = await building_products.count()
    print("Count of building products:", count)
    await expect(building_products).to_have_count(count)

    # xpath with text()
    registration_link = page.locator("//a[text()='Register']")
    await expect(registration_link).to_be_visible()

    # xpath with last()
    googlepluslink = page.locator("//div[@class='column follow-us']//li[last()]")
    await expect(googlepluslink).to_have_text("Google+")

    # xpath with position()
    twitterlink = page.locator("//div[@class='column follow-us']//li[position()=2]")
    await expect(twitterlink).to_have_text("Twitter")


async def handle_dynamic_elements(page):
    await page.goto("https://testautomationpractice.blogspot.com/")

    for _ in range(5):
        button = page.locator("//button[text()='START' or text()='STOP']")
        await button.click()
        await page.wait_for_timeout(2000)


async def handle_dynamic_elements_css(page):
    await page.goto("https://testautomationpractice.blogspot.com/")

    for _ in range(5):
        button = page.locator("button[name^='st']")
        await button.click()
        await page.wait_for_timeout(2000)


async def handle_dynamic_elements_role(page):
    await page.goto("https://testautomationpractice.blogspot.com/")

    for _ in range(5):
        button = page.get_by_role("button", name=re.compile(r"ST.*"))
        await button.click()
        await page.wait_for_timeout(2000)


async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False, slow_mo=300)
        context = await browser.new_context()
        page = await context.new_page()

        await verify_xpath_locators(page)
        await handle_dynamic_elements(page)
        await handle_dynamic_elements_css(page)
        await handle_dynamic_elements_role(page)

        await browser.close()


if __name__ == "__main__":
    asyncio.run(main())
