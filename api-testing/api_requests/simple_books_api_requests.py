import requests

from api_requests.generate_token_request import get_token

token = get_token()

def get_api_status():
    endpoint = "https://simple-books-api.glitch.me/status"
    response = requests.get(endpoint)
    return response


# def get_list_of_books(book_type="", limit_size=""):
#     endpoint = "https://simple-books-api.glitch.me/books"
#
#     if book_type != "" and limit_size != "":
#         endpoint = f"{endpoint}?type={book_type}&limit={limit_size}"
#     elif book_type != "":
#         endpoint = f"{endpoint}?type={book_type}"
#     elif limit_size != "":
#         endpoint = f"{endpoint}?limit={limit_size}"
#     response = requests.get(endpoint)
#     return response

def get_list_of_books(book_type="", limit_size=""):
    endpoint = f"https://simple-books-api.glitch.me/books?type={book_type}&limit={limit_size}"
    response = requests.get(endpoint)

    return response


# print(get_list_of_books().json())
# print(get_list_of_books(book_type="fiction").json())
# print(get_list_of_books(book_type='fiction', limit_size=3).json())

ORDERS_ENDPOINT = "https://simple-books-api.glitch.me/orders"


def submit_order(book_id, customer_name):
    header_params = {
        'Authorization': f"Bearer {token}"
    }

    request_body = {
        "bookId": book_id,
        "customerName": customer_name
    }

    response = requests.post(ORDERS_ENDPOINT, headers=header_params, json=request_body)
    return response

def get_order(order_id):
    endpoint = ORDERS_ENDPOINT + f'/{order_id}'

    header_params = {
        'Authorization': f"Bearer {token}"
    }

    return requests.get(endpoint, headers=header_params)

def update_order(order_id, customer_name):
    endpoint = ORDERS_ENDPOINT + f'/{order_id}'
    header_params = {
        'Authorization': f"Bearer {token}"
    }
    request_body = {
        "customerName": customer_name
    }

    return requests.patch(endpoint, headers=header_params, json=request_body)

def delete_order(order_id):
    endpoint = ORDERS_ENDPOINT + f'/{order_id}'
    header_params = {
        'Authorization': f"Bearer {token}"
    }

    return requests.delete(endpoint, headers=header_params)