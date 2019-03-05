
import unittest

import Algoritmos


class Tests(unittest.TestCase):

    def test_quicksort(self):
        self.assertEqual(Algoritmos.quicksort([2, 34, 1, 257, 32, 3156, 23, 12, 13, 21], 0, 9), [
                         1, 2, 12, 13, 21, 23, 32, 34, 257, 3156])
        self.assertEqual(Algoritmos.quicksort([2, 34, 1, 257, 32, 3156, 23, 12, 13, 21], 0, 9), [
                         1, 2, 12, 13, 21, 23, 32, 34, 257, 3156])

    def test_bublesort(self):
        self.assertEqual(Algoritmos.bubbleSort([2, 34, 1, 257, 32, 3156, 23, 12, 13, 21]), [
                         1, 2, 12, 13, 21, 23, 32, 34, 257, 3156])


if __name__ == "__main__":
    unittest.main()

