import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://formy-project.herokuapp.com/form")
time.sleep(1)

driver.find_element(By.CSS_SELECTOR, "#first-name").send_keys("Test")
time.sleep(1)

driver.find_element(By.CSS_SELECTOR, "input#first-name").clear()
time.sleep(1)

driver.find_element(By.CSS_SELECTOR, "input[placeholder='Enter first name']").send_keys("Test 2")
time.sleep(1)

driver.find_element(By.CSS_SELECTOR, "input.form-control").send_keys("Am cautat dupa clasa")
time.sleep(1)

# Find element vr find elements
driver.find_element(By.CSS_SELECTOR, "input[type='checkbox']").click()
driver.find_element(By.CSS_SELECTOR, "input[type='checkbox']").click()

lista_checkboxuri = driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")

print(len(lista_checkboxuri))

for element in lista_checkboxuri:
    element.click()
    print(element.is_selected())
    print(element.get_attribute("id"))
    print(element.get_attribute("value"))
    print("\n")

time.sleep(1)

# find_element returneaza un singur element (primul) pe care il gaseste
# returneaza eroare NoSuchElementException in caz ca nu gaseste elementul
# driver.find_element(By.CSS_SELECTOR, "input#tralala")

# find_element returneaza o lista cu elemente web
# retunreaza o lista goala
lista = driver.find_elements(By.CSS_SELECTOR, "input#tralala")
print(len(lista))
print("Am trecut de functia find_elements()")