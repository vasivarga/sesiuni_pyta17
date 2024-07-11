import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select

# Intram pe siteul demo.nopcommerce.com si facem o cautare dupa cuvantul phone
# verificam ca s-au returnat cel putin 3 rezultate

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://demo.nopcommerce.com/")
time.sleep(1)

driver.find_element(By.XPATH, "//input[@id='small-searchterms']").send_keys("phone")
driver.find_element(By.XPATH, "//button[text()='Search']").click()
time.sleep(1)

lista_produse = driver.find_elements(By.XPATH, "//div[@class='product-item']")
assert len(lista_produse) >= 3, "Eroare, s-au gasit mai putin de 3 rezultate"

# Functie care va lua din pagina elementele web care reprezinta preturile
def get_element_prices():
    return driver.find_elements(By.XPATH, "//span[@class='price actual-price']")

# Functie care primeste ca parametru o lista cu preturi (WebElement)
# si returneaza o lista noua cu preturile fara semn $ si cu tipul float
def get_product_prices_as_list(lista_elemente_web: list[WebElement]):
    lista_valoare_preturi = []
    for element in lista_elemente_web:
        text_pret = element.text.replace('$', '')
        lista_valoare_preturi.append(float(text_pret))
    return lista_valoare_preturi


# Extragem pretul cel mai mic

# iau lista cu elementele web care contin preturile
lista_elemente_pret = get_element_prices()

# extrag din lista respectiva preturile sub forma de numere
lista_valoare_preturi = get_product_prices_as_list(lista_elemente_pret)

print(f"Lista nesortata: {lista_valoare_preturi}")

lista_valoare_preturi.sort()

print(f"Lista sortata: {lista_valoare_preturi}")

print(f"Pretul cel mai mic este {lista_valoare_preturi[0]}")


# Sortam produsele dupa pret crescator si validam ca s-a sortat corect in pagina
dropdown = Select(driver.find_element(By.XPATH, "//select[@name='products-orderby']"))
dropdown.select_by_visible_text("Price: Low to High")
time.sleep(1)

lista_pret_produse_dupa_sortare = get_element_prices()
lista_preturi = get_product_prices_as_list(lista_pret_produse_dupa_sortare)

assert lista_preturi == lista_valoare_preturi, "Eroare, listele de pret nu sunt egale"


# Explicatie
def salutare(nume: str):
    print(f"Salut, {nume}")

lista = [234, True]

salutare("Mihai")
salutare("Ana")

# argumentul este subliniat cu galben
salutare(lista)
salutare(5)
