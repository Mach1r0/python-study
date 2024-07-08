from models import Point, Triangle, Rectangle, Hexagon, Octagon, Nonagon

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
