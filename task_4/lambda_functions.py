#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Task f
uppercase_name = lambda person: person.name.upper()

# Task g
def uppercase_names(person_list):
    """
    Convert names in a list of Person objects to uppercase.

    Args:
        person_list (list): List of Person objects.

    Returns:
        list: List of uppercase names.
    """
    return list(map(uppercase_name, person_list))

