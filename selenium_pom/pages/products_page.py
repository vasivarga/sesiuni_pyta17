from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class ProductsPage(BasePage):

    BUTTON_ADD_TO_CART_BACKPACK = (By.ID, "add-to-cart-sauce-labs-backpack")
    BUTTON_REMOVE_BACKPACK = (By.ID, "remove-sauce-labs-backpack")
    SHOPPING_CART_BADGE = (By.CSS_SELECTOR, "span.shopping_cart_badge")
    SHOPPING_CART = (By.ID, "shopping_cart_container")
    BACKBACK_PRICE = (By.XPATH, "//button[@id='remove-sauce-labs-backpack']/preceding-sibling::div")
    BACKBACK_TITLE = (By.XPATH, "//button[@id='remove-sauce-labs-backpack']/../../div/a/div")

    def click_add_backpack_to_cart_button(self):
        self.click(self.BUTTON_ADD_TO_CART_BACKPACK)

    def is_remove_backpack_button_visible(self):
        return self.find(self.BUTTON_REMOVE_BACKPACK).is_displayed()

    def is_add_to_cart_backpack_button_not_present(self):
        return self.is_element_absent(self.BUTTON_ADD_TO_CART_BACKPACK)

    def get_cart_badge_text(self):
        return self.get_text(self.SHOPPING_CART_BADGE)

    def click_shopping_cart(self):
        self.click(self.SHOPPING_CART_BADGE)

    def get_backpack_price(self):
        return self.get_text(self.BACKBACK_PRICE)

    def get_backpack_title(self):
        return self.get_text(self.BACKBACK_TITLE)


