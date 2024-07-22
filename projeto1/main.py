import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def printCoord(self):
        print(f'O ponto possui as coord: ({self.x}, {self.y}).')

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
        p1, p2, p3 = self.points
        side1 = math.sqrt((p2.x - p1.x) ** 2 + (p2.y - p1.y) ** 2)
        side2 = math.sqrt((p3.x - p2.x) ** 2 + (p3.y - p2.y) ** 2)
        side3 = math.sqrt((p1.x - p3.x) ** 2 + (p1.y - p3.y) ** 2)
        
        print(f'Side 1: {side1}, Side 2: {side2}, Side 3: {side3}')
        return side1 + side2 + side3

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

# O script principal para interação com o usuário
def main():
    print("Escolha a figura geométrica:")
    print("1. Triângulo")
    print("2. Retângulo")
    print("3. Quadrado")
    print("4. Círculo")

    choice = int(input("Digite o número da figura: "))

    if choice == 1:
        print("Digite as coordenadas dos 3 pontos do triângulo:")
        points = []
        for i in range(3):
            x = int(input(f"Ponto {i+1} - x: "))
            y = int(input(f"Ponto {i+1} - y: "))
            points.append(Point(x, y))
        shape = Triangle(*points)

    elif choice == 2:
        print("Digite as coordenadas do ponto superior esquerdo e as dimensões do retângulo:")
        x = int(input("Ponto superior esquerdo - x: "))
        y = int(input("Ponto superior esquerdo - y: "))
        width = int(input("Largura: "))
        height = int(input("Altura: "))
        shape = Rectangle(Point(x, y), width, height)

    elif choice == 3:
        print("Digite as coordenadas do ponto superior esquerdo e o lado do quadrado:")
        x = int(input("Ponto superior esquerdo - x: "))
        y = int(input("Ponto superior esquerdo - y: "))
        side_length = int(input("Comprimento do lado: "))
        shape = Square(Point(x, y), side_length)

    elif choice == 4:
        print("Digite as coordenadas do centro e o raio do círculo:")
        x = int(input("Centro - x: "))
        y = int(input("Centro - y: "))
        radius = int(input("Raio: "))
        shape = Circle(x, y, radius)

    else:
        print("Escolha inválida.")
        return

    shape.printCoord()

    print("Escolha o cálculo a ser realizado:")
    print("1. Área")
    print("2. Perímetro")

    calc_choice = int(input("Digite o número do cálculo: "))

    if calc_choice == 1:
        print(f"A área da figura é: {shape.calculate_area()}")
    elif calc_choice == 2:
        print(f"O perímetro da figura é: {shape.calculate_perimeter()}")
    else:
        print("Escolha inválida.")

if __name__ == "__main__":
    main()
