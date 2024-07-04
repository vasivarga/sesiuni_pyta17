import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

# metoda care deschide un link
driver.get("https://www.elefant.ro/")
time.sleep(2)

# metoda care gaseste si ne returneaza un WebElement
# ID
button_accept = driver.find_element(By.ID, "CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll")
button_accept.click()

# CLASS NAME
input_search = driver.find_element(By.CLASS_NAME, "searchTerm")
input_search.send_keys("Carte")

# NAME
button_search = driver.find_element(By.NAME, "search")
button_search.click()
time.sleep(2)

# LINK TEXT
# link_pagina_de_pornire = driver.find_element(By.LINK_TEXT, "PAGINA DE PORNIRE")
# link_pagina_de_pornire.click()

# PARTIAL LINK TEXT
partial_link_pagina_de_pornire = driver.find_element(By.PARTIAL_LINK_TEXT, "PAGINA DE")
partial_link_pagina_de_pornire.click()

print(driver.title)
print(driver.current_url)

time.sleep(3)