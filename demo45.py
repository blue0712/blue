import requests

#BASE_URL = 'https://ucom2019-d306a.firebaseio.com/%s.json'
BASE_URL = 'https://ucom2019-f2b9e.firebaseio.com/%s.json'

data1 = 'hello firebase realtime db using python'
url1 = BASE_URL % "demo1_string"
r1 = requests.put(url1, json=data1)
print(r1.status_code, r1.content, r1.json())

data2 = '試試中文使用rest的方式存取'
url2 = BASE_URL % "demo2_chinese_string"
r2 = requests.put(url2, json=data2)
print(r2.status_code, r2.content, r2.json())

data3 = [100, 3.14, 'hello', None, data2, None, data1]
url3 = BASE_URL % "demo3_list"
r3 = requests.put(url3, json=data3)
print(r3.status_code, r3.content, r3.json())

data4 = {'course':'pykt',"start":"nov",'duration':'35hr'}
url4 = BASE_URL %"demo4_dict"
r4 = requests.put(url4, json=data4)
print(r4.status_code, r4.content, r4.json())