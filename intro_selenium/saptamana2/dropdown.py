import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://formy-project.herokuapp.com/form")
time.sleep(1)

# Metoda 1 - nu este recomandata

# driver.find_element(By.ID, "select-menu").click()
# driver.find_element(By.CSS_SELECTOR, "option[value='1']").click()
# time.sleep(3)


# Metoda 2 - recomandata
element_select = driver.find_element(By.ID, "select-menu")
dropdown = Select(element_select)
dropdown.select_by_value("4")
time.sleep(2)
dropdown.select_by_index(3)
time.sleep(2)
dropdown.select_by_visible_text("2-4")
time.sleep(2)


