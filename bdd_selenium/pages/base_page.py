from selenium.webdriver.support.select import Select

from browser import Browser


class BasePage(Browser):

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

    def select_dropdown_text(self, locator, text):
        dropdown = Select(self.find(locator))
        dropdown.select_by_visible_text(text)