import pytest
from playwright.sync_api import Page, expect

def test_verify_css_locators(page: Page):
    page.goto("https://demowebshop.tricentis.com/")

    #tag id
    # page.Locator("input#small-searchterms").fill("T-Shirts")
    page.locator("#small-searchterms").fill("T-Shirts")
    page.wait_for_timeout (5000)


    # tag class
    page.locator("input.search-box-text").fill("T-Shirts")
    # page.locator(".search-box-text").fill("T-Shirts")
    page.wait_for_timeout(5000)


    # tag attribute
    page.locator("input[name=q]").fill("T-Shirts")
    page.locator("[name=q]").fill("7-Shirts")
    page.wait_for_timeout(5000)

    # tag class attribute
    # page. locator("input.search-box-text[value='Search store']").fill("7-Shirts")
    page.locator(".search-box-text[value='Search store' ]").fill("T-Shirts")
    page.wait_for_timeout(5000)


