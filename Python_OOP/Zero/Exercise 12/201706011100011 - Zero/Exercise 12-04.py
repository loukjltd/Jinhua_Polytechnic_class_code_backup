from abc import ABC, abstractmethod
import math

class Shape(ABC):
    def __init__(self, colour):
        self.colour = colour

    def fill(self):
        print("Shape filled with {0}".format(self.colour))

    @abstractmethod
    def get_area(self):
        pass

    @abstractmethod
    def draw(self):
        pass


class Rectangle(Shape):
    def __init__(self, colour, length, width):
        Shape.__init__(self, colour)
        self.length = length
        self.width = width

    def get_area(self):
        return self.length * self.width

    def draw(self):
        print("Drawing a rectangle")


class Circle(Shape):
    def __init__(self, colour, radius):
        Shape.__init__(self, colour)
        self.radius = radius

    def get_area(self):
        return math.pi * self.radius * self.radius

    def draw(self):
        print("Drawing a circle")


shapes = [Circle("Blue", 10),
          Circle("White", 20),
          Rectangle("Black", 3, 5),
          Rectangle("Red", 7, 9)]
for i in shapes:
    i.fill()
    i.draw()

a = 0
total_area = 0
max_area = shapes[0].get_area()
min_area = shapes[0].get_area()
for i in shapes:
    a += 1
    area1 = i.get_area()
    total_area = total_area + area1
    if area1 > max_area:
        max_area = area1
    if area1 < min_area:
        min_area = area1
average_area = total_area/a

print("total area: %.2f" % total_area)
print("average area: %.2f" % average_area)
print("max area: %.2f" % max_area)
print("min area: %.2f" % min_area)
