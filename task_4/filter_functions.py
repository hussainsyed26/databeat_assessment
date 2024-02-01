#!/usr/bin/env python
# coding: utf-8

# In[7]:


# Task a:
def filter_by_age(data, age):
    """
    Filter a dictionary based on age.

    Args:
        data (dict): A dictionary containing names as keys and ages as values.
        age (int): Minimum age to filter the dictionary.

    Returns:
        dict: Filtered dictionary with names and ages meeting the age criteria.
    """
    return {name: person_age for name, person_age in data.items() if person_age >= age}

from decorators import log_decorator

# Task e: Applying decorator to filter_by_age function
@log_decorator
def filter_by_age(data, age):
    return {name: person_age for name, person_age in data.items() if person_age >= age}

