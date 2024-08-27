import requests

AUTH_URL = "http://20.244.56.144/test/auth"

auth_payload = {
    "companyName": "Gitam",
    "clientID": "cbecd33d-a084-4172-9952-7aa040e8c721",
    "clientSecret": "lBAhNQnpTynspQRN",
    "ownerName": "DIVYAKOLU SAI CHANDU",
    "ownerEmail": "saichandu2384@gmail.com",
    "rollNo": "VU21CSEN0300112"
}

def get_auth_token():
    response = requests.post(AUTH_URL, json=auth_payload)
    if response.status_code == 201:
        return response.json().get("access_token")
    else:
        raise Exception("Authentication failed")
