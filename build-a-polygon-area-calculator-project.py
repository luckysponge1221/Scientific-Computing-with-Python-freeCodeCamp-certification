class Rectangle:

    def __init__(self, width, height):
        self.width = width 
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width*self.height

    def get_perimeter(self):
        return 2*self.width + 2*self.height

    def get_diagonal(self):
        return (self.width**2 + self.height**2)**0.5

    def get_picture(self):
        picture = ''
        if self.width > 50 or self.height > 50:
            return 'Too big for picture.'
        for i in range(self.height):
            picture += f'{"*"*self.width}\n'
        return picture 
    
    def get_amount_inside(self, shape):
        w = getattr(shape, 'width')
        h = getattr(shape, 'height')

        if w <= self.width and h <= self.height:
            nw = self.width//w
            nh = self.height//h
            amount = nw*nh
            return amount
        else:
            return 0
    
    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
        self.side = side

    def set_side(self, side):
        self.width = side
        self.height = side

    def set_width(self, side):
        self.width = side
        self.height = side

    def set_height(self, side):
        self.width = side
        self.height = side

    def __str__(self):
        return f'Square(side={self.width})'


# Testing
r1 = Rectangle(2,3)
print(r1)
print(r1.set_width(15), r1)
print(r1.set_height(10), r1)
print(r1.get_area())
print(r1.get_perimeter())
print(r1.get_diagonal())
print(r1.get_picture())
r2 = Rectangle(58,48)
print(r2.get_picture())

s1 = Square(5)
print(s1)
print(s1.get_picture())
print(s1.get_picture())

print(r1.get_amount_inside(s1))

rec = Rectangle(4,8)
sq = Rectangle(3,6)
print(rec.get_amount_inside(sq))

print(Rectangle(15,10).get_amount_inside(Square(5)))
print(Rectangle(4,8).get_amount_inside(Rectangle(3, 6)))
print(Rectangle(2,3).get_amount_inside(Rectangle(3, 6)))
