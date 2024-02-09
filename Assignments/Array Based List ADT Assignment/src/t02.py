"""
-------------------------------------------------------
Assignment 5 Task 2
-------------------------------------------------------
Author:  Ryan Chisholm
ID:      169027577
Email:   chis7577@mylaurier.ca
__updated__ = "2023-02-18"
-------------------------------------------------------
"""
# Imports
from Sorted_List_array import Sorted_List

# Constants

source = Sorted_List()
'''source.insert(2)
source.insert(10)
source.insert(5)
source.insert(1)
source.insert(3)
source.insert(4)
source.insert(12)
source.insert(14)'''
'''[10, 5, 1, 10] -> [1, 5, 10, 10]'''
print('Source: ')
for i in source:
    print(i)
        
print()

source1 = Sorted_List()
'''source1.insert(1)
source1.insert(2)
source1.insert(3)
source1.insert(4)
source1.insert(9)'''
'''[1, 6, 2, 3] -> [1, 2, 3, 6]'''
print('source1: ')
for i in source1:
    print(i)
    
print()

source2 = Sorted_List()
'''source2.insert(5)
source2.insert(6)
source2.insert(6)
source2.insert(8)
source2.insert(13)'''

'''[5, 7, 3, 2] -> [2, 3, 5, 7]'''
print('source2: ')
for i in source2:
    print(i)
    
print()
    
key = -7
print(f'Test if {key} in source: ')
b = key in source 
print(b)

print()

'''find = source[0]
item = 'source[2]'
print(f'{item} = {find} ')

print()'''

print('Test for equal: source1 and source2')
equals = source1 == source2
print(equals)

print()

'''print('Test Clean: ')
source.clean()

print('Cleaned source')
for i in source:
    print(i)
    
print()'''

num = -7
print(f'Test Count {num} in source: ')
count = source.count(num)
print(count)

print()

val = -7
print(f'Test find {val} in source: ')
value = source.find(val)
print(value)

print()

print('Interesection: source1 and source2')
target = Sorted_List()
target.intersection(source1, source2)
for i in target:
    print(i)
    
print()

'''print('Find Max in source')
maximum = source.max()
print(maximum)

print()

print('Find Min in source')
minimum = source.min()
print(minimum)

print()

print('Find peak in source')
peak = source.peek()
print(peak)

print()'''

'''number = 1
print(f'Remove {number} from source')
removed = source.remove(number)
print(f'Removed {removed}')
print('Source after remove')
for i in source:
    print(i)
    
print()'''

'''print('Remove Front')
front_removed = source.remove_front()
print(f'Removed {front_removed}')
print()
for i in source:
    print(i)
    
print()'''

'''remove_number = 2
print(f'Remove Many {remove_number}')
many_removed = source.remove_many(remove_number)
for i in source:
    print(i)
    
print()'''
    
    
'''target1, target2 = source.split()
print('split in source')
print('target1: ')
for i in target1:
    print(i)
    
print()

print('target2: ')
for i in target2:
    print(i)  '''
    
print()

'''print('split alt source')
list1, list2 = source.split_alt()
print()
print('List 1: ')
for i in list1:
    print(i)
    
print()
print('List 2: ')  
for i in list2:
    print(i)

print()'''

print('Union source1, source2')
sort = Sorted_List()
sort.union(source1, source2)
for i in sort:
    print(i)

