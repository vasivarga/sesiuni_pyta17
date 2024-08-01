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