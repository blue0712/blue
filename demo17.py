a1 = 'abcdefg'
print('a' in a1, 'A' in a1, 'ab' in a1)
a2 = 'hij'
print(a1 + a2, a2 * 5, 5 * a2)
a3 = 'QWERTYUIOPASDFGHJKLZXCVBNM'
print(a3[0:10:2], a3[::2])
print("reverse:", a3[10:0:-2])
print(a3[::1])
print(a3[::-1])
print(len(a3), min(a3), max(a3))
print(a3.index('W'), a3.index('P'))
# print(a3.index('0'))
print(a3.count('0'))
l1 = ['0', 'P', '9', 'Q', '3', '7', 'W', 'R']

for x in l1:
    print(x in a3 and a3.index(x))