"""
-------------------------------------------------------
Lab 2 Task 4 
-------------------------------------------------------
Author:  Ryan Chisholm
ID:      169027577
Email:   chis7577@mylaurier.ca
__updated__ = "2023-01-25"
-------------------------------------------------------
"""
# Imports
from utilities import stack_test
from Stack_array import Stack

# Constants

s = Stack()

stack_test(s) #test empty stack

s.push(1) #add to stack
s.push(2)

stack_test(s) #test non-empty stack