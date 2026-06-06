import pytest
import allure
from selenium import webdriver
from gemini_client import get_ai_analysis  # Import your AI function

@pytest.fixture(scope="function")
def driver():
    """Fixture to initialize and quit the browser for each test."""
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless") # Optional: run without opening window
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(5)
    yield driver
    driver.quit()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Hook to capture failure details and attach AI analysis to Allure."""
    outcome = yield
    report = outcome.get_result()

    # Only run analysis when the test actually fails during the 'call' phase
    if report.when == "call" and report.failed:
        # 1. Capture error logs from the test
        error_details = report.longreprtext

        # 2. Get AI Analysis from Gemini
        print(f"\n Analyzing failure for {item.name}...")
        ai_analysis = get_ai_analysis(error_details)

        # 3. Attach the AI analysis text to the Allure report
        allure.attach(
            ai_analysis,
            name="Gemini AI Root Cause Analysis",
            attachment_type=allure.attachment_type.TEXT
        )

        # 4. Optional: Attach a screenshot to help the AI (if driver is available)
        if "driver" in item.fixturenames:
            web_driver = item.funcargs['driver']
            allure.attach(
                web_driver.get_screenshot_as_png(),
                name="Failure Screenshot",
                attachment_type=allure.attachment_type.PNG
            )