import unittest
from ..grades import calculate_average

class TestCalculateAverage(unittest.TestCase):
    
    def test_average(self):
        self.assertEqual(calculate_average([10, 20, 30]), 20)

    def test_empty_list(self):
        self.assertEqual(calculate_average([]), 0)

if __name__ == '__main__':
    unittest.main()