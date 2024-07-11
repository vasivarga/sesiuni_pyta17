import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://formy-project.herokuapp.com/datepicker")
time.sleep(1)


# Exercitiu 1:
# Definim o functie pentru deschiderea date picker-ului
# pe care o vom refolosi

def open_datepicker():
    driver.find_element(By.ID, "datepicker").click()
    time.sleep(1)


open_datepicker()
#
#
# # Exercitiu 2:
# # Deschidem date picker-ul si dam click pe ziua curenta
# # Ce observam?
# # Cum putem sa facem programul sa ruleze corect indiferent data în care suntem?
# # Care este diferenta dintre ziua de astazi si celelalte zile ale calendarului?
#
# open_datepicker()
# driver.find_element(By.CSS_SELECTOR, ".today.day").click()
# time.sleep(2)
#
# # Exercitiu 3: Deschidem date picker-ul si afisam cate zile are luna curenta
# # Sa mearga corect indiferent de data in care rulam scriptul
#
# open_datepicker()
# lista = driver.find_elements(By.CSS_SELECTOR, "td:not(.old, .new).day")
# print(f"Luna curenta are {len(lista)} zile")
#
# # Exercitiu 4: Deschidem date picker-ul si afisam TOATE zilele care se vad din luna trecuta
# lista_zile_luna_trecuta = driver.find_elements(By.CSS_SELECTOR, "td.old.day")
# lista_zile_luna_viitoare = driver.find_elements(By.CSS_SELECTOR, "td.new.day")
#
# print("Zilele din luna trecuta:")
# for zi in lista_zile_luna_trecuta:
#     print(zi.text)
#
# print("Zilele din luna viitoare:")
# for zi in lista_zile_luna_viitoare:
#     print(zi.text)
#
#
# # Exercitiu 6: Navigam in calendar folosind butonul » (Next)
# # pana cand ajungem in anul 2025
#
# #definim o functie pentru a obtine textul cu luna si anul de pe calendar
def get_calendar_month_and_year_text():
    return driver.find_element(By.CSS_SELECTOR, ".datepicker-days .datepicker-switch").text
#
#
# print(get_calendar_month_and_year_text())

def click_next_button():
    driver.find_element(By.CSS_SELECTOR, ".datepicker-days .next").click()

# while "2025" not in get_calendar_month_and_year_text():
#     click_next_button()
#     time.sleep(1)


# Exercitiu 8: Scriem o functie care selecteaza o data din viitor
# Functia va primi 3 parametri (anul, luna - string in limba engleza, ziua)

def select_date(year, month, day):
    open_datepicker()
    while year not in get_calendar_month_and_year_text():
        click_next_button()
        time.sleep(1)

    while month not in get_calendar_month_and_year_text():
        click_next_button()
        time.sleep(1)

    driver.find_element(By.XPATH, f"//td[text()='{day}' and @class='day']").click()


driver.refresh()

select_date("2024", "August", "3")
select_date("2024", "November", "20")
select_date("2025", "January", "3")
