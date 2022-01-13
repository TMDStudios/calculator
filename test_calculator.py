import unittest
import calculator

class TestCalculator(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(calculator.calculate(2, "+", 2), 4.0)
        self.assertEqual(calculator.calculate(-2, "+", 2.5), 0.5)
        self.assertEqual(calculator.calculate(-2, "+", -2), -4.0)

    def test_subtraction(self):
        self.assertEqual(calculator.calculate(2, "-", 2), 0.0)
        self.assertEqual(calculator.calculate(-2, "-", 2.5), -4.5)
        self.assertEqual(calculator.calculate(-2, "-", -2), 0.0)

    def test_multiplication(self):
        self.assertEqual(calculator.calculate(2, "*", 2), 4.0)
        self.assertEqual(calculator.calculate(-2, "*", 2.5), -5.0)
        self.assertEqual(calculator.calculate(-2, "*", -2), 4.0)

    def test_division(self):
        self.assertEqual(calculator.calculate(2, "/", 2), 1.0)
        self.assertEqual(calculator.calculate(-5, "/", 2.5), -2.0)
        self.assertEqual(calculator.calculate(-2, "/", -2), 1.0)
