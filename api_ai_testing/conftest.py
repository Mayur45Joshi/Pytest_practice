import allure
import pytest
from gemini_ai import analyze_report

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        error = report.longreprtext

        ai_analysis = analyze_report(error)

        allure.attach(
            ai_analysis,
            name="Gemini AI Failure Analysis",
            attachment_type=allure.attachment_type.TEXT
        )
