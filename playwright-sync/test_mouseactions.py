import pytest
from playwright.sync_api import sync_playwright, expect, Page

@pytest.mark.skip
def test_mouse_hover(page:Page):

    page.goto("https://testautomationpractice.blogspot.com/")

    pointme=page.locator(".dropbtn")
    pointme.hover()

    laptops=page.locator('.dropdown-content a:nth-child(2)')
    laptops.hover()

    page.wait_for_timeout(5000)

@pytest.mark.skip
def test_mouse_rightclick(page:Page):

    page.goto("http://swisnl.github.io/jQuery-contextMenu/demo.html")

    button=page.locator(".context-menu-one")
    button.click(button="right")

    page.wait_for_timeout(5000)

@pytest.mark.skip
def test_mouse_doubleclick(page:Page):

    page.goto("https://testautomationpractice.blogspot.com/")

    btncopy=page.locator("button[ondblclick='myFunction1()']")
    btncopy.dblclick() # performs double click action

    filed2=page.locator("#field2")
    expect(filed2).to_have_value("Hello World!")

    page.wait_for_timeout(5000)



def test_mouse_draganddrop(page:Page):

    page.goto("https://testautomationpractice.blogspot.com/")

    source=page.locator("#draggable")
    target=page.locator("#droppable")

    #Appraoch1 : manval drag using hover()
    # source.hover()
    # page.mouse.down()
    # target.hover()
    # page.mouse.up()

    #Appraoch 2 : drag_to()
    source.drag_to(target)

    page.wait_for_timeout(5000)