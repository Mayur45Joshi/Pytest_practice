import pytest
from playwright.sync_api import sync_playwright, expect, Page

def test_single_select_dropdown(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    # 3 ways to select option from the dropdown
    #page.locator("#country").select_option("India") # by label
    page.locator("#country").select_option(label="India") # by label

    #page.locator("#country").select_option("germany") #by valve
    #page.locator("#country").select_option(value="germany") # by value

    page.locator("#country").select_option(index=3) # by index # index starts from 0

    # check number of options in dropdown
    dropdown_options = page.locator("#country>option")
    expect(dropdown_options).to_have_count(10)

    options_text = [text.strip() for text in dropdown_options.all_text_contents()]
    print(options_text)

    # print countries using loop
    for option in options_text:
        print(option)

    page.wait_for_timeout(5000)



def test_multi_select_dropdown(page: Page):

    page.goto("https://testautomationpractice.blogspot.com/")

    # select multiple options from teh dropdown - 3 ways

    page. locator("#colors").select_option(["Red","Blue","Green"]) # by label
    page.locator("#colors").select_option(label=["Red", "Blue", "Green"]) # by label

    #page.locator("#colors").select_option(value=["red", "white","green"]) # by values
    page.locator("#colors").select_option(index=[4,2])

    drowpdown_options = page.locator("#colors>option")
    expect(drowpdown_options).to_have_count(7)

    page.wait_for_timeout(5000)



def test_single_select_dropdown_sort(page: Page):

    page.goto("https://testautomationpractice.blogspot.com/")

    dropdown_options=page.locator("#animals>option") # sorted list
    #dropdown_options=page.locator("#colors>option")

    options_text=[text.strip() for text in dropdown_options.all_text_contents()]

    original_list=options_text.copy()
    sorted_list= sorted(options_text)

    print("Original list:",original_list)
    print("Sorted list:",sorted_list)

    if original_list == sorted_list:
        print("dropdown options are sorted order ... ")
    else:
        print("dropdown options are Not sorted order.")

    page.wait_for_timeout(5000)