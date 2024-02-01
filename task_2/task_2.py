#!/usr/bin/env python
# coding: utf-8

# In[6]:


import tracemalloc
from typing import List, Tuple

def find_pairs_recursive(nums: List[int], k: int, max_memory: int) -> List[Tuple[int, int]]:
    """
    Find pairs of integers in the given list whose sum is equal to the target value (k).
    
    Args:
        nums (List[int]): The input list of integers.
        k (int): The target sum value.
        max_memory (int): The maximum allowed memory usage in bytes.

    Returns:
        List[Tuple[int, int]]: A list of tuples representing pairs of integers that sum up to k.

    Raises:
        TypeError: If the input list contains any element that is not an integer.
        MemoryError: If the memory usage exceeds the specified limit during processing.
    """
    if any(not isinstance(num, int) for num in nums):
        raise TypeError("Input list should contain only integers.")

    result = set()
    processed_indices = set()

    # Start tracing memory
    tracemalloc.start()

    try:
        for i in range(len(nums)):
            current_num = nums[i]
            complement = k - current_num

            if complement in nums[i + 1:] and i not in processed_indices:
                complement_index = nums.index(complement, i + 1)
                result.add((current_num, complement))
                processed_indices.add(i)
                processed_indices.add(complement_index)

            # Check memory usage after processing each element
            _, current_memory = tracemalloc.get_traced_memory()
            if current_memory > max_memory:
                raise MemoryError("Memory limit exceeded during processing.")

    finally:
        # Stop tracing memory
        tracemalloc.stop()

    return list(result)

