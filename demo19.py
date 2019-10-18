v1 = 'ABCDE'
v2 = ['A', 'B', 'C', 'D', 'E']
v3 = list(v1)
print(type(v1), type(v2), type(v3))
v2[1] = 'b'
v3[2] = 'c'
print(v1, v2, v3)
# v1[1] = 'b'
v4 = list('QWERTYUIOP' * 5)
print("V4" , v4)

v4[::3] = '*' * len(v4[::3])
print(v4)
del v4[2:5]
print(v4)
v4[2:5] = []
print(v4)
v4 = [3.14, 500, 'None', None, (3, 5), {'apple', 'banana'}]
print(type(v4))