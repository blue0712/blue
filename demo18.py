a1 = True
a2 = False

print(a1 and a1, a1 and a2)
print(a1 and 3.14, a1 and 500, a1 and 'hello', a1 and None)

a3 = False
print(a3 or a1, a3 or a2)
print(a3 or 3.14, a3 or 500, a3 or 'world', a3 or None)