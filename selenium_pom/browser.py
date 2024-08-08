from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class Browser:
    chrome_options = Options()
    chrome_options.add_argument("--disable-search-engine-choice-screen")
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    driver.implicitly_wait(3)

    def close(self):
        self.driver.close()