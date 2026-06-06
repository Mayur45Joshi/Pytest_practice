import pytest
import json
from playwright.sync_api import sync_playwright, Page


# ── Load test data ──────────────────────────────────────────────
@pytest.fixture(scope="session")
def test_data():
    with open("test_data/login_data.json") as f:
        return json.load(f)


# ── Browser setup ────────────────────────────────────────────────
@pytest.fixture(scope="session")
def browser_instance():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        yield browser
        browser.close()


@pytest.fixture(scope="function")
def page(browser_instance) -> Page:
    """Fresh context + page per test for isolation"""
    context = browser_instance.new_context(
        viewport={"width": 1280, "height": 720}
    )
    page = context.new_page()
    yield page
    context.close()


# ── Screenshot on failure ────────────────────────────────────────
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")
        if page:
            screenshot_name = item.name.replace(" ", "_")
            page.screenshot(path=f"screenshots/{screenshot_name}.png")
            print(f"\nScreenshot saved: screenshots/{screenshot_name}.png")