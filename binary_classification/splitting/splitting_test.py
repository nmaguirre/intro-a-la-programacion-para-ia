import unittest
from splitting import *

class SplittingTest(unittest.TestCase):

    def test_tuple_split_singleton(self):
        ts = tuple([1])
        result = tuple_split(ts)
        self.assertEqual(result, (tuple(), 1))

    def test_tuple_split_pair(self):
        ts = (1, 2)
        result = tuple_split(ts)
        self.assertEqual(result, (tuple([1]), 2))

    def test_tuple_split_triple(self):
        ts = (1, 2, 3)
        result = tuple_split(ts)
        self.assertEqual(result, ((1, 2), 3))

    def test_to_binary_singleton_one(self):
        ts = tuple([1])
        result = to_binary(ts, 1)
        self.assertEqual(result, ts)

    def test_to_binary_pair_one(self):
        ts = (1, 2)
        result = to_binary(ts, 2)
        self.assertEqual(result, (1, 1))

    def test_to_binary_triple_one(self):
        ts = (1, 2, 3)
        result = to_binary(ts, 3)
        self.assertEqual(result, (1, 2, 1))

    def test_to_binary_singleton_zero(self):
        ts = tuple([1])
        result = to_binary(ts, 3)
        self.assertEqual(result, tuple([0]))

    def test_to_binary_pair_zero(self):
        ts = (1, 2)
        result = to_binary(ts, False)
        self.assertEqual(result, (1, 0))

    def test_to_binary_triple_zero(self):
        ts = (1, 2, 3)
        result = to_binary(ts, "3")
        self.assertEqual(result, (1, 2, 0))

if __name__ == '__main__':
    unittest.main()
