class Rectangle:
    'this class represents rectangles'
    def setSize(self, width, height):
        'defines the width and height of the rectangle'
        self.width = width
        self.height = height
    def perimeter(self):
        'returns the perimeter of the rectangle'
        return 2 * (self.width + self.height)
    def area(self):
        'returns the area of the rectangle'
        return self.width * self.height
