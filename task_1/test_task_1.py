#!/usr/bin/env python
# coding: utf-8

# In[1]:


import unittest
from task_1 import find_pairs_recursive

class TestFindPairsRecursive(unittest.TestCase):
    def test_find_pairs(self):
        # Test case 1: General case
        nums_1 = [1, 2, 3, 4, 5, 6]
        k_1 = 7
        self.assertEqual(find_pairs_recursive(nums_1, k_1), [(1, 6), (2, 5), (3, 4)])

        # Test case 2: No pairs found
        nums_2 = [1, 2, 3, 4, 5]
        k_2 = 20
        self.assertEqual(find_pairs_recursive(nums_2, k_2), [])

        # Test case 3: Empty list
        nums_3 = []
        k_3 = 5
        self.assertEqual(find_pairs_recursive(nums_3, k_3), [])

        # Test case 4: List with duplicate elements
        nums_4 = [3, 3, 4, 4, 5, 5]
        k_4 = 8
        self.assertEqual(find_pairs_recursive(nums_4, k_4), [(3, 5), (4, 4)])

        # Test case 5: List with non-integer elements
        nums_5 = [1, 2, 'a', 4, 5]
        k_5 = 6
        with self.assertRaises(TypeError):
            find_pairs_recursive(nums_5, k_5)

if __name__ == '__main__':
    unittest.main()

