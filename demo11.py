x = 5
y = 3.14
print(type(x), type(y))
c1 = 5 + 3j
c2 = 4 - 2j
print(type(c1), type(c2))
print(c1.real, c1.imag)
print(c2.imag, c2.real)
print(c1 + c2, c1 - c2, c1 * c2)
print(c1.conjugate())
print(c2.conjugate())
print(abs(5))
print(abs(-5))
print(abs(c1), abs(c2))
print((5 ** 2 + 3 ** 2) ** 0.5, (4 ** 2 + (-2) ** 2) ** 0.5)