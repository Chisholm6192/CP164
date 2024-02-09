"""
-------------------------------------------------------
Assignment 9 Task 4
-------------------------------------------------------
Author:  Ryan Chisholm
ID:      169027577
Email:   chis7577@mylaurier.ca
__updated__ = "2023-04-02"
-------------------------------------------------------
"""
# Imports
from BST_linked import BST

# Constants

bst = BST()
bst.insert(5)
bst.insert(3)
bst.insert(7)
bst.insert(4)
bst.insert(2)
bst.insert(6)
bst.insert(8)
"""
           5
    3             7
2      4       6     8
    
"""

zero, one, two = bst.node_counts()

print(zero, one, two)

contains = 10 in bst
print(contains)

print()

value, parent = bst.parent_r(9)
print(value, parent)