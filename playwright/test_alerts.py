import pytest
from playwright.sync_api import sync_playwright, expect, Page

@pytest.mark.skip
def test_simple_dialog(page:Page):

    page.goto("https://testautomationpractice.blogspot.com/")

    # Approach 1
    # registering an event
    def handle_dialog(dialog):
        dialog.accept()

    page.on("dialog",handle_dialog)

    page.locator("#alertBtn").click() # clicking on the button which will open dialog

    page.wait_for_timeout(5000)


@pytest.mark.skip
def test_simple_dialog2(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    # Approach 2
    page.on("dialog", lambda dialog:dialog.accept())

    page.locator("#alertBtn").click() # clicking on the button which will open dialog
    page.wait_for_timeout(5000)


@pytest.mark.skip
def test_confirmation_dialog(page: Page):

    page.goto("https://testautomationpractice.blogspot.com/")

    #page.on("dialog", lambda dialog:dialog.accept())
    page.on("dialog",lambda dialog:dialog.dismiss())
    page.wait_for_timeout(3000)

    page.locator("#confirmBtn").click() # clicking on the button which will open dialog
    page.wait_for_timeout(5000)

    text=page.locator("#demo").inner_text()
    print("Output text :=== >", text)

    #expect(page.locator("#demo")).to_have_text("You pressed OK!")
    expect(page.locator("#demo")).to_have_text("You pressed Cancel!")
    page.wait_for_timeout(3000)


def test_prompt_dialog(page: Page):

    page.goto("https://testautomationpractice.blogspot.com/")

    page.on("dialog", lambda dialog: dialog.accept('John'))
    page.locator("#promptBtn").click() # clicking on the button which will open dialog
    page.wait_for_timeout(3000)

    text=page.locator("#demo").inner_text()
    print("Output text:", text)
    expect(page.locator("#demo")).to_have_text("Hello John! How are you today?")
    page.wait_for_timeout(5000)
