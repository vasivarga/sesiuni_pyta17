import random
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By

TEXTS_ARE_NOT_MATCHING = "Unexpected result text"


class TestAlerts(unittest.TestCase):

    BUTTON_JS_ALERT = (By.XPATH, "//button[text()='Click for JS Alert']")
    BUTTON_JS_CONFIRM = (By.CSS_SELECTOR, "[onclick='jsConfirm()']")
    BUTTON_JS_PROMPT = (By.CSS_SELECTOR, "[onclick='jsPrompt()']")

    P_RESULT = (By.ID, "result")

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://the-internet.herokuapp.com/javascript_alerts")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def click(self, tuplu):
        self.driver.find_element(*tuplu).click()

    def get_text(self, tuplu):
        return self.driver.find_element(*tuplu).text

    def test_accept_simple_alert(self):
        self.click(self.BUTTON_JS_ALERT)

        alert = self.driver.switch_to.alert
        alert.accept()

        expected = "You successfully clicked an alert"
        actual = self.get_text(self.P_RESULT)

        # assert expected == actual, "Texts are not matching"
        self.assertEqual(expected, actual, TEXTS_ARE_NOT_MATCHING)

    def test_accept_confirm_alert(self):
        self.click(self.BUTTON_JS_CONFIRM)

        alert = self.driver.switch_to.alert
        alert.accept()

        expected = "You clicked: Ok"
        actual = self.get_text(self.P_RESULT)

        self.assertEqual(expected, actual, TEXTS_ARE_NOT_MATCHING)


    def test_cancel_confirm_alert(self):
        self.click(self.BUTTON_JS_CONFIRM)

        alert = self.driver.switch_to.alert
        alert.dismiss()

        expected = "You clicked: Cancel"
        actual = self.get_text(self.P_RESULT)

        self.assertEqual(expected, actual, TEXTS_ARE_NOT_MATCHING)

    def test_accept_prompt_alert_with_text(self):
        self.click(self.BUTTON_JS_PROMPT)

        alert = self.driver.switch_to.alert

        text_to_send = "Testam inputul de la alerta " + str(random.randint(0, 9999999999999))

        alert.send_keys(text_to_send)
        alert.accept()

        expected = "You entered: " + text_to_send
        actual = self.get_text(self.P_RESULT)

        self.assertEqual(expected, actual, TEXTS_ARE_NOT_MATCHING)

    def test_cancel_prompt_alert_without_text(self):
        self.click(self.BUTTON_JS_PROMPT)

        alert = self.driver.switch_to.alert
        alert.dismiss()

        expected = "You entered: null"
        actual = self.get_text(self.P_RESULT)

        self.assertEqual(expected, actual, TEXTS_ARE_NOT_MATCHING)