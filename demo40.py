import json

data1 = ['Sunday', 'Monday', 3.14, 500, None, ('apple', 'banana')]
result1 = json.dumps(data1)
print(type(data1), type(result1), result1)
result2 = json.loads(result1)
print(type(result2))
for item in result2:
    print(item)

data2 = {'name': 'PYKT', 'duration': '35hr', 'instructor': 'Tim'}
result3 = json.dumps(data2)
print(type(data2), type(result3), result3)
result4 = json.loads(result3)
print(type(result4))
for k, v in result4.items():
    print(f'key={k},value={v}')