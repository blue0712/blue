class Car:
    vendor = 'Lexus'
    valid = True


c1 = Car()
c2 = Car()
print(Car.vendor, Car.valid)
print(c1.vendor, c1.valid, c2.vendor, c2.valid)
Car.function = True
print(c1.function, c2.function, Car.function)
c1.passenger = 4
c2.color = 'red'
# print(c1.passenger, c2.passenger)
print(c1.passenger)
# print(c2.color, c1.color)
print(c2.color)
Car.max = 100
c3 = Car()
print(c1.max, c2.max, c3.max, Car.max)