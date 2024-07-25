import unittest


class TestDemo(unittest.TestCase):

    def setUp(self):
        print("Ruleaza metoda setUp()")

    def tearDown(self):
        print("Ruleaza metoda tearDown()")

    def test_case_1(self):
        print("Ruleaza metoda de test TC1")
        assert True

    def test_case_2(self):
        print("Ruleaza metoda de test TC2")
        # assert 1 + 1 == 3, "Testul a picat"
        self.assertEqual(1+1+1, 3, "Testul a picat...")
        self.assertTrue(5==5, "Testul a picat")

        membru = "c"
        lista = ["a", "b", 5, True]

        self.assertIn(membru, lista, "Membrul nu se afla in lista")

    @unittest.skip
    def test_case_3(self):
        print("Ruleaza metoda de test TC3")

    def metoda_auxiliara(self):
        print("Se ruleaza metoda auxiliara...")

    def test_case_4(self):
        print("Ruleaza metoda de test TC4")
        self.metoda_auxiliara()
        assert True