sales = {'iphone6': 600, 'iphone6+': 500,
         'iphone7': 800, 'iphone7+': 400,
         'iphone11': 1000}
print(sales['iphone11'])
print(sales.get('iphone11+'))
print('htc' in sales, 'iphone11' in sales)
# print(sales['iphone11+'])
sales['iphoneXS'] = 850
print(sales.keys())
print(sales.values())
print(sales.items())
for item in sales.items():
    print(type(item), item, item[0], item[1])

for item in sales.items():
    print('%s has %d in stock' % (item[0], item[1]))

del sales['iphone6']
for k, v in sales.items():
    print(f'**{k} has {v} in stock')
updated = {'iphoneXS': 830, 'iPad': 450}
sales.update(updated)
print(sales)