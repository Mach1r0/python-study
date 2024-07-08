class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Borda:
    def __init__(self, points):
        self.points = points  # A list of Point objects

    def draw(self):
        raise NotImplementedError("Subclass must implement abstract method")
    
    def calculate_area(self):
        raise NotImplementedError("Subclass must implement abstract method")
    
    def calculate_perimeter(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Triangle(Borda):
    def __init__(self, p1, p2, p3):
        super().__init__([p1, p2, p3])

    def draw(self):
        print("Drawing Triangle with points:")
        for point in self.points:
            print(f"({point.x}, {point.y})")
    
    def calculate_area(self):
        # Basic implementation for the area of a triangle (assuming the points form a valid triangle)
        pass

    def calculate_perimeter(self):
        # Basic implementation for the perimeter of a triangle
        pass

class Rectangle(Borda):
    def __init__(self, p1, p2, p3, p4):
        super().__init__([p1, p2, p3, p4])

    def draw(self):
        print("Drawing Rectangle with points:")
        for point in self.points:
            print(f"({point.x}, {point.y})")
    
    def calculate_area(self):
        # Basic implementation for the area of a rectangle
        pass

    def calculate_perimeter(self):
        # Basic implementation for the perimeter of a rectangle
        pass

class Hexagon(Borda):
    def __init__(self, p1, p2, p3, p4, p5, p6):
        super().__init__([p1, p2, p3, p4, p5, p6])

    def draw(self):
        print("Drawing Hexagon with points:")
        for point in self.points:
            print(f"({point.x}, {point.y})")

    def calculate_area(self):
        # Basic implementation for the area of a hexagon
        pass

    def calculate_perimeter(self):
        # Basic implementation for the perimeter of a hexagon
        pass

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


def main():
    print("Escolha a figura geométrica:")
    print("1. Triângulo")
    print("2. Retângulo")
    print("3. Hexágono")
    print("4. Octágono")
    print("5. Eneágono")

    choice = int(input("Digite o número da figura: "))

    points = []
    if choice == 1:
        print("Digite as coordenadas dos 3 pontos do triângulo:")
        for i in range(3):
            x = int(input(f"Ponto {i+1} - x: "))
            y = int(input(f"Ponto {i+1} - y: "))
            points.append(Point(x, y))
        shape = Triangle(*points)

    elif choice == 2:
        print("Digite as coordenadas dos 4 pontos do retângulo:")
        for i in range(4):
            x = int(input(f"Ponto {i+1} - x: "))
            y = int(input(f"Ponto {i+1} - y: "))
            points.append(Point(x, y))
        shape = Rectangle(*points)

    elif choice == 3:
        print("Digite as coordenadas dos 6 pontos do hexágono:")
        for i in range(6):
            x = int(input(f"Ponto {i+1} - x: "))
            y = int(input(f"Ponto {i+1} - y: "))
            points.append(Point(x, y))
        shape = Hexagon(*points)

    elif choice == 4:
        print("Digite as coordenadas dos 8 pontos do octágono:")
        for i in range(8):
            x = int(input(f"Ponto {i+1} - x: "))
            y = int(input(f"Ponto {i+1} - y: "))
            points.append(Point(x, y))
        shape = Octagon(*points)

    elif choice == 5:
        print("Digite as coordenadas dos 9 pontos do eneágono:")
        for i in range(9):
            x = int(input(f"Ponto {i+1} - x: "))
            y = int(input(f"Ponto {i+1} - y: "))
            points.append(Point(x, y))
        shape = Nonagon(*points)

    else:
        print("Escolha inválida.")
        return

    shape.draw()

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
