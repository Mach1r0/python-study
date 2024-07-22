import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def printCoord(self):
        print(f'O ponto possui as coord: ({self.x}, {self.y}).')

    def to_tuple(self):
        return (self.x, self.y)

    def distance_to(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

    def distance_to_origin(self):
        origin = Point(0, 0)
        return self.distance_to(origin)