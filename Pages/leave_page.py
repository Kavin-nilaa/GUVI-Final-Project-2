from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pages.base_page import BasePage
from selenium.webdriver.common.by import By

class LeavePage(BasePage):
    leave = (By.XPATH, "//span[text()='Leave']")
    assign_leave = (By.XPATH,"//a[text()='Assign Leave']")
    employee_name = (By.XPATH,"//input[@placeholder='Type for hints...']")
    employee_name_suggestion = (By.XPATH, "//div[@role='listbox']//span")
    leave_type = (By.XPATH, "(//div[@class='oxd-select-text--after'])[1]")
    leave_option = (By.XPATH, "//div[normalize-space()='CAN - Personal']")
    from_date = (By.XPATH, "(//input[@placeholder='yyyy-dd-mm'])[1]")
    to_date = (By.XPATH, "(//input[@placeholder='yyyy-dd-mm'])[2]")
    partial_days = (By.XPATH,
                    "//label[contains(text(),'Partial Days')]/following::div[@class='oxd-select-text-input'][1]")
    partial_options = (By.XPATH, "//span[normalize-space()='All Days']")
    duration = (By.XPATH, "(//div[@class='oxd-select-text--after'])[3]")
    duration_options = (By.XPATH, "//div[normalize-space()='Half Day - Morning']")
    comments = (By.XPATH, "//textarea[contains(@class,'oxd-textarea')]")
    assign_button = (By.XPATH, "//button[@type='submit']")
    confirm_popup = (By.XPATH, "//div[@role='document']")
    confirm_ok = (By.XPATH, "//button[normalize-space()='Ok']")

    def click_leave(self):
        self.click_element(self.leave)

    def click_assign_leave(self):
        self.click_element(self.assign_leave)

    def enter_employee_name(self, employee_name):
        self.enter_text(self.employee_name, employee_name)
        self.click_element(self.employee_name_suggestion)

    def select_leave_type(self):
        self.click_element(self.leave_type)
        self.click_element(self.leave_option)

    def enter_from_date(self, from_date):
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.from_date))
        element.click()
        element.send_keys(from_date)
        element.send_keys(Keys.TAB)

    def enter_to_date(self, to_date):
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.to_date))
        # ActionChains(self.driver).move_to_element(element).click().send_keys(to_date).perform()

        element.click()
        element.send_keys(Keys.COMMAND, "a")
        element.send_keys(Keys.DELETE)
        element.send_keys(to_date)
        element.send_keys(Keys.TAB)

    def select_partial(self):
        self.click_element(self.partial_days)
        self.click_element(self.partial_options)

    def select_duration(self):
        self.click_element(self.duration)
        self.click_element(self.duration_options)

    def enter_comments(self, comments):
        self.enter_text(self.comments, comments)

    def click_assign(self):
        self.click_element(self.assign_button)

    def is_confirm_popup_displayed(self):
        return self.is_element_displayed(self.confirm_popup)

    def click_ok(self):
        self.click_element(self.confirm_ok)