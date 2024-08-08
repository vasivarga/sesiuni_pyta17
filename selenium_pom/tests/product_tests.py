import unittest

from pages.cart_page import CartPage
from pages.login_page import LoginPage
from pages.products_page import ProductsPage


class ProductTests(unittest.TestCase):

    def setUp(self) -> None:
        self.login_page = LoginPage()
        self.products_page = ProductsPage()
        self.cart_page = CartPage()

        self.login_page.open()
        self.login_page.login("standard_user", "secret_sauce")

    def tearDown(self) -> None:
        self.login_page.close()

    def test_add_product_to_cart(self):
        self.products_page.click_add_backpack_to_cart_button()
        assert self.products_page.is_add_to_cart_backpack_button_not_present()
        assert self.products_page.is_remove_backpack_button_visible()
        assert self.products_page.get_cart_badge_text() == "1"

        expected_product_title = self.products_page.get_backpack_title()
        expected_product_price = self.products_page.get_backpack_price()

        self.products_page.click_shopping_cart()

        assert self.cart_page.get_current_url() == "https://www.saucedemo.com/cart.html"

        actual_product_title = self.cart_page.get_item_name_text()
        actual_product_price = self.cart_page.get_item_price_text()

        assert expected_product_title == actual_product_title
        assert expected_product_price == actual_product_price


    # Tema: faceti un test care sorteaza produsele dupa pret
    # crescator si validam faptul ca produsele sunt ordonate



