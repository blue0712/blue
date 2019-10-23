import requests

BASE_URL = 'https://ucom2019-f2b9e.firebaseio.com/%s.json'

url5 = BASE_URL % "demo5_orders"

for x in range(0, 10):
    data5 = {'name': 'Mark', 'quantity': 2 + x}
    r5 = requests.post(url5, json=data5)
    print(r5.status_code, r5.content, r5.json())