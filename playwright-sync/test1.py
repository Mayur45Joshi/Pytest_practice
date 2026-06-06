from playwright.sync_api import sync_playwright

def check_center():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://www.cvshealth.com/")

        # Locate the text element
        element = page.locator("text=Building a world of health around every individual")

        # Wait for element
        element.wait_for()

        # Get bounding box of element
        box = element.bounding_box()

        # Get viewport size
        viewport = page.viewport_size

        # Calculate centers
        element_center_x = box["x"] + box["width"] / 2
        viewport_center_x = viewport["width"] / 2

        print(f"Element center X: {element_center_x}")
        print(f"Viewport center X: {viewport_center_x}")

        # Check if centered (allow small tolerance)
        if abs(element_center_x - viewport_center_x) < 5:
            print("✅ Element is horizontally centered")
        else:
            print("❌ Element is NOT centered")

        browser.close()

check_center()