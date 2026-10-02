
import time

from Pages.admin_page import AdminPage
from Pages.login_page import LoginPage

def test_tc005_verify_new_user_login(driver):
    login = LoginPage(driver)
    admin = AdminPage(driver)

    login.open_login_page()
    login.login('Admin', 'admin123')

    assert "orangehrmlive.com" in admin.get_current_url()

    admin.click_admin()
    admin.click_add_option()
    admin.click_user_role()
    admin.enter_employee_name("Ranga Akunuri")
    admin.select_status()
    admin.enter_username("Mickey")
    admin.enter_password("ASDZXCasdzxc@123")
    admin.confirm_password("ASDZXCasdzxc@123")
    admin.click_save()

    login.click_logout()
    login.login("Mickey", "ASDZXCasdzxc@123")
    assert "opensource-demo" in driver.current_url.lower()

def test_tc006_verify_newly_created_user(driver):
    admin = AdminPage(driver)
    login = LoginPage(driver)
    login.open_login_page()
    login.login('Mickey', 'ASDZXCasdzxc@123')
    admin.click_admin()
    admin.search_username("Mickey")
    time.sleep(3)
    admin.click_search_button()
    time.sleep(3)
    admin.is_user_exist()
    print("New user login is displayed")


















