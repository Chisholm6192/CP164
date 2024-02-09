"""
-------------------------------------------------------
Assignment 10 Task 4
-------------------------------------------------------
Author:  Ryan Chisholm
ID:      169027577
Email:   chis7577@mylaurier.ca
__updated__ = "2023-04-09"
-------------------------------------------------------
"""
# Imports
from Deque_linked import Deque
from Sorts_Deque_linked import Sorts

# Constants


a = Deque()
a.insert_rear(23)
a.insert_rear(15)

#a = [15, 23, 45, 12, 78, 61, 7, 18, 24]
Sorts.gnome_sort(a)
for i in a:
    print(i)