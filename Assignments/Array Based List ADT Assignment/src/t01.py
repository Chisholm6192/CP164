"""
-------------------------------------------------------
Assignment 5 Task 1
-------------------------------------------------------
Author:  Ryan Chisholm
ID:      169027577
Email:   chis7577@mylaurier.ca
__updated__ = "2023-02-15"
-------------------------------------------------------
"""
# Imports
from List_array import List
from Movie_utilities import read_movies

# Constants


fh = open('movies.txt', 'r', encoding = 'utf-8')
fh_list = list(fh)
movies = read_movies(fh_list)


target = List()
target.append(1)
target.append(1)
target.append(2)
#target.append(10)
#target.append(2)
#target.append(movies[0])
'''[10,2]'''
print('target')
for i in target:
    print(i)
    
print()

llist = List()
llist.append(1)
llist.append(2)
'''llist.append(3)
llist.append(2)
llist.append(4)
llist.append(4)
llist.append(2)
llist.append(10)
llist.append(3)'''
'''[1,2,3,2,4,4,2,10,3]'''
print('llist')
for i in llist:
    print(i)
    
print()
print(llist[0])

print()

target1 = List()
target1.append(1)
target1.append(2)
'''target1.append(34)
target1.append(7)'''
'''[1,2,34,7]'''
print('Target 1: ')
for i in target1:
    print(i)
    
print()

target2 = List()
target2.append(3)
target2.append(6)
target2.append(2)
'''[3,6,2]'''
print('Target 2: ')
for i in target2:
    print(i)
    
print()

source1 = List()
source1.append(1)
source1.append(2)
source1.append(8)
source1.append(7)
'''[1,2,34,7]'''
print('source1: ')
for i in source1:
    print(i)
    
print()

source2 = List()
source2.append(3)
source2.append(6)
source2.append(8)
source2.append(2)
source2.append(8)
'''[3,6,34,2]'''
print('source2: ')
for i in source2:
    print(i)
    
print()

source = List()
source.append(10)
source.append(12)
source.append(3)
source.append(7)
source.append(3)
#source.append(6)
#source.append(1)
#source.append(4)
#source.append(7)
#source.append(23)
print('source: ')
'''[10,12,3,7,3,6]'''
for i in source:
    print(i)
    
print()

split = List()
split.append(23)
split.append(2)
split.append(34)
split.append(14)
'''[23,2,7,34,14]'''
print('split: ')
for i in split:
    print(i)
    
print()

list1 = List()
list1.append(1)


'''[44,33,55,22,55]'''
print('list1: ')
for i in list1:
    print(i)
    
print()

list2 = List()
list2.append(2)
list2.append(1)

'''list2.append(2)
list2.append(5)
list2.append(1)
list2.append(2)'''
'''[22,55,11,12]'''
print('list2: ')
for i in list2:
    print(i)
    
print()
print()


equals = llist == target
print(f'Test for Equal (llist and target): {equals}')

print()
print()

print(f'List Clean (llist)')
llist.clean()
for i in llist:
    print(i)
    
print()
print()

values = List()
values.combine(target1, target2)
print('List Combine (target1, target2)')
for i in values:
    print(i)

print()
print()
    
target = List()
target.intersection(source1, source2)
print('List Intersection (source1, source2)')
for i in target:
    print(i)
    
print()
print()

source.prepend(2)
print('Prepend')
for i in source:
    print(i)
    
print()
print()

print(f'Remove Front: {source.remove_front()}')
for i in source:
    print(i)

print()
print()

print('Remove Many')
source.remove_many(5)
for i in source:
    print(i)
        
print()
print()

print('Source Split')
l1, l2 = source.split()
print('List 1: ')
for i in l1:
    print(i)
    
print()

print('List 2: ')
for i in l2:
    print(i)
      
print()
print()

li1, li2 = split.split_alt()
print('List 1: ')
for i in li1:
    print(i)
    
print()

print('List 2: ')
for i in li2:
    print(i)

print()
print()

print('Union')
united = List()
united.union(list1, list2)

for i in united:
    print(i)

fh.close()
print()





