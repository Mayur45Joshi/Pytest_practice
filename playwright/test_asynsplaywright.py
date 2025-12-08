import pytest
from playwright.async_api import async_playwright,Page, expect


@pytest.mark.asyncio
async def test_verifyPageUrl():
    async with async_playwright() as p:
        browser=await p.chromium. launch(headless=False)
        mypage=await browser.new_page()

        # myurl=mypage.url
        # print("Url of the application:", myurl)
        await mypage.goto("http://www.automationpractice.pl/index.php")
        await expect(mypage).to_have_url("http://www.automationpractice.pl/index.php")