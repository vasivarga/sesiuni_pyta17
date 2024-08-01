import unittest

from app.calculator import Calculator

calculator = Calculator()


class CalculatorTests(unittest.TestCase):

    def test_adunare(self):
        a = 5
        b = 3

        expected = 8
        actual = calculator.adunare(a, b)

        assert expected == actual

    def test_scadere(self):
        a = 25
        b = 3

        expected = 22
        actual = calculator.scadere(a, b)

        assert expected == actual

    def test_inmultire(self):
        a = 5
        b = 3

        expected = 15
        actual = calculator.inmultire(a, b)

        assert expected == actual

    def test_impartire(self):
        a = 20
        b = 4

        expected = 5.0
        actual = calculator.impartire(a, b)

        assert expected == actual
