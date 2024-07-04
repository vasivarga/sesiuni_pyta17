import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# Test case: Pagina afiseaza titlul corect

# Pasii: Navigam pe site
# Rezultat asteptat: titlul paginii este "elefant.ro - mallul online al familiei tale! • Branduri de top, preturi excelente • Peste 500.000 de produse pentru tine!"

driver = webdriver.Chrome()

# metoda care deschide un link
driver.get("https://www.elefant.ro/")
time.sleep(1)

titlu_asteptat = "elefant.ro - mallul online al familiei tale! • Branduri de top, preturi excelente • Peste 500.000 de produse pentru tine!"
titlul_actual = driver.title

assert titlu_asteptat == titlul_actual, "Eroare, titlul nu este bun!"