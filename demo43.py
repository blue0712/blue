import requests
from bs4 import BeautifulSoup

url1 = "https://www.mobile01.com/"

r2 = requests.get(url1)
print(r2.status_code)
headers = {
    'User-Agent': "My super computer",
    'from': "Trump Donald"
}


r1 = requests.get(url1, headers=headers)
print(r1.status_code)
print(r1.content)
soup1 = BeautifulSoup(r1.content, 'html.parser')
print(soup1.title)