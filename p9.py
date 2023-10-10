class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

rectangle = Rectangle(10, 5)

print("The area of the rectangle is", rectangle.calculate_area())
#done