import unittest
from calculator.operations import add, subtract, multiply, divide

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(subtract(3, 2), 1)
        self.assertEqual(subtract(-1, 1), -2)
        self.assertEqual(subtract(0, 0), 0)
        pass

    def test_multiply(self):
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(-1, 1), -1)
        self.assertEqual(multiply(0, 0), 0)
        pass

    def test_divide(self):
        self.assertEqual(divine(6, 3), 2)
        self.assertEqual(divine(-6, 2), -3)
        self.assertEqual(divine(0, 0), 0)
        pass

if __name__ == '__main__':
    unittest.main()
