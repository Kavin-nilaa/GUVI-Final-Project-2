import pytest
from Pages.login_page import LoginPage
from Utils.excel_util import open_excel_file


TEST_DATA_FILE = "Final Project 2 Test Data.xlsx"
TEST_DATA_SHEET = "Sheet1"

test_data = open_excel_file(TEST_DATA_FILE,TEST_DATA_SHEET)

@pytest.mark.parametrize("username,password,expected",test_data)

def test_tc001_verify_login_credentials(driver,username,password,expected):
    login = LoginPage(driver)
    login.open_login_page()
    login.enter_credentials(username,password)
    login.click_login()

    if expected == "Pass":
        assert "OrangeHRM" in driver.title
        login.click_logout()
        print(f"Login/Logout successful for {username}")
    else:
        error = login.get_text(login.invalid_message)
        assert "Invalid" in error
        print(f" Login failed as expected for {username}")

def test_tc002_verify_home_url(driver):
    login = LoginPage(driver)
    login.open_login_page()
    assert "OrangeHRM" in driver.title
    print(driver.title)
    print("Home page URL is valid")

def test_tc003_verify_presence_of_login_page(driver):
    login = LoginPage(driver)
    login.open_login_page()
    assert login.is_element_displayed( login.username_field)
    assert login.is_element_displayed( login.password_field)
    print("Both username and password fields are displayed")

def test_tc007_verify_forget_password(driver):
    login = LoginPage(driver)
    login.open_login_page()
    login.verify_forget_password("Admin")








