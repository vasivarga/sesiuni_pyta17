import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class TestWaits(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Firefox()
        self.driver.get("https://www.uitestingplayground.com/ajax")
        self.driver.maximize_window()

    def tearDown(self) -> None:
        self.driver.quit()

    # IMPLICIT WAIT:
    # Este o așteptare globală (se aplica pentru toate elementele din momentul setării)
    # care spune driver-ului să aștepte un anumit timp înainte de a arunca
    # o excepție „No Such Element Exception” dacă elementul nu este găsit pe pagină.

    # Cum funcționează?
    # Se setează o singură dată și va fi aplicată tuturor elementelor pe care le cauți în pagină.
    # Dacă elementul este găsit înainte de expirarea timpului, scriptul va continua imediat.
    # Dacă elementul nu este găsit în timpul specificat, atunci testul va eșua.
    def test_implicit_wait(self):
        self.driver.implicitly_wait(20)
        self.driver.find_element(By.ID, "ajaxButton").click()
        self.driver.find_element(By.CLASS_NAME, "bg-success")

        self.driver.refresh()
        self.driver.find_element(By.ID, "ajaxButton").click()
        self.driver.find_element(By.CLASS_NAME, "bg-success")

    # EXPLICIT WAIT:
    # Explicit wait este o așteptare aplicată pentru un anumit element, spunând driverului
    # să aștepte până când o anumită condiție este îndeplinită înainte de a continua.

    # Cum funcționează?
    # Este mai flexibilă decât implicit wait, deoarece poți specifica exact condițiile pe care trebuie
    # să le îndeplinească elementul înainte ca scriptul să continue.
    # Este utilă pentru cazurile în care un element apare după o anumită acțiune sau un timp variabil.
    def test_explicit_wait(self):
        self.driver.find_element(By.ID, "ajaxButton").click()

        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "bg-success")))

        self.driver.refresh()
        self.driver.find_element(By.ID, "ajaxButton").click()
        # Testul ar pica
        # self.driver.find_element(By.CLASS_NAME, "bg-success")


