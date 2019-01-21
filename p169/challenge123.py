#3
class Shape:
    def what_am_i(self):
        return "I am a shape"

#1
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def calculate_perimeter(self):
        return (self.length * 2) + (self.width * 2)

class Square(Shape):
    def __init__(self, side):
        self.side = side
    
    def calculate_perimeter(self):
        return self.side * 4

    #2
    def change_size(self, n):
        self.side += n

rect = Rectangle(2, 100)
print(rect.calculate_perimeter())
print(rect.what_am_i())

squr = Square(55)
print(squr.calculate_perimeter())
squr.change_size(5)
print(squr.calculate_perimeter())
print(squr.what_am_i())