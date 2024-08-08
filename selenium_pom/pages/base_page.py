from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from browser import Browser


class BasePage(Browser):

    ITEM_NAME = (By.CSS_SELECTOR, "div.inventory_item_name")
    ITEM_PRICE = (By.CSS_SELECTOR, "div.inventory_item_price")

    # Common selenium methods
    def find(self, locator):
        return self.driver.find_element(*locator)

    def type(self, locator, text):
        self.find(locator).send_keys(text)

    def click(self, locator):
        self.find(locator).click()

    def get_text(self, locator):
        return self.find(locator).text

    def verify_current_url(self, expected):
        assert self.driver.current_url == expected

    def get_current_url(self):
        return self.driver.current_url

    def select_dropdown_text(self, locator, text):
        dropdown = Select(self.find(locator))
        dropdown.select_by_visible_text(text)

    def is_element_absent(self, locator):
        return len(self.driver.find_elements(*locator)) == 0

    # Common elements methods
    def get_item_name_text(self):
        return self.get_text(self.ITEM_NAME)

    def get_item_price_text(self):
        return self.get_text(self.ITEM_PRICE)