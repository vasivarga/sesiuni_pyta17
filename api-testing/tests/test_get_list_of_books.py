import unittest

import pytest

from api_requests.simple_books_api_requests import get_list_of_books


# limit intre 1 si 20
# type fiction sau non-fiction

# fara param
# limit
# type
# limit + type
# limita sub 1
# limita peste 20
# type invalid

class TestGetListOfBooks(unittest.TestCase):

    @pytest.mark.tags("smoke")
    def test_get_list_of_books_no_params(self):
        response = get_list_of_books()
        assert response.status_code == 200, "Unexpected status code"
        body = response.json()
        assert len(body) == 6, "Unexpected number of books returned"

    @pytest.mark.tags("smoke")
    def test_get_list_of_books_filter_by_limit(self):
        response = get_list_of_books(limit_size=2)
        assert response.status_code == 200, "Unexpected status code"
        assert len(response.json()) == 2, "Unexpected number of books returned"

    @pytest.mark.tags("regression", "smoke")
    def test_get_list_of_books_filter_by_type(self):
        response = get_list_of_books(book_type='fiction')
        books_list = response.json()

        for book in books_list:
            print(book['name'])
            assert book['type'] == 'fiction', "Unexpected book type"

    @pytest.mark.tags("regression")
    def test_get_list_of_books_filter_by_type_and_limit(self):
        # get_list_of_books(book_type='non-fiction', limit_size=1)
        pass

    def test_get_list_of_books_filter_by_invalid_limit_less_than_0(self):
        response = get_list_of_books(limit_size=-1)

        expected_error_message = "Invalid value for query parameter 'limit'. Must be greater than 0."
        actual_error_message = response.json()['error']

        assert expected_error_message == actual_error_message, "Unexpected error message"

    def test_get_list_of_books_filter_by_invalid_limit_greater_than_20(self):
        pass

    def test_get_list_of_books_filter_by_invalid_book_type(self):
        pass
