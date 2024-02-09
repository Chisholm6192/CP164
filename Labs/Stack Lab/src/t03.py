"""
-------------------------------------------------------
Lab 2 Task 3
-------------------------------------------------------
Author:  Ryan Chisholm
ID:      169027577
Email:   chis7577@mylaurier.ca
__updated__ = "2023-01-25"
-------------------------------------------------------
"""
# Imports
from utilities import stack_to_array
from Stack_array import Stack

# Constants


s = Stack()
s.push(55)
s.push(44)
s.push(33)
s.push(22)
s.push(11)

target = []
print(list(s))

stack_to_array(s, target)

print(target)