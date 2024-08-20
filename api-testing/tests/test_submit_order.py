import unittest

from api_requests.simple_books_api_requests import submit_order


# submit valid order
# submit order with invalid id

class TestSubmitOrder(unittest.TestCase):

    def test_submit_order_valid_book_id(self):
        response = submit_order(5, "Pyta17")

        assert response.status_code == 201, "Unexpected status code"
        assert response.json()['created'] == True, "Order not created"

    def test_submit_order_invalid_book_id(self):
        response = submit_order(9, "Pyta17")
        expected_error = "Invalid or missing bookId."
        actual_error = response.json()['error']
        assert response.status_code == 400, "Unexpected status code"
        assert expected_error == actual_error, "Unexpected error message"