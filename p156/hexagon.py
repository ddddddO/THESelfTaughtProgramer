#4
class Hexagon:
    def __init__(self, side):
        self.side = side

    def calculate_perimeter(self):
        return self.side * 6

hex = Hexagon(6)
rslt = hex.calculate_perimeter()
print(rslt)