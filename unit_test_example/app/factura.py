class Factura:

    def calcul_pret(self, putere_consumata):
        if putere_consumata < 100:
            return putere_consumata * 1.5

        elif 100 <= putere_consumata <= 300:
            return putere_consumata * 3

        elif putere_consumata > 300:
            return putere_consumata * 5