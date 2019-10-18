l1 = ()
l2 = []
l3 = {}
l4 = {'x'}
l5 = {'x': 500}
l6 = set()
print(type(l1), type(l2), type(l3), type(l4), type(l5), type(l6))
s1 = set(list('APPLE'))
print(s1)
s2 = set(list('PINEAPPLE'))
print(s2)
s3 = {'B', 'A', 'N', 'A', 'N', 'A'}
print(s3)
print(s1 | s3)
print(s1 & s3)
print(s1 ^ s3)
print(len(s1 | s3))
s3.add('X')
print(s3)
s3.add(('X', 'Y'))
print(s3)
s3.add(3.14159)
print(s3)
# s3.add(s1)
s4 = set('5',)
print(s4)


for x in s3:
    print('got a value in s3 %s' % (str(x)))

    t1 = set(list('APPLE'))
    t2 = {'B', 'A', 'N', 'A', 'N', 'A'}
    t3 = set(list('PINEAPPLE'))
    print(t1 < t2, t1 > t2)
    print(t1 < t3, t1 > t3)
    print(t1 < t1, t1 > t1)
