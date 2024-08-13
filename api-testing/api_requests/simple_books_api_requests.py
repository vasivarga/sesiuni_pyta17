import requests


def get_api_status():
    endpoint = "https://simple-books-api.glitch.me/status"
    response = requests.get(endpoint)
    return response

# response = get_api_status()
# print(response.status_code)
# print(response.json())
# body = response.json()
# print(type(body))
# print(body['status'])


def get_list_of_books(book_type="", limit_size=""):
    pass

# optional: get_list_of_books(book_type="", limit_size="")
# print(get_list_of_books("fiction", 5).json())