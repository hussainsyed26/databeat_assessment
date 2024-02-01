#!/usr/bin/env python
# coding: utf-8

# In[6]:


from typing import List, Set, Tuple

def find_pairs_recursive(nums: List[int], k: int) -> List[Tuple[int, int]]:
    """
    Find pairs in the list whose sum is equal to a given value (k).

    Args:
    - nums (List[int]): The input list of integers.
    - k (int): The target sum value.

    Returns:
    - List[Tuple[int, int]]: A list containing unique pairs whose sum is equal to k.
    
    Raises:
        TypeError: If the input list contains any element that is not an integer.
    """
    # Check if all elements in the input list are integers
    if any(not isinstance(num, int) for num in nums):
        raise TypeError("Input list should contain only integers.")

    # Use a set to store unique pairs and processed indices to avoid duplicates
    result = set() 
    processed_indices = set()

    def recursive_helper(sublist: List[int], current_index: int):
        """
        A recursive helper function to find pairs in a sublist whose sum is equal to a given value (k).

        Args:
        - sublist (List[int]): The sublist of integers being processed.
        - current_index (int): The current index in the sublist.

        Modifies:
        - Updates the 'result' set with unique pairs found in the sublist.
        - Updates the 'processed_indices' set to avoid duplicate processing.

        Returns:
        - None

        This function is designed to be called recursively to explore all possible pairs
        in the sublist and identify those whose sum is equal to the target value (k).
        """
        # Check if the current index is within the bounds of the sublist
        if current_index < len(sublist):
            current_num = sublist[current_index]
            complement = k - current_num    #complement:The value needed to complete the pair and achieve the target sum k.

            # Check if the complement exists in the remaining part of the sublist
            # and if the current index has not been processed before
            if complement in sublist[current_index + 1:] and current_index not in processed_indices:
                complement_index = sublist.index(complement, current_index + 1)
                # Add the pair to the result set and mark indices as processed
                result.add((current_num, complement))
                processed_indices.add(current_index)
                processed_indices.add(complement_index)

            # Recursively call the function for the next index
            recursive_helper(sublist, current_index + 1)

    # Start the recursive helper function with the entire input list and index 0
    recursive_helper(nums, 0)

    # Convert the result set to a list and return
    return list(result)


# In[7]:


# Test Case 1: Random positive integers
nums = [10, 7, 3, 5, 2, 8, 9, 1]
k = 10
result = find_pairs_recursive(nums, k)
print(result)


# Test Case 2: Random negative integers
nums = [-5, -3, -8, -2, -1, -4, -7]
k = -12
result = find_pairs_recursive(nums, k)
print(result)


# Test Case 3: Mix of positive and negative integers
nums = [5, -3, 2, 8, -1, 7, -4]
k = 4
result = find_pairs_recursive(nums, k)
print(result)


# Test Case 4: Large list with duplicate pairs
nums = [1, 2, 3, 4] * 10
k = 6
result = find_pairs_recursive(nums, k)
print(result)


# Test Case 5: Large list with no pairs
nums = [1, 2, 3, 4] * 10
k = 20
result = find_pairs_recursive(nums, k)
print(result)


# Test Case 6: Edge case - empty list
nums = []
k = 5
result = find_pairs_recursive(nums, k)
print(result)


# Test Case 7: All elements are the same
nums = [7] * 10
k = 14
result = find_pairs_recursive(nums, k)
print(result)


# Test Case 8: Large list with multiple valid pairs
nums = list(range(1, 1001))
k = 100
result100 = find_pairs_recursive(nums, k)
print(result100)


# Test Case 9: Large list with no valid pairs
nums = list(range(1, 1001))
k = 2000
result = find_pairs_recursive(nums, k)
print(result)


# Test Case 10: Random list with a mix of even and odd numbers
nums = [11, 22, 33, 44, 55, 66, 77, 88, 99]
k = 100
result = find_pairs_recursive(nums, k)
print(result)


# Test Case 11: Random list with float numbers
nums = [1.5, 2.5, 3.5, 4.5, 5.5]
k = 7
result = find_pairs_recursive(nums, k)
print(result)

