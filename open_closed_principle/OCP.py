from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectange(Shape):
    def __init__(self, width,length):
        self.width = width 
        self.length = length

    def area(self):
        return self.width * self.length

class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

def calculate_total_area(shapes):
    total_area = sum(shape.area() for shape in shapes)
    return total_area

shapes = [Rectange(5,6), Circle(3)]
total_area = calculate_total_area(shapes)
print("Total area:", total_area)