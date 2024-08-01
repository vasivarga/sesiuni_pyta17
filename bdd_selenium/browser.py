from selenium import webdriver


class Browser:
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.implicitly_wait(3)

    def close(self):
        self.driver.quit()


