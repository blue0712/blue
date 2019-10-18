x = 5
l1 = [5]

print(type(x), type(l1), x, l1)
print(hex(id(x)), hex(id(l1)), hex(id(l1[0])))

x = 6
l1[0] = 6
print(type(x), type(l1), x, l1)
print(hex(id(x)), hex(id(l1)), hex(id(l1[0])))

x = None
print(type(x))