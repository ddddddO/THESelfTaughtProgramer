#2
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return self.radius ** 2 * math.pi

ci = Circle(3)
print(ci.radius)

area = ci.area()
print(area)