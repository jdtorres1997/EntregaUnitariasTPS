
import unittest

import Algoritmos


class Tests(unittest.TestCase):
    def test_quicksort(self):
        self.assertEqual(Algoritmos.quicksort([1, 2, 3], 0, 2), [1, 2, 3])
        self.assertEqual(Algoritmos.quicksort(
            [1, 2, 3, 4, 5], 0, 4), [1, 2, 3, 4, 5])

    def test_bublesort(self):
        self.assertEqual(Algoritmos.bubbleSort([1]), [1])
        self.assertEqual(Algoritmos.bubbleSort([2, 1]), [1, 2])
        self.assertEqual(Algoritmos.bubbleSort([1, 2]), [1, 2])

    def test_selectionSort(self):
        self.assertEqual(Algoritmos.selectionSort([1]), [1])
        self.assertEqual(Algoritmos.selectionSort([2, 1]), [1, 2])
        self.assertEqual(Algoritmos.selectionSort([1, 2]), [1, 2])

    def test_mergeSort(self):
        self.assertEqual(Algoritmos.merge([1], [2]), [1, 2])
        self.assertEqual(Algoritmos.merge([2], [1]), [1, 2])

    def test_bogoSort(self):
        self.assertEqual(Algoritmos.inorder([2, 1]), False)
        self.assertEqual(Algoritmos.inorder([1, 2]), True)

    def test_pesoArbol(self):
        self.assertEqual(Algoritmos.pesoArbol(3), 3)
        self.assertEqual(Algoritmos.pesoArbol([3]), 3)
        self.assertEqual(Algoritmos.pesoArbol([3, 2, 4, 7, 15]), 31)

    def test_cantidadElementos(self):
        self.assertEqual(Algoritmos.cantidadElementos(3), 1)
        self.assertEqual(Algoritmos.cantidadElementos([3]), 1)
        self.assertEqual(Algoritmos.cantidadElementos([3, 2, 4, 7, 15]), 5)

    def test_alturaArbol(self):
        self.assertEqual(Algoritmos.alturaArbol(3), 0)
        self.assertEqual(Algoritmos.alturaArbol([3]), 0)
        self.assertEqual(Algoritmos.alturaArbol([3, 2, 4, 7, 15]), 1)
        self.assertEqual(Algoritmos.alturaArbol([4, 2]), 1)
        self.assertEqual(Algoritmos.alturaArbol([[2, 3, 4], 3]), 1)
        self.assertEqual(Algoritmos.alturaArbol([[2, 4], 3, [4, 6]]), 2)

    def test_mergeSort2(self):
        self.assertEqual(Algoritmos.merge2([1], [2]), [1, 2])
        self.assertEqual(Algoritmos.merge2([2], [1]), [1, 2])

    def test_bucket_sort(self):
        self.assertEqual(Algoritmos.bucket_sort([3, 2, 3]), [2, 2, 3])
        self.assertEqual(Algoritmos.bucket_sort([1]), [1])


if __name__ == "__main__":
    unittest.main()
