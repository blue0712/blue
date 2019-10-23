import requests

BASE_URL = 'https://ucom2019-d306a.firebaseio.com/%s.json'

# url1 = BASE_URL % "demo1_string"
# url2 = BASE_URL % "demo2_chinese_string"
# url3 = BASE_URL % "demo3_list"
# url4 = BASE_URL % "demo4_dict"
# url5 = BASE_URL % "demo5_orders"
#
# r1 = requests.delete(url1)
# print(r1.status_code, r1.content)
# r2 = requests.delete(url2)
# print(r2.status_code, r2.content)
# r3 = requests.delete(url3)
# r4 = requests.delete(url4)
# r5 = requests.delete(url5)

url_all = BASE_URL % ""
r6 = requests.delete(url_all)