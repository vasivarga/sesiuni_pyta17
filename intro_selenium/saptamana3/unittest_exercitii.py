# Implementează o clasă TestLogin care să moștenească unittest.TestCase
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestLogin(unittest.TestCase):

    # - Metoda setUp():
    # - Driver
    # open https://the-internet.herokuapp.com/
    # Click pe Form Authentication
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get("https://the-internet.herokuapp.com/")
        self.driver.find_element(By.LINK_TEXT, "Form Authentication").click()

    # - tearDown():
    # Quit browser
    def tearDown(self):
        self.driver.quit()

    # ● Test 1
    # - Verifică dacă noul url e corect
    def test_url_is_correct(self):
        expected_url = "https://the-internet.herokuapp.com/login"
        actual_url = self.driver.current_url

        # assert expected_url == actual_url, "Unexpected URL"
        self.assertEqual(expected_url, actual_url, "Unexpected URL")

    # ● Test 2
    # - Verifică dacă page title e corect
    def test_page_title_is_correct(self):
        expected_title = "The Internet"
        actual_title = self.driver.title

        self.assertEqual(expected_title, actual_title, "Unexpected title")

    # ● Test 3
    # - Verifică textul de pe elementul xpath=//h2 e corect
    def test_login_form_title(self):
        expected = "Login Page"
        actual = self.driver.find_element(By.XPATH, "//h2").text
        self.assertEqual(expected, actual, "Unexpected text on element")


    # ● Test 4
    # - Verifică dacă butonul de login este displayed
    def test_login_button_is_displayed(self):
        # assert self.driver.find_element(By.CLASS_NAME, "radius").is_displayed(), "Login button is not displayed"
        self.assertTrue(self.driver.find_element(By.CLASS_NAME, "radius").is_displayed(), "Login button is not displayed")

    # ● Test 5
    # - Verifică dacă atributul href al linkului ‘Elemental Selenium’ e corect
    def test_elemental_selenium_link_attribute(self):
        expected = "http://elementalselenium.com/"
        actual = self.driver.find_element(By.LINK_TEXT, "Elemental Selenium").get_attribute("href")
        self.assertEqual(expected, actual, "Incorrect link")

    # ● Test 6
    # - Lasă goale user și pass
    # - Click login
    # - Verifică dacă eroarea e displayed
    def test_invalid_login_error_message(self):
        self.driver.find_element(By.CLASS_NAME, "radius").click()
        assert self.driver.find_element(By.ID, "flash").is_displayed()

    # ● Test 7
    # - Completează cu user și pass invalide
    # - Click login
    # - Verifică dacă mesajul de pe eroare e corect
    # - Este și un x pus acolo extra așa că vom folosi soluția de mai jos:
    # expected = 'Your username is invalid!'
    def test_invalid_login_message_text(self):
        self.driver.find_element(By.ID, "username").send_keys("Python")
        self.driver.find_element(By.ID, "password").send_keys("TestareAutomata")
        self.driver.find_element(By.CLASS_NAME, "radius").click()
        expected = 'Your username is invalid!'
        actual = self.driver.find_element(By.ID, "flash").text
        self.assertIn(expected, actual)

    # ● Test 8
    # - Lasă goale user și pass
    # - Click login
    # - Apasă x la eroare
    # - Verifică dacă eroarea a dispărut
    def test_error_message_disappears(self):
        self.driver.find_element(By.CLASS_NAME, "radius").click()
        self.driver.find_element(By.CLASS_NAME, "close").click()
        locator = (By.ID, "flash")

        wait = WebDriverWait(self.driver, 10)
        wait.until_not(expected_conditions.presence_of_element_located(locator))

        self.assertTrue(self.is_element_absent(locator))


    def is_element_present(self, locator):
        elemente_gasite = self.driver.find_elements(*locator)
        return len(elemente_gasite) > 0

    def is_element_absent(self, locator):
        elemente_gasite = self.driver.find_elements(*locator)
        return len(elemente_gasite) == 0