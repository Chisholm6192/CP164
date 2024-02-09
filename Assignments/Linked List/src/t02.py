"""
-------------------------------------------------------
Assignment 8 Task 2
-------------------------------------------------------
Author:  Ryan Chisholm
ID:      169027577
Email:   chis7577@mylaurier.ca
__updated__ = "2023-03-18"
-------------------------------------------------------
"""
# Imports
from Sorted_List_linked import Sorted_List

# Constants

print('Source')
source = Sorted_List()
source.insert(11)
source.insert(22)
source.insert(33)
source.insert(44)
source.insert(55)
for i in source:
    print(i)
    
print()

target1 = Sorted_List()
target1.insert(12)
target1.insert(9)
target1.insert(12)
target1.insert(0)
'''[0, 9, 12, 12]'''

target2 = Sorted_List()
target2.insert(1)
target2.insert(9)
target2.insert(12)
target2.insert(9)
'''[1, 9, 9, 12]'''
     
print()

print('Remove')
value = source.remove(55)
for i in source:
    print(i)

print()

print('Remove Front')
num = source.remove_front()
for i in source:
    print(i)

print()

print(f'source[0] = {source[0]}')
print(f'33 in source: {33 in source}')
print(f'Max: {source.max()}')
print(f'Min: {source.min()}')
print(f'Count of 22: {source.count(22)}')

print()

print('Intersection')
intersect = Sorted_List()
intersect.intersection(target1, target2)
for i in intersect:
    print(i)
    
print()

print('Union')
linked_union = Sorted_List()

test = Sorted_List()
test.insert(0)
test.insert(12)
test.insert(5)
test.insert(0)

test_1 = Sorted_List()
test_1.insert(0)
test_1.insert(22)
test_1.insert(33)
test_1.insert(44)
test_1.insert(55)

linked_union.union(test, test_1)
for i in linked_union:
    print(i)
    
print()

print('Combine')
linked_combine = Sorted_List()
linked_combine.combine(test, test_1)
for i in linked_combine:
    print(i)






