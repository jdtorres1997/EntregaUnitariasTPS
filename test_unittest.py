
import unittest

import Algoritmos


class Tests(unittest.TestCase):
    def test_quicksort(self):
        self.assertEqual(Algoritmos.quicksort([1, 2, 3], 0, 2), [1, 2, 3])

    def test_quicksort2(self):
        self.assertEqual(Algoritmos.quicksort(
            [1, 2, 3, 4, 5], 0, 4), [1, 2, 3, 4, 5])

    def test_bublesort(self):
        self.assertEqual(Algoritmos.bubbleSort([1]), [1])

    def test_bublesort2(self):
        self.assertEqual(Algoritmos.bubbleSort([2, 1]), [1, 2])

    def test_bublesort3(self):
        self.assertEqual(Algoritmos.bubbleSort([1, 2]), [1, 2])

    def test_selectionSort(self):
        self.assertEqual(Algoritmos.selectionSort([1]), [1])

    def test_selectionSort2(self):
        self.assertEqual(Algoritmos.selectionSort([2, 1]), [1, 2])
    def test_selectionSort3(self):
        self.assertEqual(Algoritmos.selectionSort([1, 2]), [1, 2])

    def test_mergeSort(self):
        self.assertEqual(Algoritmos.merge([1], [2]), [1, 2])
    def test_mergeSort2(self):
        self.assertEqual(Algoritmos.merge([2], [1]), [1, 2])

    def test_bogoSort(self):
        self.assertEqual(Algoritmos.inorder([2, 1]), False)
    def test_bogoSort2(self):
        self.assertEqual(Algoritmos.inorder([1, 2]), True)

    def test_pesoArbol(self):
        self.assertEqual(Algoritmos.pesoArbol(3), 3)
    def test_pesoArbol2(self):
        self.assertEqual(Algoritmos.pesoArbol([3]), 3)
    def test_pesoArbol3(self):
        self.assertEqual(Algoritmos.pesoArbol([3, 2, 4, 7, 15]), 31)

    def test_cantidadElementos(self):
        self.assertEqual(Algoritmos.cantidadElementos(3), 1)
    def test_cantidadElementos2(self):
        self.assertEqual(Algoritmos.cantidadElementos([3]), 1)
    def test_cantidadElementos3(self):
        self.assertEqual(Algoritmos.cantidadElementos([3, 2, 4, 7, 15]), 5)

    def test_alturaArbol(self):
        self.assertEqual(Algoritmos.alturaArbol(3), 0)
    def test_alturaArbol2(self):
        self.assertEqual(Algoritmos.alturaArbol([3]), 0)
    def test_alturaArbol3(self):
        self.assertEqual(Algoritmos.alturaArbol([3, 2, 4, 7, 15]), 1)
    def test_alturaArbol4(self):
        self.assertEqual(Algoritmos.alturaArbol([4, 2]), 1)
    def test_alturaArbol5(self):
        self.assertEqual(Algoritmos.alturaArbol([[2, 3, 4], 3]), 1)
    def test_alturaArbol6(self):
        self.assertEqual(Algoritmos.alturaArbol([[2, 4], 3, [4, 6]]), 2)

    def test_mergeSortt2(self):
        self.assertEqual(Algoritmos.merge2([1], [2]), [1, 2])
    def test_mergeSortt3(self):
        self.assertEqual(Algoritmos.merge2([2], [1]), [1, 2])

    def test_bucket_sort(self):
        self.assertEqual(Algoritmos.bucket_sort([3, 2, 3]), [2, 2, 3])
    def test_bucket_sort2(self):
        self.assertEqual(Algoritmos.bucket_sort([1]), [1])


if __name__ == "__main__":
    unittest.main()
