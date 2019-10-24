a1 = True
a2 = False

print(a1 and a2, a1 and a1, a2 and a2)
print(a1 and 100)
print(a1 and 3.14)
print(a1 and 'hello world')
print(a1 and None)
print(a2 or 100)
print(a2 or 3.14)
print(a2 or 'hello world'*3)
print(a2 or None)