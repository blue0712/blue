class Person:
    def __init__(self, age):
        self.age = age
        pass

    pass


p1 = Person(38)
y = 38
print(p1.age, y, hex(id(p1)), hex(id(p1.age)), hex(id(y)))
p1.age = 39
y = 39
print(p1.age, y, hex(id(p1)), hex(id(p1.age)), hex(id(y)))
p2 = Person(38)
p3 = p1
print(hex(id(p1)), hex(id(p2)), hex(id(p3)))
print(hex(id(p1.age)), hex(id(p2.age)), hex(id(p3.age)))