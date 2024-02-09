"""
-------------------------------------------------------
Lab 2 Task 2
-------------------------------------------------------
Author:  Ryan Chisholm
ID:      169027577
Email:   chis7577@mylaurier.ca
__updated__ = "2023-01-25"
-------------------------------------------------------
"""
# Imports
from utilities import array_to_stack
from Stack_array import Stack

# Constants


s = Stack()

source = [11, 22, 33, 44, 55]
print(source)

array_to_stack(s, source)

print(list(s))