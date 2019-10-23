import itertools

l1 = ['a', 'b', 'c']
l2 = ['i', 'j', 'k']
l3 = ['p', 'q', 'r']
i1 = itertools.chain(l1, l2, l3)
print(type(i1), i1)
print('start iterate:')
for i in i1:
    print(i, end='\t')
print()
print('start iterate,again:')
for i in i1:
    print(i, end='\t')
print()
i2 = itertools.chain(l1, l2, l3)
l4 = [i for i in i2]
for i in l4:
    print(i, end='\t')
print()
for i in l4:
    print(i, end='\t')
print()
currencies = ['TWD', 'USD', 'JPY', 'EURO', 'AUD']
result = itertools.combinations(currencies, 4)
l5 = [l for l in result]
print(len(l5), l5)
result2 = itertools.permutations(currencies, 2)
l6 = [r for r in result2]
print(len(l6), l6)