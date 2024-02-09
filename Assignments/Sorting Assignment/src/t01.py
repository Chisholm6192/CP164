"""
-------------------------------------------------------
Assignment 10 Task 1
-------------------------------------------------------
Author:  Ryan Chisholm
ID:      169027577
Email:   chis7577@mylaurier.ca
__updated__ = "2023-04-04"
-------------------------------------------------------
"""
# Imports
from Sorts_array import Sorts
from List_array import List

# Constants

a = List()
a.append(23)

a.append(15)
a.append(45)
#a = [15, 23, 45, 12, 78, 61, 7, 18, 24]
Sorts.radix_sort(a)
for i in a:
    print(i)
