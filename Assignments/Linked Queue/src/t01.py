"""
-------------------------------------------------------
Assignment 6 Task 1
-------------------------------------------------------
Author:  Ryan Chisholm
ID:      169027577
Email:   chis7577@mylaurier.ca
__updated__ = "2023-03-11"
-------------------------------------------------------
"""
# Imports
from Queue_linked import Queue

# Constants



Q = Queue()
Q.insert(10)
Q.insert(11)

print('Queue')
for i in Q:
    print(i)
    
print()
    
print('Peek')
print(Q.peek())

    
Q.remove()
print('Removed')
for i in Q:
    print(i)

print()
    
source = Queue()
source.insert(11)
source.insert(22)
source.insert(33)
source.insert(44)

target = Queue()
print('Queue Append')
target._append_queue(source)
for i in target:
    print(i)

print('Source after append')
for i in source:
    print(i)
print(f'Count: {source._count}')

print()

source1 = Queue()
'''source1.insert(11)
source1.insert(22)
source1.insert(33)
source1.insert(44)'''

print('Source1')
for i in source1:
    print(i)

print()

print('Source2')    
source2 = Queue()
source2.insert(11)
source2.insert(22)
source2.insert(33)
source2.insert(44)
for i in source2:
    print(i)
    
print()
'''print('Move front to rear')
source1._move_front_to_rear(source2)

for i in source1:
    print(i)'''
    
'''print('Combine')
q = Queue()
q.combine(source1, source2)

for i in q:
    print(i)'''
    
print('Split Alt')
split_queue = Queue()
split_queue.insert(10)
split_queue.insert(12)
split_queue.insert(45)
target1, target2 = split_queue.split_alt()

print('Target1')
for i in target1:
    print(i)
    
print()

print('Target2')
for i in target2:
    print(i)
    
print()
print('Equals')
equals = target1 == target2
print(equals)



