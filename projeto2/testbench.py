import unittest
import io
import sys
import math
from package.points import Point
from package.shapes import Rectangle, Square, Triangle, Circle, point_near_line_segment

class TestShapes(unittest.TestCase):
    
    def capture_print_output(self, func, *args, **kwargs):
        """Helper function to capture print statements."""
        with io.StringIO() as buf:
            sys.stdout = buf
            try:
                func(*args, **kwargs)
            finally:
                sys.stdout = sys.__stdout__
            return buf.getvalue()

    def test_point(self):
        p1 = Point(3, 4)
        p2 = Point(6, 8)
        
        # Capture and test coordinates printing
        output = self.capture_print_output(p1.printCoord)
        self.assertIn('O ponto possui as coord: (3, 4).', output)
        
        # Test distance calculations
        self.assertAlmostEqual(p1.distance_to(p2), 5)
        self.assertAlmostEqual(p1.distance_to_origin(), 5)

    def test_rectangle(self):
        top_left = Point(0, 10)
        rect = Rectangle(top_left, 5, 3)
        
        # Capture and test coordinates printing
        output = self.capture_print_output(rect.printCoord)
        self.assertIn('Retângulo com pontos:', output)
        self.assertIn('Ponto 1: (0, 10)', output)
        self.assertIn('Ponto 2: (5, 10)', output)
        self.assertIn('Ponto 3: (5, 7)', output)
        self.assertIn('Ponto 4: (0, 7)', output)
        
        # Test area and perimeter
        self.assertEqual(rect.calculate_area(), 15)
        self.assertEqual(rect.calculate_perimeter(), 16)
        
        # Test point containment
        inside_point = Point(2, 8)
        outside_point = Point(6, 12)
        self.assertTrue(rect.contains_point(inside_point))
        self.assertFalse(rect.contains_point(outside_point))
        
    def test_square(self):
        top_left = Point(0, 10)
        sq = Square(top_left, 4)
        
        # Capture and test coordinates printing
        output = self.capture_print_output(sq.printCoord)
        self.assertIn('Quadrado com pontos:', output)
        self.assertIn('Ponto 1: (0, 10)', output)
        self.assertIn('Ponto 2: (4, 10)', output)
        self.assertIn('Ponto 3: (4, 6)', output)
        self.assertIn('Ponto 4: (0, 6)', output)
        
        # Test area and perimeter
        self.assertEqual(sq.calculate_area(), 16)
        self.assertEqual(sq.calculate_perimeter(), 16)
        
        # Test point containment
        inside_point = Point(2, 8)
        outside_point = Point(5, 12)
        self.assertTrue(sq.contains_point(inside_point))
        self.assertFalse(sq.contains_point(outside_point))

    def test_triangle(self):
        p1 = Point(0, 0)
        p2 = Point(4, 0)
        p3 = Point(2, 3)
        tri = Triangle(p1, p2, p3)
        
        # Capture and test coordinates printing
        output = self.capture_print_output(tri.printCoord)
        self.assertIn('Ponto 1: (0, 0)', output)
        self.assertIn('Ponto 2: (4, 0)', output)
        self.assertIn('Ponto 3: (2, 3)', output)
        
        # Test area and perimeter
        self.assertAlmostEqual(tri.calculate_area(), 6)
        self.assertAlmostEqual(tri.calculate_perimeter(), 11.21110255092798, places=2)

    def test_circle(self):
        circle = Circle(0, 0, 5)
        
        # Capture and test coordinates printing
        output = self.capture_print_output(circle.printCoord)
        self.assertIn('O círculo com centro (0, 0) e raio 5.', output)
        
        # Test area and perimeter
        self.assertAlmostEqual(circle.calculate_area(), math.pi * 25)
        self.assertAlmostEqual(circle.calculate_perimeter(), 2 * math.pi * 5)
        
        # Test point containment
        inside_point = Point(3, 4)
        outside_point = Point(6, 6)
        self.assertTrue(circle.contains_point(inside_point))
        self.assertFalse(circle.contains_point(outside_point))

    def test_point_near_line_segment(self):
        p1 = Point(0, 0)
        p2 = Point(4, 0)
        p3 = Point(2, 1)
        self.assertTrue(point_near_line_segment(p1, p2, p3))
        
        p3 = Point(5, 1)
        self.assertFalse(point_near_line_segment(p1, p2, p3))

if __name__ == '__main__':
    unittest.main()
