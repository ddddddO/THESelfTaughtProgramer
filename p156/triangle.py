#3
class Triangle:
    def __init__(self, height, base):
        self.height = height
        self.base = base
    
    def area(self):
        return self.height * self.base / 2
    
tri = Triangle(4, 3)
area = tri.area()
print(area)
