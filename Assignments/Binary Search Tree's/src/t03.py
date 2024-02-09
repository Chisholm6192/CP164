"""
-------------------------------------------------------
Assignment 8 Task 3
-------------------------------------------------------
Author:  Ryan Chisholm
ID:      169027577
Email:   chis7577@mylaurier.ca
__updated__ = "2023-03-26"
-------------------------------------------------------
"""
# Imports
from functions import do_comparisons, letter_table
from Letter import Letter
from BST_linked import BST

# Constants


DATA1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
DATA2 = "MFTCJPWADHKNRUYBEIGLOQSVXZ"
DATA3 = "ETAOINSHRDLUCMPFYWGBVKJXZQ"

#print('DATA1 BST')
bst1 = BST()

#add data
for i in DATA1:
    letter = Letter(i)
    bst1.insert(letter)

bst2 = BST()

for i in DATA2:
    letter = Letter(i)
    bst2.insert(letter)

bst3 = BST() 

for i in DATA3:
    letter = Letter(i) 
    bst3.insert(letter)
    
fh = open('words.txt', 'r', encoding ='utf-8')
do_comparisons(fh, bst1)
fh.close()

fh = open('words.txt', 'r', encoding ='utf-8')
do_comparisons(fh, bst2)
fh.close()

fh = open('words.txt', 'r', encoding ='utf-8')
do_comparisons(fh, bst3)
fh.close()    
print('BST1')
letter_table(bst1)

print()

print('BST2')
letter_table(bst2)

print()

print('BST3')
letter_table(bst3)


