import unittest
from delta_weight import *

class TestDeltaWeight(unittest.TestCase):

    def test_no_diff(self):
        eta = 0.3
        y_act = 0
        y_pred = 0
        x = 1
        result = delta_weight(eta, y_act, y_pred, x)
        self.assertEqual(result, 0)

    def test_no_diff_pos(self):
        eta = 0.3
        y_act = 1
        y_pred = 1
        x = 1
        result = delta_weight(eta, y_act, y_pred, x)
        self.assertEqual(result, 0)

    def test_diff_pos(self):
        eta = 0.3
        y_act = 1
        y_pred = 0
        x = 1
        result = delta_weight(eta, y_act, y_pred, x)
        self.assertEqual(result, 0.3)

    def test_diff_neg(self):
        eta = 0.3
        y_act = 0
        y_pred = 1
        x = 1
        result = delta_weight(eta, y_act, y_pred, x)
        self.assertEqual(result, -0.3)

    def test_no_diff_inzero(self):
        eta = 0.3
        y_act = 0
        y_pred = 0
        x = 0
        result = delta_weight(eta, y_act, y_pred, x)
        self.assertEqual(result, 0)

    def test_no_diff_pos_inzero(self):
        eta = 0.3
        y_act = 1
        y_pred = 1
        x = 0
        result = delta_weight(eta, y_act, y_pred, x)
        self.assertEqual(result, 0)

    def test_diff_pos_inzero(self):
        eta = 0.3
        y_act = 1
        y_pred = 0
        x = 0
        result = delta_weight(eta, y_act, y_pred, x)
        self.assertEqual(result, 0)

    def test_diff_neg_inzero(self):
        eta = 0.3
        y_act = 1
        y_pred = 0
        x = 0
        result = delta_weight(eta, y_act, y_pred, x)
        self.assertEqual(result, 0)

if __name__ == '__main__':
    unittest.main()
