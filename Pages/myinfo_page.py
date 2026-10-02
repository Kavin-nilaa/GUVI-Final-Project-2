from Pages.base_page import BasePage
from selenium.webdriver.common.by import By

class MyInfoPage(BasePage):
    my_info = (By.XPATH, "//span[text()='My Info']")
    personal_details = (By.XPATH,"//a[text()='Personal Details']")
    contact_details = (By.XPATH,"//a[text()='Contact Details']")
    emergency_contacts =(By.XPATH,"//a[@href='/web/index.php/pim/viewEmergencyContacts/empNumber/7']")
    dependents = (By.XPATH,"//a[text()='Dependents']")

    def is_myinfo_visible(self):
        self.is_element_displayed(self.my_info)
    def is_my_info_clickable(self):
        self.click_element(self.my_info)

    def is_personal_details_visible(self):
        self.is_element_displayed(self.personal_details)
    def is_personal_details_clickable(self):
        self.click_element(self.personal_details)

    def is_contact_details_visible(self):
        self.is_element_displayed(self.contact_details)
    def is_contact_details_clickable(self):
        self.click_element(self.contact_details)

    def is_emergency_contacts_visible(self):
        self.is_element_displayed(self.emergency_contacts)
    def is_emergency_contacts_clickable(self):
        self.click_element(self.emergency_contacts)

    def is_dependents_visible(self):
        self.is_element_displayed(self.dependents)
    def is_dependents_clickable(self):
        self.click_element(self.dependents)
