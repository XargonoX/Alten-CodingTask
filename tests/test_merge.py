import unittest
from merge import merge
import numpy as np

class TestMerge(unittest.TestCase):
    def test_merge(self):
        testIntervalList = [
            np.ndarray(shape=(2,), buffer=np.array([4, 6]), dtype='int'),
            np.ndarray(shape=(2,), buffer=np.array([1, 2]), dtype='int'),
            np.ndarray(shape=(2,), buffer=np.array([3, 10]), dtype='int'),
            np.ndarray(shape=(2,), buffer=np.array([20, 25]), dtype='int'),
            np.ndarray(shape=(2,), buffer=np.array([15, 9]), dtype='int'), #intentionally reversed
            np.ndarray(shape=(2,), buffer=np.array([2, 3]), dtype='int'),
            np.ndarray(shape=(2,), buffer=np.array([23, 30]), dtype='int'),
            np.ndarray(shape=(2,), buffer=np.array([5, 5]), dtype='int'),
        ]

        targetResultIntervalList = [
            np.ndarray(shape=(2,), buffer=np.array([2, 15]), dtype='int'),
            np.ndarray(shape=(2,), buffer=np.array([1, 2]), dtype='int'),
            np.ndarray(shape=(2,), buffer=np.array([20, 30]), dtype='int'),
        ]

        resultIntervalList = merge(testIntervalList)
        self.assertTrue(np.array_equal(resultIntervalList, targetResultIntervalList))


if __name__ == '__main__':
    unittest.main()
