from selenium.webdriver.common.by import By
from Pages.base_page import BasePage

class LoginPage(BasePage):
    username_field = (By.NAME, "username")
    password_field = (By.NAME, "password")
    login_button = (By.XPATH, '//button[@type="submit"]')
    profile = (By.XPATH, "//span[@class='oxd-userdropdown-tab']")
    logout_button = (By.XPATH, "//a[contains(text(),'Logout')]")
    invalid_message = (By.XPATH,"//p[text()='Invalid credentials']")

    forgot_password = (By.XPATH,"//p[text()='Forgot your password? ']")
    username = (By.XPATH,"//input[@name='username']")
    reset_button = (By.XPATH,"//button[@type='submit']")

    def open_login_page(self):
        self.open_url("https://opensource-demo.orangehrmlive.com")

    def enter_credentials(self,username,password):
        self.enter_text(self.username_field,username)
        self.enter_text(self.password_field,password)

    def click_login(self):
        self.click_element(self.login_button)

    def login(self,username,password):
        self.enter_text(self.username_field,username)
        self.enter_text(self.password_field,password)
        self.click_element(self.login_button)

    def click_logout(self):
        self.click_element(self.profile)
        self.click_element(self.logout_button)

    def verify_forget_password(self,username):
        self.click_element(self.forgot_password)
        self.enter_text(self.username,username)
        self.click_element(self.reset_button)









