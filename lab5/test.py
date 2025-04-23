import unittest
import math
from io import StringIO
import sys
from unittest.mock import patch
from mirasol_lab5 import (Triangle, Equilateral, Isosceles, Scalene, Right, 
                            Acute, Obtuse, Trapezoid, Parallelogram, Rectangle,
                            Rhombus, Square, Kite, Pentagon, Hexagon)

class TestInvalidShapes(unittest.TestCase):
    def setUp(self):
        self.held_output = StringIO()
        sys.stdout = self.held_output

    def tearDown(self):
        self.held_output.close()
        sys.stdout = sys.__stdout__

    def capture_output(self):
        self.held_output.seek(0)
        return self.held_output.read()

    # --- Triangle Validation Tests ---
    def test_invalid_equilateral(self):
        eq = Equilateral()
        with patch('builtins.input', side_effect=['-5', '0', '5']):
            eq.getLengths()
            output = self.capture_output()
            self.assertIn("greater than 0", output)
            self.assertEqual(eq.a, 5)  # Should finally accept valid input

    def test_invalid_isosceles(self):
        iso = Isosceles()
        # Test: equal sides a and c (invalid), then valid input
        with patch('builtins.input', side_effect=['5', '5', '6', '5']):
            iso.getLengths()
            output = self.capture_output()
            self.assertIn("should not be equal to side length (c)", output)
            self.assertEqual(iso.a, 6)
            self.assertEqual(iso.c, 5)

        # Test: triangle inequality violation
        with patch('builtins.input', side_effect=['1', '1', '3', '8', '3', '2']):
            iso.getLengths()
            output = self.capture_output()
            self.assertIn("sum of side lengths", output)
            self.assertEqual(iso.c, 2)  # Last valid input

    def test_invalid_scalene(self):
        sc = Scalene()
        # Test: all sides equal (invalid)
        with patch('builtins.input', side_effect=['5', '5', '5', '3', '4', '5']):
            sc.getLengths()
            output = self.capture_output()
            self.assertIn("should all be different", output)
            self.assertEqual(sc.a, 3)
            self.assertEqual(sc.b, 4)
            self.assertEqual(sc.c, 5)

    def test_invalid_right_triangle_angles(self):
        rt = Right()
        # Test: angles don't sum to 180
        with patch('builtins.input', side_effect=['60', '60', '90', '45', '45', '45']):
            rt.getAngles()
            output = self.capture_output()
            self.assertIn("sum of angles", output)
            self.assertEqual(rt.C, 45)  # Last valid input

        # Test: two angles >= 90
        with patch('builtins.input', side_effect=['90', '45', '100', '0', '60', '30', '10']):
            rt.getAngles()
            output = self.capture_output()
            self.assertIn("greater than 0", output)
            self.assertEqual(rt.C, 30)

    # --- Quadrilateral Validation Tests ---
    def test_invalid_trapezoid(self):
        trap = Trapezoid()
        # Test: bases equal
        with patch('builtins.input', side_effect=['5', '5', '4', '6', '4', '9']):
            trap.getLengths()
            output = self.capture_output()
            self.assertIn("should be different", output)
            self.assertEqual(trap.base_2, 4)  # Last valid input

    def test_invalid_parallelogram_angles(self):
        para = Parallelogram()
        # Test: angle = 90 (invalid for parallelogram)
        with patch('builtins.input', side_effect=['90', '60']):
            para.getAngles()
            output = self.capture_output()
            self.assertIn("equal to (90)", output)
            self.assertEqual(para.A, 60)

    def test_invalid_kite_sides(self):
        kite = Kite()
        # Test: adjacent sides equal (invalid for kite)
        with patch('builtins.input', side_effect=['5', '5', '4', '3']):
            kite.getLengths()
            output = self.capture_output()
            self.assertIn("should have different lengths", output)
            self.assertEqual(kite.b, 3)  # Last valid input

    # --- Regular Polygon Validation Tests ---
    def test_invalid_pentagon(self):
        pent = Pentagon()
        with patch('builtins.input', side_effect=['0', '-5', '5']):
            pent.getLengths()
            output = self.capture_output()
            self.assertIn("greater than 0", output)
            self.assertEqual(pent.a, 5)

    def test_invalid_hexagon(self):
        hex = Hexagon()
        with patch('builtins.input', side_effect=['-1', '0', '5']):
            hex.getLengths()
            output = self.capture_output()
            self.assertIn("greater than 0", output)
            self.assertEqual(hex.a, 5)

    # --- Comprehensive Angle Validation ---
    def test_acute_triangle_validation(self):
        ac = Acute()
        # Test: angle >= 90
        with patch('builtins.input', side_effect=['90', '45', '45', '80', '50', '50']):
            ac.getAngles()
            output = self.capture_output()
            self.assertIn("less than (90) degrees", output)
            self.assertEqual(ac.A, 80)

    def test_obtuse_triangle_validation(self):
        obt = Obtuse()
        # Test: no angle > 90
        with patch('builtins.input', side_effect=['60', '60', '60', '100', '40', '40']):
            obt.getAngles()
            output = self.capture_output()
            self.assertIn("greater than (90) degrees", output)
            self.assertEqual(obt.A, 100)

if __name__ == '__main__':
    unittest.main()