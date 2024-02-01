#!/usr/bin/env python
# coding: utf-8

# In[4]:


from task_2 import find_pairs_recursive

max_memory = 100000  # Specify the maximum memory limit in bytes;

# Test Case 1: Random positive integers
nums = [10, 7, 3, 5, 2, 8, 9, 1]
k = 10
result = find_pairs_recursive(nums, k, max_memory)
print(result)


# Test Case 2: Random negative integers
nums = [-5, -3, -8, -2, -1, -4, -7]
k = -12
result = find_pairs_recursive(nums, k, max_memory)
print(result)


# Test Case 3: Mix of positive and negative integers
nums = [5, -3, 2, 8, -1, 7, -4]
k = 4
result = find_pairs_recursive(nums, k, max_memory)
print(result)


# Test Case 4: Large list with duplicate pairs
nums = [1, 2, 3, 4] * 10
k = 6
result = find_pairs_recursive(nums, k, max_memory)
print(result)


# Test Case 5: Large list with no pairs
nums = [1, 2, 3, 4] * 10
k = 20
result = find_pairs_recursive(nums, k, max_memory)
print(result)


# Test Case 6: Edge case - empty list
nums = []
k = 5
result = find_pairs_recursive(nums, k, max_memory)
print(result)


# Test Case 7: All elements are the same
nums = [7] * 10
k = 14
result = find_pairs_recursive(nums, k, max_memory)
print(result)


# Test Case 8: Large list with multiple valid pairs
nums = list(range(1, 1001))
k = 100
result100 = find_pairs_recursive(nums, k, max_memory)
print(result100)


# Test Case 9: Large list with no valid pairs
nums = list(range(1, 1001))
k = 2000
result = find_pairs_recursive(nums, k, max_memory)
print(result)


# Test Case 10: Random list with a mix of even and odd numbers
nums = [11, 22, 33, 44, 55, 66, 77, 88, 99]
k = 100
result = find_pairs_recursive(nums, k, max_memory)
print(result)


# Test Case 11: Random list with float numbers
nums = [1.5, 2.5, 3.5, 4.5, 5.5]
k = 7
result = find_pairs_recursive(nums, k, max_memory)
print(result)

