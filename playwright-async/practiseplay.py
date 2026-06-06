import asyncio

from playwright.async_api import async_playwright, expect


async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False,args=["--start-maximized"])
        context = await browser.new_context()
        page= await context.new_page()

        await page.goto("https://testautomationpractice.blogspot.com/")
        await page.get_by_placeholder("Enter Name").fill("mayur")
        await page.locator("input#male").check()
        await page.get_by_label("Sunday").check()

        await page.locator("select#country").select_option("Canada")
        await page.locator("select#colors").select_option("White")

        #date picker clander 1
        await page.locator("//input[@id='datepicker']").click()
        target_month = "July"
        target_year="2026"

        while True:
            current_month = await page.locator("//span[@class='ui-datepicker-month']").inner_text()
            current_year = await page.locator("//span[@class='ui-datepicker-year']").inner_text()
            if current_month==target_month and current_year==target_year:
                break
            await page.locator("//a[@title='Next']").click()

        await page.locator("//a[@data-date='19']").click()

        #date picker calnder 2
        await page.locator("//input[@id='txtDate']").click()
        await page.locator("//select[@aria-label='Select month']").select_option("Jul")
        await page.locator("//select[@aria-label='Select year']").select_option("2027")
        await page.locator("//a[@data-date='19']").click()
        #await page.wait_for_timeout(5000)

        #date picker 3
        await page.wait_for_timeout(10000)
        await page.locator("//input[@id='start-date']").fill("19-07-2027")


        #  uploading
        await page.locator("//input[@id='singleFileInput']").set_input_files(r"C:\Users\HP\Downloads\Macro Teaching formate (1).pdf")

        #dynamic button
        await page.locator("//button[@name='start']").click()
        await page.locator("//button[@name='start']").click()

        start_btn = page.locator("//button[@name='start']")
        stop_btn = page.locator("//button[@name='stop']")

        for _ in range(5):
            await start_btn.click()
            await stop_btn.wait_for()

            await stop_btn.click()
            await start_btn.wait_for()


        # ✅ Simple Alert
        async with page.expect_event("dialog") as dialog_info:
            await page.click("//button[@id='alertBtn']")

        dialog = await dialog_info.value
        #print(dialog.message)
        await dialog.accept()

        # ✅ Confirmation Alert
        async with page.expect_event("dialog") as dialog_info:
            await page.click("//button[@id='confirmBtn']")

        dialog = await dialog_info.value
        #print(dialog.message)
        await dialog.accept()


        # new tab handle

        async with context.expect_page() as page_info:
            await page.click("//button[text()='New Tab']")

        new_page=await page_info.value
        await new_page.wait_for_load_state()
        print(await new_page.title())
        await new_page.click("//a[text()='Online Training']")
        #await page.click("//button[text()='Popup Windows']")



        # multiple tab / popups on click
        pages = []
        def handle_page(p):
            pages.append(p)

        # Start listening BEFORE the click
        context.on("page", handle_page)

        # Trigger action that opens multiple windows
        await page.get_by_role("button", name="Popup Windows").click()

        # Wait until 2 windows are collected
        while len(pages) < 2:
            await asyncio.sleep(0.5)

        # Work with the new windows
        for i, p in enumerate(pages):
            await p.wait_for_load_state()
            print(f"Window {i + 1} URL:", p.url)
            print(await p.title())

        #operation on any specific window
        target_page=None
        for p in pages:
            if "Selenium" in await p.title():
                target_page=p
                break
        if target_page:
            await target_page.bring_to_front()
            await target_page.click("(//a[contains(text(),'Read more')])[1]")


        # hover

        await page.locator("//button[text()='Point Me']").hover()
        await page.click("//a[text()='Mobiles']")
        await page.dblclick("//button[text()='Copy Text']")
        text=await page.locator("//input[@id='field2']").input_value()
        print(text)


        #drag drop
        source="//div[@id='draggable']"
        target="//div[@id='droppable']"
        await page.locator(source).drag_to(page.locator(target))
        #await expect(target).to_have_text("Dropped!")
        await expect(page.locator("//div[@id='droppable']//p")).to_have_text("Dropped!")



        #combobox  scroll dropdown
        await page.locator("//input[@id='comboBox']").click()
        item = page.locator("//div[@id='dropdown']//div[text()='Item 86']")
        await item.scroll_into_view_if_needed()
        await item.click()
        await page.wait_for_timeout(5000)


        #slider handle
        slider=page.locator("//div[@id='slider-range']")
        # Get slider position
        box = await slider.bounding_box()

        #calculate center
        x = box["x"] + box["width"] / 2
        y = box["y"] + box["height"] / 2

        #move to right
        await page.mouse.move(x,y)
        await page.mouse.down()

        # Move by pixels (adjust value)
        await page.mouse.move(x+150 , y)
        await page.mouse.up()



        #broken links

        links = await page.locator("a").all()
        for link in links:
            url = await link.get_attribute("href")
            if url is None or url.startswith("javascript"):
                continue
            try:
                response = await page.request.get(url)
                status = response.status

                if status >= 400 :
                    print(f"Broken link {url} --> {status}")
                else:
                    print(f"Valid link {url} --> {status}")
            except Exception as e:
                print(f"error  {url}")


        await page.wait_for_timeout(5000)

asyncio.run(main())