from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/dynamic_controls")

driver.find_element(By.XPATH, "//button[text()='Enable']").click()

wait = WebDriverWait(driver, 10)

locator_element = (By.XPATH, "//input[@type='text']")

# Asteptam pana cand atributul "disabled" al inputului dispare
wait.until_not(expected_conditions.element_attribute_to_include(locator_element, "disabled"))

driver.find_element(By.XPATH, "//input[@type='text']").send_keys("Aloo")