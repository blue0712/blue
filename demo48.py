import requests

BASE_URL = 'https://ucom2019-f2b9e.firebaseio.com/%s.json'

url1 = BASE_URL % "demo1_string"
url2 = BASE_URL % "demo2_chinese_string"
url3 = BASE_URL % "demo3_list"
url4 = BASE_URL % "demo4_dict"
url5 = BASE_URL % "demo5_orders"
r1 = requests.get(url1)
print(r1.status_code, r1.json())
r2 = requests.get(url2)
print(r2.json())
r3 = requests.get(url3)
print(r3.json())
r4 = requests.get(url4)
print(r4.json())
r5 = requests.get(url5)
print(r5.json())

