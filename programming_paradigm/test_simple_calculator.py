

import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
    def test_one_negative_addition(self):
        self.assertEqual(self.calc.add(-1, 1), 0)
    def test_both_negative_addition(self):
        self.assertEqual(self.calc.add(-3,-4), -7)
    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(6,5), 1)
    def test_bigger_number_negative_subtraction(self):
        self.assertEqual(self.calc.subtract(-10, 7), -17)
    def test_smaller_number_negative_subtraction(self):
        self.assertEqual(self.calc.subtract(10, -7), 17)
    def test_both_negative_subtraction(self):
        self.assertEqual(self.calc.subtract(-4,-1), -3)
    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(3,4), 12)
    def test_one_negative_multiplication(self):
        self.assertEqual(self.calc.multiply(-3, 4), -12)
    def test_both_negative_multiplication(self):
        self.assertEqual(self.calc.multiply(-3,-4), 12)
    def test_division(self):
        self.assertEqual(self.calc.divide(10,5), 2)
    def test_byzero_division(self):
        self.assertEqual(self.calc.divide(4,0), "None")
    def test_one_negative_division(self):
        self.assertEqual(self.calc.divide(-10, 5), -2)
    def test_both_negative_division(self):
        self.assertEqual(self.calc.divide(-10,-5), 2)

       

if __name__ == "__main__":
     unittest.main()
   