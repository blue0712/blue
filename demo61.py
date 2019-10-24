class MyClass:
    pass

m1 = MyClass()

print(m1.__class__)
print(type(m1))
print(MyClass)
print(m1)

print(m1.__class__.__bases__)
print(type(m1.__class__.__bases__))
print(type(MyClass).__base__)
print(type(MyClass.__base__))

print(type(m1) == MyClass)