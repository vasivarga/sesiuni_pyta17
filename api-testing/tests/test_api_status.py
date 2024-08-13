import unittest

from api_requests.simple_books_api_requests import get_api_status


class TestApiStatus(unittest.TestCase):

    def test_api_status_code_and_body(self):
        response = get_api_status()

        assert response.status_code == 200, "Unexpected status code"
        assert response.json()['status'] == 'OK', "Unexpected API status"