lista = [1, "a", True, False]
print(lista)

print(*lista)



def suma(a, b):
    return a+b

print(suma(5,5))

def suma_numere(*numere):
    suma = 0
    for numar in numere:
        suma += numar

    return suma

print(suma_numere(1,2,3,4,435,345,435,345,34,534,534,5,345))
print(suma_numere(1,4,5,345))