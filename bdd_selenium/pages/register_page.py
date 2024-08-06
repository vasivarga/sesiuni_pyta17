from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class RegisterPage(BasePage):

    ERROR_FIRST_NAME = (By.ID, "FirstName-error")
    ERROR_LAST_NAME = (By.ID, "LastName-error")
    ERROR_EMAIL = (By.ID, "Email-error")
    ERROR_PASSWORD = (By.ID, "ConfirmPassword-error")
    BUTTON_REGISTER = (By.ID, "register-button")

    INPUT_FIRST_NAME = (By.ID, "FirstName")
    INPUT_LAST_NAME = (By.ID, "LastName")
    DROPDOWN_DAY = (By.NAME, "DateOfBirthDay")
    DROPDOWN_MONTH = (By.NAME, "DateOfBirthMonth")
    DROPDOWN_YEAR = (By.NAME, "DateOfBirthYear")
    INPUT_EMAIL = (By.ID, "Email")
    INPUT_PASSWORD = (By.ID, "Password")
    INPUT_PASSWORD_CONFIRM = (By.ID, "ConfirmPassword")
    ERROR_PASS_VALIDATION = (By.CSS_SELECTOR, "[data-valmsg-for='Password']")

    def open(self):
        self.driver.get("https://demo.nopcommerce.com/register")

    def click_register_button(self):
        self.click(self.BUTTON_REGISTER)

    def verify_first_name_mandatory_error(self, expected_text):
        assert self.get_text(self.ERROR_FIRST_NAME) == expected_text

    def verify_last_name_mandatory_error(self, expected_text):
        assert self.get_text(self.ERROR_LAST_NAME) == expected_text

    def verify_email_mandatory_error(self, expected_text):
        assert self.get_text(self.ERROR_EMAIL) == expected_text

    def verify_password_mandatory_error(self, expected_text):
        assert self.get_text(self.ERROR_PASSWORD) == expected_text

    def set_first_name(self, name):
        self.type(self.INPUT_FIRST_NAME, name)

    def set_last_name(self, name):
        self.type(self.INPUT_LAST_NAME, name)

    def select_day_of_birth(self, day):
        self.select_dropdown_text(self.DROPDOWN_DAY, day)

    def select_month_of_birth(self, month):
        self.select_dropdown_text(self.DROPDOWN_MONTH, month)

    def select_year_of_birth(self, year):
        self.select_dropdown_text(self.DROPDOWN_YEAR, year)

    def set_email(self, email):
        self.type(self.INPUT_EMAIL, email)

    def set_password(self, password):
        self.type(self.INPUT_PASSWORD, password)

    def set_password_confirm(self, pass_confirm):
        self.type(self.INPUT_PASSWORD_CONFIRM, pass_confirm)

    def verify_pass_validation_text_contains(self, expected_text):
        assert expected_text in self.get_text(self.ERROR_PASS_VALIDATION), f"'{expected_text}' not found on element"