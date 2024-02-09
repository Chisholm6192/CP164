"""
-------------------------------------------------------
Assignment 7 Task 1
-------------------------------------------------------
Author:  Ryan Chisholm
ID:      169027577
Email:   chis7577@mylaurier.ca
__updated__ = "2023-03-16"
-------------------------------------------------------
"""
# Imports
from List_linked import List

# Constants

source = List()
source.append(3)
source.append(24)
source.append(8)

target = List()
target.append(8)
target.append(24)
target.append(3)
target.append(3)
target.append(8)

print('Append')
for i in source:
    print(i)
    
print()

print('Equals')
equals = source == target
print(equals)

print()

print('Get Item')
print(source[1])

print()

print('Clean')
#target.clean()

for i in target:
    print(i)
    
'''New target value: [3, 24, 8]'''
    
print()

source1 = List()
source2 = List()

source1.append(11)
source1.append(33)
#source1.append(23)

source2.append(22)
source2.append(44)
#source2.append(0)
#source2.append(14)
print('Combine')
list_obj = List()

list_obj.combine(source1, source2)

for i in list_obj:
    print(i)
    
print()

print('Intersection')

intersect = List()
intersect.intersection(source, target)
for i in intersect:
    print(i)
    
    
print()

print('Prepend')
source1.append(4)
source1.append(45)
source1.prepend(1)
for i in source1:
    print(i)
    
print()

print('Remove Front')
source1.remove_front()
for i in source1:
    print(i)
    
print()

print('Remove Many')
target.remove_many(3)
for i in target:
    print(i)
    
print()

split_list = List()
split_list.append(10)
split_list.append(2)
split_list.append(3)
split_list.append(1)
split_list.append(4)

print('Split')
target1, target2 = split_list.split()
print('target1')
for i in target1:
    print(i)
    
print()
print('target2')
for i in target2:
    print(i)
    
print()

'''print('Split Alt')
target1, target2 = split_list.split_alt()
print('target1')
for i in target1:
    print(i)
    
print()
print('target2')
for i in target2:
    print(i)

print()'''


print('Union')
list_union = List()
list_union.union(target1, target2)
for i in list_union:
    print(i)
    
print()

print('Equals')
equal = list_union == split_list
print(equal)


