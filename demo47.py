import requests

BASE_URL = 'https://ucom2019-f2b9e.firebaseio.com/%s.json'
url3 = BASE_URL % "demo3_list"
data3 = {'0': '一佰', '3': '參佰', '5': '伍佰', '8': '捌佰'}
r3 = requests.patch(url3, json=data3)
print(r3.status_code, r3.content, r3.json())
data4 = {'location': 'Taipei', 'course': 'PYKT',
         'instructor': 'Mark HO'}
url4 = BASE_URL % "demo4_dict"
r4 = requests.patch(url4, json=data4)
print(r4.status_code, r4.content, r4.json())