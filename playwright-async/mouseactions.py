import asyncio
from playwright.async_api import async_playwright, expect


async def mouse_hover(page):
    await page.goto("https://testautomationpractice.blogspot.com/")

    pointme = page.locator(".dropbtn")
    await pointme.hover()

    laptops = page.locator(".dropdown-content a:nth-child(2)")
    await laptops.hover()

    await page.wait_for_timeout(5000)


async def mouse_rightclick(page):
    await page.goto("http://swisnl.github.io/jQuery-contextMenu/demo.html")

    button = page.locator(".context-menu-one")
    await button.click(button="right")

    await page.wait_for_timeout(5000)


async def mouse_doubleclick(page):
    await page.goto("https://testautomationpractice.blogspot.com/")

    btncopy = page.locator("button[ondblclick='myFunction1()']")
    await btncopy.dblclick()

    field2 = page.locator("#field2")
    await expect(field2).to_have_value("Hello World!")

    await page.wait_for_timeout(5000)


async def mouse_draganddrop(page):
    await page.goto("https://testautomationpractice.blogspot.com/")

    source = page.locator("#draggable")
    target = page.locator("#droppable")

    # Approach 1 – Manual Drag
    # await source.hover()
    # await page.mouse.down()
    # await target.hover()
    # await page.mouse.up()

    # Approach 2 – drag_to()
    await source.drag_to(target)

    await page.wait_for_timeout(5000)


async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False, slow_mo=500)
        context = await browser.new_context()
        page = await context.new_page()

        await mouse_hover(page)
        await mouse_rightclick(page)
        await mouse_doubleclick(page)
        await mouse_draganddrop(page)

        await browser.close()


asyncio.run(main())
