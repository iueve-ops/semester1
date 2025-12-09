import unittest
from quicksort import quicksort 
import random

class test_quiqsort(unittest.TestCase):

    def test_1(self):
        self.assertEqual(quicksort([]), [])

    def test_2(self):
        self.assertEqual(quicksort([5]), [5])

    def test_3(self):
        self.assertEqual(quicksort([1, 2, 3, 4]), [1, 2, 3, 4])

    def test_4(self):
        self.assertEqual(quicksort([4, 3, 2, 1]), [1, 2, 3, 4])

    def test_5(self):
        with self.assertRaises(TypeError):
            quicksort([3, "1", (2), [3], 1])
    def test_6(self):
        self.assertEqual(quicksort([0, -2, 5, -1]), [-2, -1, 0, 5])

    def test_7(self):
        arr = [random.randint(-1000, 1000) for _ in range(1000)]
        self.assertEqual(quicksort(arr), sorted(arr))
 
    def test_8(self):
        self.assertEqual(quicksort([7, 7, 7, 7]), [7, 7, 7, 7])
    
    def test_9(self):
        arr = [5, -1, 3, 0, -2, 8, 3]
        self.assertEqual(quicksort(arr), sorted(arr))
    def test_10(self):
        with self.assertRaises(TypeError):
            quicksort("not a list")

        with self.assertRaises(TypeError):
            quicksort(123)

        with self.assertRaises(TypeError):
            quicksort(None)