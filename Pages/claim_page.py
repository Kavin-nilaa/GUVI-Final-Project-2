from selenium.webdriver.common.by import By

from Pages.base_page import BasePage

class ClaimPage(BasePage):
    claim = (By.XPATH,"//span[text()='Claim']")
    submit_claim =(By.XPATH,"//a[text()='Submit Claim']")
    event = (By.XPATH,"(//div[text()='-- Select --'])[1]")
    event_selection = (By.XPATH,"//div[normalize-space()='Medical Reimbursement']")
    currency = (By.XPATH,"(//i[contains(@class,'oxd-select-text--arrow')])[2]")
    currency_selection = (By.XPATH,"//*[normalize-space()='Indian Rupee']")
    remarks = (By.CSS_SELECTOR,".oxd-textarea.oxd-textarea--active.oxd-textarea--resize-vertical")
    create_button = (By.XPATH,"//button[@type='submit']")

    def click_claim(self):
        self.click_element(self.claim)
        self.click_element(self.submit_claim)

    def select_event(self):
        self.click_element(self.event)
        self.click_element(self.event_selection)

    def select_currency(self):
        self.click_element(self.currency)
        self.click_element(self.currency_selection)

    def enter_remarks(self,remarks):
        self.enter_text(self.remarks,remarks)

    def click_create(self):
        self.click_element(self.create_button)


