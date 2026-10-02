from selenium.webdriver.common.by import By

from Pages.base_page import BasePage

class AdminPage(BasePage):
    admin = (By.XPATH, "//span[text()='Admin']")
    ADD = (By.XPATH,"//button[normalize-space()='Add']")
    USER_ROLE = (By.XPATH, "(//div[contains(@class,'oxd-select-text')])[1]")
    ESS_OPTION = (By.XPATH, "//div[normalize-space()='ESS']")
    EMPLOYEE_NAME = (By.XPATH, "//input[@placeholder='Type for hints...']")
    EMPLOYEE_NAME_SUGGESTION = (By.XPATH, "//div[@role='listbox']//span")
    STATUS = (By.XPATH, "(//div[contains(@class,'oxd-select-text')])[4]")
    STATUS_OPTION = (By.XPATH, "//div[normalize-space()='Enabled']")
    USERNAME = (By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[2]")
    PASSWORD = (By.XPATH, "(//input[@type='password'])[1]")
    CONFIRM_PASS = (By.XPATH, "(//input[@type='password'])[2]")
    SAVE = (By.XPATH, "//button[@type='submit']")
    SEARCH_USER = (By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[2]")
    SEARCH_BUTTON = (By.XPATH, "//button[@type='submit']")
    SEARCH_RESULT = (By.XPATH, "//div[text()='Admin123']")

    def click_admin(self):
        self.click_element(self.admin)

    def click_add_option(self):
        self.click_element(self.ADD)

    def click_user_role(self):
        self.click_element(self.USER_ROLE)
        self.click_element(self.ESS_OPTION)

    def enter_employee_name(self,employee_name):
        self.enter_text(self.EMPLOYEE_NAME, employee_name)
        self.click_element(self.EMPLOYEE_NAME_SUGGESTION)

    def select_status(self,):
        self.click_element(self.STATUS)
        self.click_element(self.STATUS_OPTION)

    def enter_username(self,username):
        self.enter_text(self.USERNAME,username)

    def enter_password(self,password):
        self.enter_text(self.PASSWORD,password)

    def confirm_password(self,enter_password):
        self.enter_text(self.CONFIRM_PASS,enter_password)

    def click_save(self):
        self.click_element(self.SAVE)

    def click_search_button(self):
        self.click_element(self.SEARCH_BUTTON)

    def search_username(self,username):
        self.enter_text(self.SEARCH_USER,username)

    def is_user_exist(self):
        self.is_element_displayed(self.SEARCH_RESULT)










