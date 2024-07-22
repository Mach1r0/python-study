import math 
from .points import Point
import plotly.graph_objects as go

class Rectangle:
    def __init__(self, top_left, width, height):
        self.top_left = top_left
        self.width = width
        self.height = height

    def printCoord(self):
        top_right = Point(self.top_left.x + self.width, self.top_left.y)
        bottom_left = Point(self.top_left.x, self.top_left.y - self.height)
        bottom_right = Point(self.top_left.x + self.width, self.top_left.y - self.height)
        print(f'Retângulo com pontos:')
        print(f'Ponto 1: ({self.top_left.x}, {self.top_left.y})')
        print(f'Ponto 2: ({top_right.x}, {top_right.y})')
        print(f'Ponto 3: ({bottom_right.x}, {bottom_right.y})')
        print(f'Ponto 4: ({bottom_left.x}, {bottom_left.y})')

    def calculate_area(self):
        return self.width * self.height

    def calculate_perimeter(self):
        return 2 * (self.width + self.height)

    def contains_point(self, point):
        return (self.top_left.x <= point.x <= self.top_left.x + self.width and
                self.top_left.y >= point.y >= self.top_left.y - self.height)

    def plot(self):
        top_right = Point(self.top_left.x + self.width, self.top_left.y)
        bottom_left = Point(self.top_left.x, self.top_left.y - self.height)
        bottom_right = Point(self.top_left.x + self.width, self.top_left.y - self.height)

        x_coords = [self.top_left.x, top_right.x, bottom_right.x, bottom_left.x, self.top_left.x]
        y_coords = [self.top_left.y, top_right.y, bottom_right.y, bottom_left.y, self.top_left.y]

        return go.Scatter(x=x_coords, y=y_coords, mode='lines', name='Rectangle')

class Square(Rectangle):
    def __init__(self, top_left, side_length):
        super().__init__(top_left, side_length, side_length)

    def printCoord(self):
        top_right = Point(self.top_left.x + self.width, self.top_left.y)
        bottom_left = Point(self.top_left.x, self.top_left.y - self.height)
        bottom_right = Point(self.top_left.x + self.width, self.top_left.y - self.height)
        print(f'Quadrado com pontos:')
        print(f'Ponto 1: ({self.top_left.x}, {self.top_left.y})')
        print(f'Ponto 2: ({top_right.x}, {top_right.y})')
        print(f'Ponto 3: ({bottom_right.x}, {bottom_right.y})')
        print(f'Ponto 4: ({bottom_left.x}, {bottom_left.y})')

class Triangle:
    def __init__(self, p1, p2, p3):
        self.points = [p1, p2, p3]

    def printCoord(self):
        for i, point in enumerate(self.points):
            print(f'Ponto {i + 1}: ({point.x}, {point.y})')

    def calculate_area(self):
        p1, p2, p3 = self.points
        
        return abs(p1.x * (p2.y - p3.y) + p2.x * (p3.y - p1.y) + p3.x * (p1.y - p2.y)) / 2
    
    def calculate_perimeter(self):
        p1, p2, p3 = self.points
        side1 = math.sqrt((p2.x - p1.x) ** 2 + (p2.y - p1.y) ** 2)
        side2 = math.sqrt((p3.x - p2.x) ** 2 + (p3.y - p2.y) ** 2)
        side3 = math.sqrt((p1.x - p3.x) ** 2 + (p1.y - p3.y) ** 2)
        
        return side1 + side2 + side3

class Circle(Point):
    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius

    def printCoord(self):
        print(f'O círculo com centro ({self.x}, {self.y}) e raio {self.radius}.')

    def calculate_area(self):
        return math.pi * self.radius ** 2

    def calculate_perimeter(self):
        return 2 * math.pi * self.radius

    def contains_point(self, point):
        return self.distance_to(point) <= self.radius

    def plot(self):
        theta = [i * (2 * math.pi / 100) for i in range(101)]
        x_circle = [self.x + self.radius * math.cos(t) for t in theta]
        y_circle = [self.y + self.radius * math.sin(t) for t in theta]

        return go.Scatter(x=x_circle, y=y_circle, mode='lines', name='Circle')

def point_near_line_segment(p1, p2, p3, tolerance=1.0):
    def distance_squared(x0, y0, x1, y1, x2, y2):
        dx = x2 - x1
        dy = y2 - y1
        if dx == 0 and dy == 0:
            return (x0 - x1) ** 2 + (y0 - y1) ** 2
        t = max(0, min(1, ((x0 - x1) * dx + (y0 - y1) * dy) / (dx * dx + dy * dy)))
        x_proj = x1 + t * dx
        y_proj = y1 + t * dy
        return (x0 - x_proj) ** 2 + (y0 - y_proj) ** 2

    dist_sq = distance_squared(p3.x, p3.y, p1.x, p1.y, p2.x, p2.y)
    return dist_sq <= tolerance ** 2
