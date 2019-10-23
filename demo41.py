import requests

url = 'https://bugzilla.mozilla.org/rest/bug/35'
r1 = requests.get(url)
print(r1.status_code, r1.headers['content-type'])
print(type(r1.content), len(r1.content), r1.content[:100])
result1 = r1.json()
print(type(result1))
bugs = result1['bugs']
print(type(bugs))
firstBug = bugs[0]
print(type(firstBug))
print(firstBug["creator_detail"])
cc_detail = firstBug['cc_detail']
for detail in cc_detail:
    print(detail)