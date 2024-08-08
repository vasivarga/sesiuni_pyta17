import random
import time
import unittest

from pages.login_page import LoginPage

expected_error = "Epic sadface: Username and password do not match any user in this service"


class LoginTests(unittest.TestCase):

    def setUp(self) -> None:
        self.login_page = LoginPage()
        self.login_page.open()

    def tearDown(self) -> None:
        self.login_page.close()

    def test_successful_login(self):
        self.login_page.set_username("standard_user")
        self.login_page.set_password("secret_sauce")
        self.login_page.click_login_button()

        self.assertEqual(self.login_page.get_current_url(), "https://www.saucedemo.com/inventory.html")
        # self.login_page.verify_current_url("https://www.saucedemo.com/inventory.html")

    def test_login_with_invalid_password(self):
        self.login_page.set_username("standard_user")
        self.login_page.set_password("121342435456")
        self.login_page.click_login_button()

        # assert self.login_page.is_login_error_message_displayed()
        self.assertTrue(self.login_page.is_login_error_message_displayed(), "Login error not displayed")
        actual_error = self.login_page.get_login_error_message()

        self.assertEqual(actual_error, expected_error, "Wrong error message")

    def test_login_with_locked_out_username(self):
        self.login_page.login("locked_out_user", "secret_sauce")

        actual_error = self.login_page.get_login_error_message()

        self.assertTrue(self.login_page.is_login_error_message_displayed())
        self.assertEqual(expected_error, actual_error)

    def test_login_with_invalid_username(self):
        username = f"user_{random.randint(0, 99999999999)}@gmail.com"
        self.login_page.login(username, "secret_sauce")

        actual_error = self.login_page.get_login_error_message()

        self.assertTrue(self.login_page.is_login_error_message_displayed())
        self.assertEqual(expected_error, actual_error)