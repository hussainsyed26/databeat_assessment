#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Task b, c
class Person:
    def __init__(self, name, age):
        """
        Initialize a Person object.

        Args:
            name (str): Name of the person.
            age (int): Age of the person.
        """
        self.name = name
        self.age = age

    def is_adult(self):
        """
        Check if the person is an adult (age 18 or above).

        Returns:
            bool: True if the person is an adult, False otherwise.
        """
        return self.age >= 18

