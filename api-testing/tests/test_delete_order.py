import unittest

from api_requests.simple_books_api_requests import submit_order, delete_order, get_order


class TestDeleteOrder(unittest.TestCase):

    def test_delete_order_with_valid_id(self):
        book_id = 1
        customer_name = "Pyta17"

        submit_order_response = submit_order(book_id, customer_name)
        order_id = submit_order_response.json()['orderId']

        delete_order_response = delete_order(order_id)
        assert delete_order_response.status_code == 204

        get_order_response = get_order(order_id)
        assert get_order_response.status_code == 404
        expected_message = f"No order with id {order_id}."
        actual_message = get_order_response.json()['error']
        assert expected_message == actual_message