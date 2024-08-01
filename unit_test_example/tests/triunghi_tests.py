import unittest

from app.triunghi import Triunghi

triunghi = Triunghi()


class TriunghiTests(unittest.TestCase):

    def test_perimetru(self):
        l1 = 5
        l2 = 10
        l3 = 7

        expected = 22
        actual = triunghi.calcul_perimetru(l1, l2, l3)
        assert expected == actual

    def test_arie(self):
        baza = 3
        inaltime = 10

        expected = 15
        actual = triunghi.calcul_arie(baza, inaltime)
        assert expected == actual
