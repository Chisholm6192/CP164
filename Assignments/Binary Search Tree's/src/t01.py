"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Ryan Chisholm
ID:      169027577
Email:   chis7577@mylaurier.ca
__updated__ = "2023-03-21"
-------------------------------------------------------
"""
# Imports
from BST_linked import BST

# Constants


bst = BST()
bst.insert(3)
bst.insert(1)
bst.insert(5)
bst.insert(0)
bst.insert(2)
bst.insert(4)
bst.insert(6)
'''bst.insert(11)
bst.insert(22)
bst.insert(33)
bst.insert(44)'''
print('bst')
for i in bst:
    print(i)
    
"""
        3
    1        5
 0    2    4    6
        
"""
    
print()

target = BST()
target.insert(5)
target.insert(1)
target.insert(6)
target.insert(4)
target.insert(2)
print('target')
for i in target:
    print(i)
    
print()

print('Equals')
equals = bst == target 
print(equals)

print()

print('Is Balanced')
balanced = bst.is_balanced()
print(balanced)

print()

print('Is Vaild')
valid = bst.is_valid()
print(valid)

print()

print('Min')
minimum = bst.min()
print(minimum)

print()

print('Leaf Count')
leafcount = bst.leaf_count()
print(leafcount)

print()

print('One Child Count')
one_count = bst.one_child_count()
print(one_count)

print()

print('Two Child Count')
two_count = bst.two_child_count()
print(two_count)

print()

print('Inorder')
inorder = bst.inorder()
for i in inorder:
    print(i)
    
print()

print('Preorder')
preorder = bst.preorder()
for i in preorder:
    print(i)
    
print()

print('Postorder')
postorder = bst.postorder()
for i in postorder:
    print(i)
    
print()

print('Levelorder')
levelorder = bst.levelorder()
for i in levelorder:
    print(i)
    
print()

print('Remove')
bst.remove(90)
for i in bst:
    print(i)

