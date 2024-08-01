from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LoginPage(BasePage):

    EMAIL_INPUT = (By.ID, "Email")
    PASSWORD_INPUT = (By.ID, "Password")
    LOGIN_BUTTON = (By.CLASS_NAME, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "div.message-error ul li")

    def open(self):
        self.driver.get("https://demo.nopcommerce.com/login")

    def set_email(self, text):
        self.type(self.EMAIL_INPUT, text)

    def set_password(self, text):
        self.type(self.PASSWORD_INPUT, text)

    def click_login(self):
        self.click(self.LOGIN_BUTTON)

    def verify_error_text_message(self, text):
        assert self.get_text(self.ERROR_MESSAGE) == text
