"""
-------------------------------------------------------
Assignment 6 Task 3
-------------------------------------------------------
Author:  Ryan Chisholm
ID:      169027577
Email:   chis7577@mylaurier.ca
__updated__ = "2023-03-13"
-------------------------------------------------------
"""
# Imports
from Deque_linked import Deque

# Constants


dq = Deque()
dq.insert_front(100)
dq.insert_front(10)
dq.insert_front(34)

for i in dq:
    print(i)
    
print()

dq.remove_front()

for i in dq:
    print(i)
    
print()

print('Equals')
source1 = Deque()
source1.insert_front(10)
source1.insert_front(4)

source2 = Deque()
source2.insert_front(10)
source2.insert_front(5)

equals = source1 == source2

print(equals)