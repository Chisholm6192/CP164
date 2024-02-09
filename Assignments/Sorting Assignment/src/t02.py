"""
-------------------------------------------------------
Assignment 10 Task 2
-------------------------------------------------------
Author:  Ryan Chisholm
ID:      169027577
Email:   chis7577@mylaurier.ca
__updated__ = "2023-04-07"
-------------------------------------------------------
"""
# Imports
from Sorts_List_linked import Sorts
from List_linked import List

# Constants

a = List()
a.append(23)
a.append(15)

a.append(45)
#a = [15, 23, 45, 12, 78, 61, 7, 18, 24]
Sorts.radix_sort(a)
for i in a:
    print(i)
