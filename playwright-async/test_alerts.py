import pytest
from playwright.async_api import async_playwright, expect, Page

@pytest.mark.skip
@pytest.mark.asyncio
async def test_simple_dialog(page: Page):

    await page.goto("https://testautomationpractice.blogspot.com/")

    # Approach 1
    # registering an event
    async def handle_dialog(dialog):
        await dialog.accept()

    page.on("dialog", handle_dialog)

    await page.locator("#alertBtn").click()  # clicking on the button which will open dialog

    await page.wait_for_timeout(5000)


@pytest.mark.skip
@pytest.mark.asyncio
async def test_simple_dialog2(page: Page):

    await page.goto("https://testautomationpractice.blogspot.com/")

    # Approach 2
    page.on("dialog", lambda dialog: dialog.accept())

    await page.locator("#alertBtn").click()  # clicking on the button which will open dialog

    await page.wait_for_timeout(5000)


@pytest.mark.skip
@pytest.mark.asyncio
async def test_confirmation_dialog(page: Page):

    await page.goto("https://testautomationpractice.blogspot.com/")

    # page.on("dialog", lambda dialog: dialog.accept())
    page.on("dialog", lambda dialog: dialog.dismiss())

    await page.wait_for_timeout(3000)

    await page.locator("#confirmBtn").click()  # clicking on the button which will open dialog

    await page.wait_for_timeout(5000)

    text = await page.locator("#demo").inner_text()
    print("Output text :=== >", text)

    await expect(page.locator("#demo")).to_have_text("You pressed Cancel!")

    await page.wait_for_timeout(3000)


@pytest.mark.asyncio
async def test_prompt_dialog(page: Page):

    await page.goto("https://testautomationpractice.blogspot.com/")

    page.on("dialog", lambda dialog: dialog.accept("John"))

    await page.locator("#promptBtn").click()  # clicking on the button which will open dialog

    await page.wait_for_timeout(3000)

    text = await page.locator("#demo").inner_text()
    print("Output text:", text)

    await expect(page.locator("#demo")).to_have_text("Hello John! How are you today?")

    await page.wait_for_timeout(5000)
