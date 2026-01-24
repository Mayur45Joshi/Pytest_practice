from playwright.sync_api import sync_playwright, expect, Page
import pytest


def test_keyboardactions (page: Page):

    page. goto("https://testautomationpractice.blogspot.com/")
    input1=page.locator("#input1")

    #1. focus on input1
    input1.focus()

    #2. provide the text in input1
    page.keyboard.insert_text("welcome")

    #3 . ctrZ+A
    page.keyboard.press("Control+A")

    #4 ctrl + C
    page.keyboard.press("Control+C")

    # S. press Tab key 2 times to navigte/focus on imput2
    page.keyboard.press("Tab")
    page.keyboard.press("Tab")

    #6. Ctrl +V - Paste the text inside the 2nd inputbox - input2
    page.keyboard.press("Control+V")

    # 7. press Tab key 2 times to navigte/focus on input3
    page.keyboard.press("Tab")
    page.keyboard.press("Tab")

    # 8. Ctrl +V - Paste the text inside the 3nd inputbox - input3
    page.keyboard.press("Control+V")

    input2 = page.locator("#input2")
    input3 = page.locator("#input3")

    expect(input2).to_have_value("welcome")
    expect(input3).to_have_value("welcome")

    page.wait_for_timeout(5000)


    