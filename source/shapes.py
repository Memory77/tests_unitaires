import math


class Shape:
    def area(self):
        pass

    def perimeter(self):
        pass


class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius 

    def area(self):
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        return math.pi * self.radius * 2
    

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return self.length*2 + self.width*2
    
    def __eq__(self, other:object):
        if not isinstance(other, Rectangle):
            return False
        return self.width == other.width and self.length == other.length
    
class Square(Rectangle):
    def __init__(self, side):
        super().__init__(length=side, width=side)
    
    
        