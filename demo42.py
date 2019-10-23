import requests
from bs4 import BeautifulSoup

url1 = "https://www.uuu.com.tw/"

r1 = requests.get(url1)
print(r1.status_code)
soup1 = BeautifulSoup(r1.content, 'html.parser')
print(soup1.title)
all_courses = soup1.find('div', {'id': 'course_list'})


courses = all_courses.find_all('a')
for i in courses:
    print(i)

courses = all_courses.find_all('h3')
for i in courses:
    print(i)