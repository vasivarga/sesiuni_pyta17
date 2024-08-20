import unittest

from api_requests.simple_books_api_requests import submit_order, get_order


class TestGetOrder(unittest.TestCase):

    def test_get_order_with_valid_id(self):
        book_id = 1
        customer_name = "Pyta17"

        submit_order_response = submit_order(book_id, customer_name)
        order_id = submit_order_response.json()['orderId']
        print(order_id)

        get_order_response = get_order(order_id)

        assert get_order_response.status_code == 200

        response_body = get_order_response.json()

        assert response_body['id'] == order_id
        assert response_body['bookId'] == book_id
        assert response_body['customerName'] == customer_name

    def test_get_order_with_invalid_id(self):
        pass
