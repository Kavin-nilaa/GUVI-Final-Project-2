import pytest
import os
from datetime import datetime
from driver_setup import get_driver
from Utils.excel_util import write_test_result

TEST_CASE_FILE = "Final Project 2 Test Case.xlsx"
TEST_CASE_SHEET = "Sheet1"

def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome",
        help="Browser Options: Chrome, Safari, Firefox, Edge"
    )

@pytest.fixture
def driver(request):
    browser = request.config.getoption("--browser")
    driver = get_driver(browser)
    yield driver
    screenshot_dir = os.path.join("reports", "screenshots")
    os.makedirs(screenshot_dir, exist_ok=True)
    screenshot_name = f"{request.node.name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
    driver.save_screenshot(os.path.join(screenshot_dir, screenshot_name))
    driver.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call":
        # Extract test case ID from function name
        parts = item.name.split("_")
        test_case_id = parts[1].upper() if len(parts) > 1 else item.name.upper()

        # Decide result based on pytest outcome
        result = "Passed" if report.passed else "Failed"

        # Update Excel
        write_test_result(TEST_CASE_FILE, TEST_CASE_SHEET, test_case_id, result)
