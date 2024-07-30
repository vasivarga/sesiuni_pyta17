import unittest

import HtmlTestRunner

from saptamana3.unittest_exercitii import TestLogin
from saptamana4.alerts import TestAlerts
from saptamana4.keys import TestKeys


class TestSuite(unittest.TestCase):

    # numele metodei este predefinit si NU trebuie schimbat
    def test_suite(self):

        # declaram o variabila TestSuite numit teste_de_rulat
        # prin intermediul acestui obiect vom accesa metoda addTest din clasa TestSuite
        # metoda addTest primeste ca si parametru o clasa de teste procesata de metoda loadTestsFromTestCase
        teste_de_rulat = unittest.TestSuite()
        teste_de_rulat.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(TestKeys))
        teste_de_rulat.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(TestAlerts))
        teste_de_rulat.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(TestLogin))

        # addTests:
        # teste_de_rulat.addTests(
        #     unittest.defaultTestLoader.loadTestsFromTestCase(TestKeys),
        #     unittest.defaultTestLoader.loadTestsFromTestCase(TestAlerts),
        #     unittest.defaultTestLoader.loadTestsFromTestCase(TestLogin)
        # )

        # vom crea o variabila de tip HTMLTestRunner care ne ajuta in executarea testelor din suita
        # si ne va genera un raport HTML cu rezultatele testelor
        runner = HtmlTestRunner.HTMLTestRunner(
            combine_reports=True,
            report_title="Titlu raport executie",
            report_name="Rezultate teste"
        )

        runner.run(teste_de_rulat)