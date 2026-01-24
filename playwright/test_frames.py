import pytest
from playwright.sync_api import sync_playwright, expect, Page


@pytest.mark.skip
def test_frames(page: Page):

    page.goto("https://ui.vision/demo/webtest/frames/")
    frames=page.frames
    print("Number of frames on a page:", len(frames)) # 7

    # frame 1
    #frame1=page.frame("name of the frame") # options 3: get the frame using name ( We cannot use here since we do
    #frame1=page.frame_locator("frame[src='frame_1.html']") # option 1: get the frame using css
    frame1= page.frame(url='https://ui.vision/demo/webtest/frames/frame_1.html') # option 2: get the frame using url
    inputbox=frame1.locator("input[name='mytext1']")
    inputbox.fill("Welcome")

    expect(inputbox).to_have_value("Welcome")

    page.wait_for_timeout(5000)



import pytest
from playwright.sync_api import sync_playwright, expect, Page

def test_inner_frames(page: Page):
    page.goto("https://ui.vision/demo/webtest/frames/")

    # frame 3
    #frame3=page.frame_locator("frame[src='frame_3.html' ]") # grap teh frame 3
    frame3 = page.frame(url="https://ui.vision/demo/webtest/frames/frame_3.html") # grap teh frame 3

    frame3.locator("input[name='mytext3' ]"). fill("Welcome") # get teh inputbox from frame 3 and provide teh text

    child_frames=frame3.child_frames
    print("Number of child frames inside teh frame 3: ", len(child_frames))

    innerframe=child_frames[0]

    radio=innerframe.get_by_label("I am a human")
    radio.check()
    expect(radio).to_be_checked()

    page.wait_for_timeout(5000)