import unittest
import numpy as np
from mnk import mnk



class test_mnk(unittest.TestCase):

    def test_simple(self):
        x = np.array([1, 2, 3, 4, 5])
        y = np.array([3, 5, 7, 9, 11]) 
        
        result = mnk(x, y)
        k, b = result
        
        self.assertAlmostEqual(k, 2.0, places=5, msg="коэффициент k должен быть 2")
        self.assertAlmostEqual(b, 1.0, places=5, msg="коэффициент b должен быть 1")

    def test_simple2(self):
        x = np.array([1, 2, 3, 10])
        y = np.array([5, 5, 5, 5])
        
        k, b = mnk(x, y)
        
        self.assertAlmostEqual(k, 0.0, places=5)
        self.assertAlmostEqual(b, 5.0, places=5)

    def test_negative_simple(self):
        x = np.array([1, 2, 3])
        y = np.array([9, 8, 7])
        
        k, b = mnk(x, y)
        
        self.assertAlmostEqual(k, -1.0, places=5)
        self.assertAlmostEqual(b, 10.0, places=5)

    def test_invalid_input(self):
        x = np.array([1, 2, 3])
        y = np.array([1, 2])
        
        result = mnk(x, y)
        
        self.assertAlmostEqual(result, 0, places=5, msg="должна возвращать 0 при разной длине массивов")

    def test_how_good_is_my_damn_function(self): #Сравнение с np.polyfit
        x = np.array([1.5, 2.3, 3.8, 4.1, 5.5])
        y = np.array([2.1, 3.5, 5.2, 5.9, 7.1])
        
        my_k, my_b = mnk(x, y)
        
        np_k, np_b = np.polyfit(x, y, 1)
        
        self.assertAlmostEqual(my_k, np_k, places=5)
        self.assertAlmostEqual(my_b, np_b, places=5)
