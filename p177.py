class Shape:
    def what_am_i(self):
        return "I am a shape"

class Square(Shape):
    square_list = []

    def __init__(self, side):
        self.side = side
        self.square_list.append(self)
    
    def calculate_perimeter(self):
        return self.side * 4

    def change_size(self, n):
        self.side += n

    #2
    def __repr__(self):
        return "{} by {} by {} by {}".format(self.side, self.side, self.side, self.side)

#1
sq1 = Square(2)
sq2 = Square(3)
sq3 = Square(4)
print(Square.square_list)

print(sq1)
print(sq2)
print(sq3)

# 3
def is_same_obj(obj1, obj2):
    return obj1 is obj2

print(is_same_obj(sq1, sq2))

sq4 = sq1
print(is_same_obj(sq1, sq4))