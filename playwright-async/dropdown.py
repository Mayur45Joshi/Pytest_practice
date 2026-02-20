import asyncio
from playwright.async_api import async_playwright, expect


async def single_select_dropdown(page):
    await page.goto("https://testautomationpractice.blogspot.com/")

    # By label
    await page.locator("#country").select_option(label="India")

    # By index (index starts from 0)
    await page.locator("#country").select_option(index=3)

    # Check number of options
    dropdown_options = page.locator("#country > option")
    await expect(dropdown_options).to_have_count(10)

    options_text = [text.strip() for text in await dropdown_options.all_text_contents()]
    print("Country list:", options_text)

    for option in options_text:
        print(option)

    await page.wait_for_timeout(3000)


async def multi_select_dropdown(page):
    await page.goto("https://testautomationpractice.blogspot.com/")

    # By label
    await page.locator("#colors").select_option(label=["Red", "Blue", "Green"])

    # By index
    await page.locator("#colors").select_option(index=[4, 2])

    dropdown_options = page.locator("#colors > option")
    await expect(dropdown_options).to_have_count(7)

    await page.wait_for_timeout(3000)


async def single_select_dropdown_sort(page):
    await page.goto("https://testautomationpractice.blogspot.com/")

    dropdown_options = page.locator("#animals > option")

    options_text = [text.strip() for text in await dropdown_options.all_text_contents()]

    original_list = options_text.copy()
    sorted_list = sorted(options_text)

    print("Original list:", original_list)
    print("Sorted list:", sorted_list)

    if original_list == sorted_list:
        print("Dropdown is in sorted order")
    else:
        print("Dropdown is NOT sorted")

    await page.wait_for_timeout(3000)


async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False, slow_mo=300)
        context = await browser.new_context()
        page = await context.new_page()

        print("Running Single Select Dropdown Test")
        await single_select_dropdown(page)

        print("Running Multi Select Dropdown Test")
        await multi_select_dropdown(page)

        print("Running Dropdown Sorting Validation Test")
        await single_select_dropdown_sort(page)

        await browser.close()


if __name__ == "__main__":
    asyncio.run(main())
