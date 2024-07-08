import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Borda:
    def __init__(self, points):
        self.points = points  

class Line(Point):
    def __init__(self, x, y):
        super().__init__(x, y)
    pass 

class Triangle(Line):
    def __init__(self, p1, p2, p3):
        super().__init__([p1, p2, p3])

    def draw(self):
        print("Drawing Triangle with points:")
        for point in self.points:
            print(f"({point.x}, {point.y})")
    
    def calculate_area(self):
        pass

    def calculate_perimeter(self):
        pass

class Circle(Point):
    def __init__(self, n, x, y, radius):
        super().__init__(n, x, y)
        self.radius = radius

class Rectangle(Borda):
    def __init__(self, top_left, bottom_right):
        # Calcula os outros dois pontos com base nos pontos dados
        top_right = Point(bottom_right.x, top_left.y)
        bottom_left = Point(top_left.x, bottom_right.y)
        super().__init__([top_left, top_right, bottom_right, bottom_left])
    
    def calculate_area(self):
        width = self.points[1].x - self.points[0].x
        height = self.points[0].y - self.points[3].y
        return width * height

    def calculate_perimeter(self):
        width = self.points[1].x - self.points[0].x
        height = self.points[0].y - self.points[3].y
        return 2 * (width + height)

class Square(Borda):
    def __init__(self, top_left, side_length):
        top_right = Point(top_left.x + side_length, top_left.y)
        bottom_left = Point(top_left.x, top_left.y - side_length)
        bottom_right = Point(top_left.x + side_length, top_left.y - side_length)
        super().__init__([top_left, top_right, bottom_right, bottom_left])
    
    def calculate_area(self):
        return self.points[0].x * self.points[0].x

    def calculate_perimeter(self):
        return 4 * self.points[0].x
    
class Hexagon(Borda):
    def __init__(self, center, side_length):
        self.center = center
        self.side_length = side_length
        # Aqui você pode calcular os pontos se necessário, mas não é obrigatório para calcular área e perímetro
        # super().__init__([p1, p2, p3, p4, p5, p6])

    def calculate_area(self):
        return (3 * math.sqrt(3) / 2) * (self.side_length ** 2)

    def calculate_perimeter(self):
        return 6 * self.side_length

class Octagon(Borda):
    def __init__(self, p1, p2, p3, p4, p5, p6, p7, p8):
        super().__init__([p1, p2, p3, p4, p5, p6, p7, p8])

    def draw(self):
        print("Drawing Octagon with points:")
        for point in self.points:
            print(f"({point.x}, {point.y})")

    def calculate_area(self):
        # Basic implementation for the area of an octagon
        pass

    def calculate_perimeter(self):
        # Basic implementation for the perimeter of an octagon
        pass

class Nonagon(Borda):
    def __init__(self, p1, p2, p3, p4, p5, p6, p7, p8, p9):
        super().__init__([p1, p2, p3, p4, p5, p6, p7, p8, p9])

    def draw(self):
        print("Drawing Nonagon with points:")
        for point in self.points:
            print(f"({point.x}, {point.y})")

    def calculate_area(self):
        # Basic implementation for the area of a nonagon
        pass

    def calculate_perimeter(self):
        # Basic implementation for the perimeter of a nonagon
        pass

# Example usage:
p1 = Point(0, 0)
p2 = Point(1, 0)
p3 = Point(1, 1)
p4 = Point(0, 1)
p5 = Point(2, 0)
p6 = Point(2, 1)
p7 = Point(0, 2)
p8 = Point(2, 2)
p9 = Point(1, 2)

shapes = [
    Triangle(p1, p2, p3),
    Rectangle(p1, p2, p3, p4),
    Hexagon(p1, p2, p3, p4, p5, p6),
    Octagon(p1, p2, p3, p4, p5, p6, p7, p8),
    Nonagon(p1, p2, p3, p4, p5, p6, p7, p8, p9)
]

for shape in shapes:
    shape.draw()
