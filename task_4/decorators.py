#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Task d
def log_decorator(func):
    """
    Decorator function to log function calls.

    Args:
        func (function): The function to be decorated.

    Returns:
        function: Decorated function.
    """
    def wrapper(*args, **kwargs):
        with open('log.txt', 'a') as log_file:
            log_file.write(f"{func.__name__} - Arguments: {args}, {kwargs}\n")
        return func(*args, **kwargs)
    return wrapper

