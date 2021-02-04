import unittest

from solution import calculateRooms

class TestSolution(unittest.TestCase):
    def test_solution(self):
        """
        Test the provided example
        """
        data = [(30, 75), (0, 50), (60, 150)]
        result = calculateRooms(data)
        self.assertEqual(result, 2)

    def test_empty(self):
        """
        Test empty rooms
        """
        data = []
        result = calculateRooms(data)
        self.assertEqual(result, 0)

    def test_three(self):
        """
        Test three rooms needed
        """
        data = [(0, 15), (10, 15), (5, 15)]
        result = calculateRooms(data)
        self.assertEqual(result, 3)

if __name__ == '__main__':
    unittest.main()