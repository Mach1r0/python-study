from main import Point, Circle, Rectangle, Square, Triangle
import math

def test_shapes():
    # Create a Point and print its coordinates
    pt1 = Point(1, 12)
    pt1.printCoord()

    # Create a Circle and print its information
    circ2 = Circle(2, 13, 4)
    circ2.printCoord()

    # Create a Rectangle
    rect = Rectangle(Point(0, 0), 5, 3)
    print("\nPrinting Rectangle details:")
    rect.printCoord()
    print(f'Área: {rect.calculate_area()}')
    print(f'Perímetro: {rect.calculate_perimeter()}')

    # Create a Square
    sqr = Square(Point(-1, 1), 4)
    print("\nPrinting Square details:")
    sqr.printCoord()
    print(f'Área: {sqr.calculate_area()}')
    print(f'Perímetro: {sqr.calculate_perimeter()}')

    # Create a Triangle
    tri = Triangle(Point(0, 0), Point(3, 0), Point(0, 4))
    print("\nPrinting Triangle details:")
    tri.printCoord()
    print(f'Área: {tri.calculate_area()}')
    print(f'Perímetro: {tri.calculate_perimeter()}')

    # Ask for Circle calculation
    print("\nCalculating Circle area and perimeter:")
    print(f'A área do círculo é: {circ2.calculate_area()}')
    print(f'O perímetro do círculo é: {circ2.calculate_perimeter()}')

if __name__ == "__main__":
    test_shapes()
