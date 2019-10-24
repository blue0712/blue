class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        pass

    def calculate_area(self):
        return self.width * self.height


r1 = Rectangle(5, 7)
r2 = Rectangle(2, 9)
print(r1.calculate_area(), r2.calculate_area())