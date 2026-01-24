import pytest
from playwright.sync_api import sync_playwright, expect, Page

def test_bootstrapdropdown(page : Page):
    # Launch the URL
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    # Login steps
    page.locator('input[name="username"]').fill('Admin')
    page.locator('input[name="password"]').fill('admin123')
    page.locator('button[type="submit"]').click()
    page.wait_for_timeout(3000)

    # click on PIM
    page.get_by_text('PIM').click()

    # click on the Job title dropdown
    page.locator("form i").nth(2).click()  # this will open options from the dropdown

    # capture all teh options from dropdown

    options=page.locator("div[role='listbox'] span")
    page.wait_for_timeout(3000)
    counts = options.count()
    print("Number of options in the dropdown:", counts)

    expect(options).to_have_count(counts)  # assertion for counting the options

    # Print all teh options
    print("All the options from the dropdown === >", options.all_text_contents())
    page.wait_for_timeout(3000)

    for i in range(counts):
        print(options.nth(i).text_content())

    # select/click on specific option
    for i in range(counts):
        text = options.nth(i).inner_text()
        print("option to be selected ===== >: ", text)
        if text == 'Finance Manager':
            print("Matching success ..... ")
            options.nth(i).click()
            break

    page.wait_for_timeout(5000)



# diff between inner text and text content method
def test_comparisonofmethods(page:Page):
    page.goto("https://demowebshop.tricentis.com/")

    products=page. locator(".product-title") # 6 products

    # 1) inner_text() vs text_content()

    print("Using inner_text() ==== > ",products.nth(1).inner_text())    #retrun actual text
    print("Using text_content() ==== > ",products.nth(1).text_content())    #retrun text with special char and spaces if any

    count = products.count()
    for i in range(count):
        product_name = products.nth(i).text_content()
        print(product_name.strip())

        # product_name = products.nth(i).inner_text()
        # print(product_name)


    # 2) all_inner_texts() vs all_text_contents()
    product_names=products.all_inner_texts()
    #product_names=products.all_text_contents()
    print(product_names)
    products_names_trimmed = [text.strip() for text in product_names]
    print(products_names_trimmed)

    # 3) all()
    product_locators = products.all()
    # print(product_locators[0].inner_text())

    for product_loc in product_locators:
        print(product_loc.inner_text())

    for i in range(len(product_locators)):
        print(product_locators[i].inner_text())