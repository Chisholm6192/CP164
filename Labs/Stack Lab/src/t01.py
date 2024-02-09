"""
-------------------------------------------------------
Lab 2 Task 1
-------------------------------------------------------
Author:  Ryan Chisholm
ID:      169027577
Email:   chis7577@mylaurier.ca
__updated__ = "2023-01-23"
-------------------------------------------------------
"""
# Imports
from Stack_array import Stack

# Constants


s = Stack()
print(s.is_empty())
s.push(6)
#print(s.pop())

value = s.peek()
print(value)

for v in s:
    print(v)