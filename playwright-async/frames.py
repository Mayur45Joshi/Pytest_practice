import asyncio
from playwright.async_api import async_playwright, expect


async def frames(page):

    await page.goto("https://ui.vision/demo/webtest/frames/")

    frames = page.frames
    print("Number of frames on a page:", len(frames))

    # frame 1
    frame1 = page.frame(url="https://ui.vision/demo/webtest/frames/frame_1.html")

    inputbox = frame1.locator("input[name='mytext1']")
    await inputbox.fill("Welcome")

    await expect(inputbox).to_have_value("Welcome")


async def inner_frames(page):

    await page.goto("https://ui.vision/demo/webtest/frames/")

    # frame 3
    frame3 = page.frame(url="https://ui.vision/demo/webtest/frames/frame_3.html")

    await frame3.locator("input[name='mytext3']").fill("Welcome")

    child_frames = frame3.child_frames
    print("Number of child frames inside frame 3:", len(child_frames))

    innerframe = child_frames[0]

    radio = innerframe.get_by_label("I am a human")
    await radio.check()

    await expect(radio).to_be_checked()


async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False, slow_mo=500)
        context = await browser.new_context()
        page = await context.new_page()

        print("Running test_frames")
        await frames(page)

        print("Running test_inner_frames")
        await inner_frames(page)

        await browser.close()


if __name__ == "__main__":
    asyncio.run(main())
