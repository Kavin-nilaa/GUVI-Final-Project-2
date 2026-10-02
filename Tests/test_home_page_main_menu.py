import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Pages.claim_page import ClaimPage
from Pages.home_page import HomePage
from Pages.leave_page import LeavePage
from Pages.login_page import LoginPage
from Pages.myinfo_page import MyInfoPage


def test_tc004_verify_main_menu_visibility_clickability(driver):
    login = LoginPage(driver)
    home = HomePage(driver)

    login.open_login_page()
    login.login('Admin','admin123')

    assert "orangehrmlive.com" in home.get_current_url()

    assert home.is_admin_visible()
    home.click_element(home.admin)
    assert 'admin' in home.get_current_url()
    print("Verified Admin")

    assert home.is_pim_visible()
    home.click_element(home.PIM)
    assert 'pim' in home.get_current_url()
    print("Verified PIM")

    assert home.is_leave_visible()
    home.click_element(home.leave)
    assert 'viewLeaveList' in home.get_current_url()
    print("Verified Leave")

    assert home.is_time_visible()
    home.click_element(home.time)
    assert "viewEmployeeTimesheet" in home.get_current_url()
    print("Verified Time")

    assert home.is_recruitment_visible()
    home.click_element(home.recruitment)
    assert "recruitment" in home.get_current_url()
    print("Verified Recruitment")

    assert home.is_my_info_visible()
    home.click_element(home.my_info)
    assert "viewPersonalDetails" in home.get_current_url()
    print("Verified My Info")

    assert home.is_performance_visible()
    home.click_element(home.performance)
    assert "searchEvaluatePerformanceReview" in home.get_current_url()
    print("Verified Performance")

    assert home.is_dashboard_visible()
    home.click_element(home.dashboard)
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(home.dashboard))
    assert "dashboard" in home.get_current_url()
    print("Verified Dashboard")

def test_tc008_verify_myinfo_visibility_clickability(driver):
    login = LoginPage(driver)
    #home = HomePage(driver)
    myinfo = MyInfoPage(driver)

    login.open_login_page()
    login.login('Admin','admin123')

    myinfo.is_myinfo_visible()
    myinfo.is_my_info_clickable()
    assert "viewPersonalDetails" in myinfo.get_current_url()

    myinfo.is_personal_details_visible()
    myinfo.is_personal_details_clickable()
    assert "viewPersonalDetails" in myinfo.get_current_url()

    myinfo.is_contact_details_visible()
    myinfo.is_contact_details_clickable()
    assert "contactDetails" in myinfo.get_current_url()

    myinfo.is_emergency_contacts_visible()
    myinfo.is_emergency_contacts_clickable()
    assert "viewEmergencyContacts" in myinfo.get_current_url()

    myinfo.is_dependents_visible()
    myinfo.is_dependents_clickable()
    assert "viewDependents" in myinfo.get_current_url()

def test_tc009_verify_assign_leave(driver):
    login = LoginPage(driver)
    leave = LeavePage(driver)
    login.open_login_page()
    login.login('Admin','admin123')

    leave.click_leave()
    leave.click_assign_leave()
    leave.enter_employee_name("Charlotte Smith")
    leave.select_leave_type()
    leave.enter_from_date("2026-01-01")
    leave.enter_to_date("2026-01-02")
    leave.select_partial()
    leave.select_duration()
    leave.enter_comments("Enjoy Your Leave!")
    leave.click_assign()
    leave.is_confirm_popup_displayed()
    leave.click_ok()

def test_tc010_verify_claim_submission(driver):
    login = LoginPage(driver)
    claim = ClaimPage(driver)
    login.open_login_page()
    login.login('Admin','admin123')

    claim.click_claim()
    claim.select_event()
    claim.select_currency()
    time.sleep(3)
    claim.enter_remarks("Submitting new claim")
    time.sleep(3)
    claim.click_create()
    time.sleep(3)














