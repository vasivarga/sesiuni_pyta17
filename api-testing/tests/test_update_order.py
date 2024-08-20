import unittest

from api_requests.simple_books_api_requests import submit_order, update_order, get_order


class TestUpdateOrder(unittest.TestCase):

    def test_update_order_with_valid_order_id(self):
        book_id = 1
        customer_name = "Pyta17"

        submit_order_response = submit_order(book_id, customer_name)
        order_id = submit_order_response.json()['orderId']

        new_customer_name = "Python Automation 17"
        update_order_response = update_order(order_id, new_customer_name)

        assert update_order_response.status_code == 204

        get_order_response = get_order(order_id)
        assert get_order_response.json()['customerName'] == new_customer_name
