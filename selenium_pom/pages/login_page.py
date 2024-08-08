from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LoginPage(BasePage):

    INPUT_USERNAME = (By.ID, "user-name")
    INPUT_PASSWORD = (By.ID, "password")
    ERROR_LOGIN = (By.CSS_SELECTOR, "div.error")
    BUTTON_LOGIN = (By.ID, "login-button")

    def open(self):
        self.driver.get("https://www.saucedemo.com/")

    def set_username(self, text):
        self.type(self.INPUT_USERNAME, text)

    def set_password(self, text):
        self.type(self.INPUT_PASSWORD, text)

    def login(self, username, password):
        self.set_username(username)
        self.set_password(password)
        self.click_login_button()

    def click_login_button(self):
        self.click(self.BUTTON_LOGIN)

    def is_login_error_message_displayed(self):
        return self.find(self.ERROR_LOGIN).is_displayed()

    def get_login_error_message(self):
        return self.get_text(self.ERROR_LOGIN)