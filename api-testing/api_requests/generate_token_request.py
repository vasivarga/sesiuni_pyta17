import random

import requests


def get_token():
    endpoint = "https://simple-books-api.glitch.me/api-clients/"

    random_number = random.randint(1, 99999999999999999)

    request_body = {
        "clientName": "Pyta17",
        "clientEmail": f"pyta17{random_number}@gmail.com"
    }

    response = requests.post(endpoint, json=request_body)
    token = response.json()["accessToken"]
    print(token)
    return token

