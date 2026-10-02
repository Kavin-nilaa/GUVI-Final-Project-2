from Pages.base_page import BasePage
from selenium.webdriver.common.by import By

class HomePage(BasePage):
    admin = (By.XPATH,"//span[text()='Admin']")
    PIM = (By.XPATH,"//span[text()='PIM']")
    leave = (By.XPATH,"//span[text()='Leave']")
    time = (By.XPATH,"//span[text()='Time']")
    recruitment = (By.XPATH,"//span[text()='Recruitment']")
    my_info = (By.XPATH,"//span[text()='My Info']")
    performance = (By.XPATH,"//span[text()='Performance']")
    dashboard = (By.XPATH,"//span[text()='Dashboard']")

    def is_admin_visible(self):
        return self.is_element_displayed(self.admin)
    def is_admin_clickable(self):
        return self.is_element_enabled(self.admin)

    def is_pim_visible(self):
        return self.is_element_displayed(self.PIM)
    def is_pim_clickable(self):
        return self.is_element_enabled(self.PIM)

    def is_leave_visible(self):
        return self.is_element_displayed(self.leave)
    def is_leave_clickable(self):
        return self.is_element_enabled(self.leave)

    def is_time_visible(self):
        return self.is_element_displayed(self.time)
    def is_time_clickable(self):
        return self.is_element_enabled(self.time)

    def is_recruitment_visible(self):
        return self.is_element_displayed(self.recruitment)
    def is_recruitment_clickable(self):
        return self.is_element_enabled(self.recruitment)

    def is_my_info_visible(self):
        return self.is_element_displayed(self.my_info)
    def is_my_info_clickable(self):
        return self.is_element_enabled(self.my_info)

    def is_performance_visible(self):
        return self.is_element_displayed(self.performance)
    def is_performance_clickable(self):
        return self.is_element_enabled(self.performance)

    def is_dashboard_visible(self):
        return self.is_element_displayed(self.dashboard)
    def is_dashboard_clickable(self):
        return self.is_element_enabled(self.dashboard)

