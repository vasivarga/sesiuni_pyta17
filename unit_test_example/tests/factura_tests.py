import unittest

from app.factura import Factura

factura = Factura()

class TestFactura(unittest.TestCase):

    def test_factura_consum_sub_100(self):
        consum = 50

        expected = 75
        print(factura.calcul_pret(consum))
        actual = factura.calcul_pret(consum)
        assert actual == expected

    def test_factura_consum_intre_100_si_300(self):
        consum = 150

        expected = 450
        print(factura.calcul_pret(consum))
        actual = factura.calcul_pret(consum)
        assert actual == expected

    def test_factura_consum_peste_300(self):
        consum = 450

        expected = 2250
        print(factura.calcul_pret(consum))
        actual = factura.calcul_pret(consum)
        assert actual == expected

