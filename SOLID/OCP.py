# Open Closed Principle
# This principle tries to imply that the code should be open to extension but not modification.
# SImply you can add more operations to an existing functionality but cannot modify the existing functionality.


from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Cirle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 2 * 3.14 * self.radius

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

def calculate_total_area(shapes):
    total_area = sum(shape.area() for shape in shapes)
    return total_area


shapes = [Rectangle(10,20) , Square(20), Cirle(10)]
print(calculate_total_area(shapes))
