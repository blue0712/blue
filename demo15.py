t1 = (5, 7)
print(hex(id(t1)))
t1 = (6, 7)
print(hex(id(t1)))
t2 = (5,)
print(t2, hex(id(t2)))
t2 += (7,)
print(t2, hex(id(t2)))
l1 = [5]
print(l1, hex(id(l1)))
l1.append(7)
print(l1, hex(id(l1)))