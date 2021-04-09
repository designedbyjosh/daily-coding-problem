import unittest

from solution import solve

class TestSolution(unittest.TestCase):
    def test_b_0_small(self):
        """
        Test that y is returned when b is 0
        """
        x = 1
        y = 2
        b = 0
        result = solve(x, y, b)
        self.assertEqual(result, y)

    def test_b_1_small(self):
        """
        Test that x is returned when b is 1
        """
        x = 1
        y = 2
        b = 1
        result = solve(x, y, b)
        self.assertEqual(result, x)

    def test_b_0_large(self):
        """
        Test that y is returned when b is 0
        """
        x = 30412
        y = 24123
        b = 0
        result = solve(x, y, b)
        self.assertEqual(result, y)

    def test_b_1_large(self):
        """
        Test that x is returned when b is 1
        """
        x = 30412
        y = 24123
        b = 1
        result = solve(x, y, b)
        self.assertEqual(result, x)

if __name__ == '__main__':
    unittest.main()