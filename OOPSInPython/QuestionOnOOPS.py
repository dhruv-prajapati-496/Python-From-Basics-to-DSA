# WAP to define a circle class to create  a circle with radius using constructor.
# Define area() method which calculates area.
# Define perimeter() method which calculates perimeter.

class circle:
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return (self.radius**2)*(22/7)

    def perimeter(self):
        return self.radius*(22/7)*2

c1 = circle(7)
print("Radius is:",c1.radius)
print("Area is:",c1.area())
print("Perimeter is:",c1.perimeter())
        