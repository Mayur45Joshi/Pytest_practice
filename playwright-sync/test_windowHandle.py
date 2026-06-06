from playwright.sync_api import sync_playwright
import pytest

def test_handle_windows():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        page.goto("https://demoqa.com/browser-windows")

        # -----------------------------
        # 1. HANDLE NEW TAB
        # -----------------------------
        print("----- Handling New Tab -----")

        with context.expect_page() as new_tab_info:
            page.click("#tabButton")

        new_tab = new_tab_info.value
        new_tab.wait_for_load_state()

        new_tab_title = new_tab.title()
        print("New Tab Title:", new_tab_title)

        assert new_tab_title is not None

        # -----------------------------
        # 2. HANDLE NEW WINDOW
        # -----------------------------
        print("----- Handling New Window -----")

        with context.expect_page() as new_window_info:
            page.click("#windowButton")

        new_window = new_window_info.value
        new_window.wait_for_load_state()

        new_window_title = new_window.title()
        print("New Window Title:", new_window_title)

        assert new_window_title is not None

        # -----------------------------
        # 3. HANDLE MESSAGE WINDOW
        # -----------------------------
        print("----- Handling Message Window -----")

        with context.expect_page() as message_window_info:
            page.click("#messageWindowButton")

        message_window = message_window_info.value
        message_window.wait_for_load_state()

        message_title = message_window.title()
        print("Message Window Title:", message_title)

        # No strict assert (title may be empty)

        # -----------------------------
        # 4. SWITCH BACK TO PARENT
        # -----------------------------
        page.bring_to_front()
        parent_title = page.title()

        print("Parent Title:", parent_title)
        assert parent_title is not None

        browser.close()