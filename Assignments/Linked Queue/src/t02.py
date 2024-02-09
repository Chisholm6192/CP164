"""
-------------------------------------------------------
Assignment 6 Task 2
-------------------------------------------------------
Author:  Ryan Chisholm
ID:      169027577
Email:   chis7577@mylaurier.ca
__updated__ = "2023-03-12"
-------------------------------------------------------
"""
# Imports
from Priority_Queue_linked import Priority_Queue

# Constants



pq = Priority_Queue()
pq.insert(5)
pq.insert(6)
pq.insert(4)

for i in pq:
    print(i)
    
    
print()

#print('Split Alt')
source = Priority_Queue()
source.insert(1)
source.insert(24)
source.insert(13)

#target1, target2 = source.split_alt()

for i in source:
    print(i)

'''print('Target 1')
for i in target1:
    print(i)
    
print()

print('Target 2')
for i in target2:
    print(i)'''
    
print()
source._append_queue(pq)

for i in source:
    print(i)
    
    
    
    
    
    
    
    