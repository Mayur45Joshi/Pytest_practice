import asyncio
from playwright.async_api import async_playwright


async def main():
    async with async_playwright() as p:
        # browser = await p.chromium.launch(headless=False)
        # context = await browser.new_context()
        # page = await context.new_page()
        # #await page.goto("https://demoqa.com/accordian")
        # await page.goto("https://demoqa.com/frames")
        # async with page.expect_popup() as popup_info:
        #     await page.locator("//button[@id='messageWindowButton']").click()
        # info = await popup_info.value
        # await info.wait_for_load_state()
        # text = await info.locator("body").text_content()
        # print(text)
        # await browser.close()




    # #modals handle
    #
    #     await page.locator("#showSmallModal").click()
    #     text = await page.locator("//div[@class='modal-body']").text_content()
    #     print(text)
    #     await page.locator("//button[@class='btn-close']").click()
    #
    #     await page.locator("#showLargeModal").click()
    #     text1 = await page.locator("//div[@class='modal-body']/p").text_content()
    #     print(text1)



        # #accordian
        #
        # await page.wait_for_timeout(50000)
        #
        # await page.locator("//button[text()='What is Lorem Ipsum?']").click()
        # text = await page.locator("(//div[@class='accordion-body'])[1]").text_content()
        # print(text)
        #
        # await page.locator("//button[text()='Where does it come from?']").click()

        # browser = await p.chromium.launch(headless=False)
        # page = await browser.new_page()
        # await page.goto("https://demoqa.com/frames")
        # #await page.wait_for_load_state("networkidle")
        # frame1 = page.frame_locator("#frame1")
        # text1 = await frame1.locator("#sampleHeading").text_content()
        # print(text1)
        # frame2 = page.frame_locator("#frame2")
        # text2 = await frame2.locator("#sampleHeading").text_content()
        # print(text2)
        # #await page.wait_for_timeout(5000)

        # parent = page.locator("//h1[text()='Frames']")
        # text3 = await parent.text_content()
        # print(text3)


        #keyboard button handle
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto("https://testautomationpractice.blogspot.com/")
        await page.locator("//input[@id='input1']").fill("mayur")


        await page.keyboard.press("Tab")

        await page.wait_for_timeout(5000)

asyncio.run(main())