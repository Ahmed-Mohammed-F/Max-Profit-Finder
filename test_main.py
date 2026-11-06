import random
import unittest
from main import find_profit_divide_conquer, find_profit_linear

class ProfitTests(unittest.TestCase):
    def test_typical(self):
        a = [10, 7, 5, 8, 11, 9]
        self.assertEqual(find_profit_divide_conquer(a), (2, 4, 6))
    def test_no_profit(self):
        self.assertEqual(find_profit_divide_conquer([9, 7, 3]), (None, None, 0))
    def test_one_day(self):
        self.assertEqual(find_profit_divide_conquer([5]), (None, None, 0))
    def test_against_linear(self):
        random.seed(7)
        for _ in range(100):
            values = [random.randint(1, 100) for _ in range(25)]
            self.assertEqual(find_profit_divide_conquer(values)[2],
                             find_profit_linear(values)[2])

if __name__ == '__main__':
    unittest.main()
