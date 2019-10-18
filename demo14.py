a1 = ()
a2 = []
a3 = (5)
a4 = (5,)
a5 = [5]
print(type(a1), type(a2))
print(type(a4), type(a5), type(a3))
b1 = 5
b2 = 7

print(b1, b2)
temp = b1
b1 = b2
b2 = temp
print(b1, b2)
b3 = 4
b4 = 6
print(b3, b4)
b3, b4 = b4, b3
print(b3, b4)
b5 = 'hello world'
b6 = [3, 4, 5]
print(b5, b6)
b5, b6 = b6, b5
print(b5, b6)
c1, c2, c3, c4, c5 = 'A', 'K', 'Q', 'J', '10'
print(c1, c2, c3, c4, c5)
c5, c1, c2, c3, c4 = c1, c2, c3, c4, c5
print(c1, c2, c3, c4, c5)