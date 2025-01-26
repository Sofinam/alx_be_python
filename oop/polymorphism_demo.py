import math

class Shape:
    def area(self):
        """Base method to calculate the area of a shape.
         Should be overridden by derived classes.
        """
        raise NotImplementedError("The area() method must be overridden in the derived class.")
    
class Rectangle(Shape):
    def __init__(self, length: float, width: float):
        """Initialise a rectangle with length and width."""
        self.length = length
        self.width = width

    def area(self):
        """Calculate the are of the rectangle.
        Formula: length x width"""
        return self.length * self.width
    
class Circle(Shape):
    def __init__(self, radius: float):
        """Initialise a circle with a radius."""
        self.radius = radius

    def area(self):
        """Calculate the area of the circle.
        Formula: n x radius"""
        return math.pi * self.radius ** 2