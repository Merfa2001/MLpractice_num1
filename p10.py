class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def calculate_perimeter(self):
        return 4 * self.width

square = Square(10)

print("The perimeter of the square is", square.calculate_perimeter())
#done