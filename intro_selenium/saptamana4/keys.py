import time
import unittest

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class TestKeys(unittest.TestCase):

    def test_keys(self):
        driver = webdriver.Firefox()
        driver.get("https://the-internet.herokuapp.com/key_presses")

        text_box = driver.find_element(By.ID, "target")

        text_box.send_keys(Keys.CONTROL)
        time.sleep(1)

        text_box.send_keys(Keys.SHIFT)
        time.sleep(1)

        text_box.send_keys(Keys.DELETE)
        time.sleep(1)

        text_box.send_keys("Testare Automata")
        time.sleep(1)

        text_box.send_keys(Keys.CONTROL + "a")
        time.sleep(1)

        text_box.send_keys(Keys.BACKSPACE)
        time.sleep(1)

        # Multiplicare de String
        text_box.send_keys("A"*10)
        time.sleep(1)

        driver.quit()
