import unittest
from list_arithmetic import *

class ListArithmeticTest(unittest.TestCase):

    def test_sum_prod_empty_lists(self):
        ls1 = list()
        ls2 = list()
        result = sum_prod(ls1, ls2)
        self.assertEqual(result, 0)

    def test_sum_prod_singleton_lists_with_zero(self):
        ls1 = [1]
        ls2 = [0]
        result = sum_prod(ls1, ls2)
        self.assertEqual(result, 0)

    def test_sum_prod_singleton_lists_no_zero(self):
        ls1 = [1]
        ls2 = [2]
        result = sum_prod(ls1, ls2)
        self.assertEqual(result, 2)

    def test_sum_prod_singleton_lists_no_unit(self):
        ls1 = [15]
        ls2 = [2]
        result = sum_prod(ls1, ls2)
        self.assertEqual(result, 30)

    def test_sum_prod_longer_lists(self):
        ls1 = [15, 1, 3, 24]
        ls2 = [2, 1, 12, 2]
        result = sum_prod(ls1, ls2)
        self.assertEqual(result, 115)

if __name__ == '__main__':
    unittest.main()
