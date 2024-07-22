import plotly.graph_objects as go
from package.shapes import *
from package.points import *

def menu():
    while True:
        print("\nEscolha uma opção:")
        print("1. Criar forma geométrica")
        print("2. Listar formas geométricas disponíveis")
        print("3. Calcular distância entre pontos")
        print("4. Verificar se ponto está dentro da forma")
        print("5. Verificar se ponto está próximo ao segmento de reta")
        print("6. Sair")

        choice = int(input("Digite o número da opção: "))

        if choice == 1:
            print("Escolha a figura geométrica:")
            print("1. Triângulo")
            print("2. Retângulo")
            print("3. Quadrado")
            print("4. Círculo")

            shape_choice = int(input("Digite o número da figura: "))

            if shape_choice == 1:
                print("Digite as coordenadas dos 3 pontos do triângulo:")
                points = []
                for i in range(3):
                    x = int(input(f"Ponto {i + 1} - x: "))
                    y = int(input(f"Ponto {i + 1} - y: "))
                    points.append(Point(x, y))
                shape = Triangle(*points)

            elif shape_choice == 2:
                print("Digite as coordenadas do ponto superior esquerdo e as dimensões do retângulo:")
                x = int(input("Ponto superior esquerdo - x: "))
                y = int(input("Ponto superior esquerdo - y: "))
                width = int(input("Largura: "))
                height = int(input("Altura: "))
                shape = Rectangle(Point(x, y), width, height)

            elif shape_choice == 3:
                print("Digite as coordenadas do ponto superior esquerdo e o lado do quadrado:")
                x = int(input("Ponto superior esquerdo - x: "))
                y = int(input("Ponto superior esquerdo - y: "))
                side_length = int(input("Comprimento do lado: "))
                shape = Square(Point(x, y), side_length)

            elif shape_choice == 4:
                print("Digite as coordenadas do centro e o raio do círculo:")
                x = int(input("Centro - x: "))
                y = int(input("Centro - y: "))
                radius = int(input("Raio: "))
                shape = Circle(x, y, radius)

            else:
                print("Escolha inválida.")
                continue

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

            # Plotting the shape
            fig = go.Figure()
            fig.add_trace(shape.plot())
            fig.update_layout(
                title="Visualização da Figura Geométrica",
                xaxis_title="X",
                yaxis_title="Y",
                xaxis=dict(scaleanchor='y', scaleratio=1),  # to keep the scale equal
            )
            fig.show()

        elif choice == 2:
            print("Formas geométricas disponíveis:")
            print("1. Triângulo")
            print("2. Retângulo")
            print("3. Quadrado")
            print("4. Círculo")

        elif choice == 3:
            print("Digite as coordenadas dos dois pontos:")
            x1 = int(input("Ponto 1 - x: "))
            y1 = int(input("Ponto 1 - y: "))
            x2 = int(input("Ponto 2 - x: "))
            y2 = int(input("Ponto 2 - y: "))

            point1 = Point(x1, y1)
            point2 = Point(x2, y2)

            print(f"A distância entre os pontos é: {point1.distance_to(point2)}")
            print(f"A distância do ponto 1 para a origem é: {point1.distance_to_origin()}")
            print(f"A distância do ponto 2 para a origem é: {point2.distance_to_origin()}")

        elif choice == 4:
            print("Digite as coordenadas do ponto:")
            x = int(input("Ponto - x: "))
            y = int(input("Ponto - y: "))

            point = Point(x, y)

            print("Escolha a figura geométrica:")
            print("1. Retângulo")
            print("2. Círculo")

            shape_choice = int(input("Digite o número da figura: "))

            if shape_choice == 1:
                print("Digite as coordenadas do ponto superior esquerdo e as dimensões do retângulo:")
                x = int(input("Ponto superior esquerdo - x: "))
                y = int(input("Ponto superior esquerdo - y: "))
                width = int(input("Largura: "))
                height = int(input("Altura: "))
                rectangle = Rectangle(Point(x, y), width, height)
                if rectangle.contains_point(point):
                    print("O ponto está dentro do retângulo.")
                else:
                    print("O ponto não está dentro do retângulo.")

            elif shape_choice == 2:
                print("Digite as coordenadas do centro e o raio do círculo:")
                x = int(input("Centro - x: "))
                y = int(input("Centro - y: "))
                radius = int(input("Raio: "))
                circle = Circle(x, y, radius)
                if circle.contains_point(point):
                    print("O ponto está dentro do círculo.")
                else:
                    print("O ponto não está dentro do círculo.")
            else:
                print("Escolha inválida.")

        elif choice == 5:
            print("Digite as coordenadas dos dois pontos do segmento de reta:")
            x1 = int(input("Ponto 1 - x: "))
            y1 = int(input("Ponto 1 - y: "))
            x2 = int(input("Ponto 2 - x: "))
            y2 = int(input("Ponto 2 - y: "))

            p1 = Point(x1, y1)
            p2 = Point(x2, y2)

            print("Digite as coordenadas do ponto a verificar:")
            x3 = int(input("Ponto 3 - x: "))
            y3 = int(input("Ponto 3 - y: "))

            p3 = Point(x3, y3)

            if point_near_line_segment(p1, p2, p3):
                print("O ponto está próximo ao segmento de reta.")
            else:
                print("O ponto não está próximo ao segmento de reta.")

        elif choice == 6:
            print("Encerrando o programa.")
            break

        else:
            print("Escolha inválida.")
