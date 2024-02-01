#!/usr/bin/env python
# coding: utf-8

# In[12]:


from filter_functions import filter_by_age
from person import Person
from lambda_functions import uppercase_names
import decorators

# Task h
def main():
    #Task i: Input dictionary
    data = {"Alice": 25, "Bob": 30, "Charlie": 18, "David": 20, "Eve": 19}

    # Task ii
    filtered_dict = filter_by_age(data, 18)
    print(f"Original dictionary: {data}")
    print(f"Filtered dictionary: {filtered_dict}")

    # Task iii
    person_objects = [Person(name, age) for name, age in data.items()]
    print(f"Original list: {person_objects}")

    # Task iv
    uppercase_names_list = uppercase_names(person_objects)
    print(f"Uppercase names: {uppercase_names_list}")

    # Task v (optional, if you want to see the log file content)
    with open('log.txt', 'r') as log_file:
        log_content = log_file.read()
        print(f"Log file content:\n{log_content}")

if __name__ == "__main__":
    main()

