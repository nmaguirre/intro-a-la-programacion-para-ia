import unittest
from activation import *

class TestActivation(unittest.TestCase):

    def test_smaller_than_threshold(self):
        result = step_activation(1)
        self.assertEqual(result, 0)

    def test_just_below_threshold(self):
        result = step_activation(theta - 0.001)
        self.assertEqual(result, 0)

    def test_threshold(self):
        result = step_activation(theta)
        self.assertEqual(result, 1)

    def test_just_above_threshold(self):
        result = step_activation(theta + 0.001)
        self.assertEqual(result, 1)

    def test_over_threshold(self):
        result = step_activation(175)
        self.assertEqual(result, 1)

if __name__ == '__main__':
    unittest.main()
