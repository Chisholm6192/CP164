"""
-------------------------------------------------------
Assignment 8 Task 2
-------------------------------------------------------
Author:  Ryan Chisholm
ID:      169027577
Email:   chis7577@mylaurier.ca
__updated__ = "2023-03-24"
-------------------------------------------------------
"""
# Imports
from BST_linked import BST
from functions import do_comparisons, comparison_total
from Letter import Letter

# Constants


DATA1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
DATA2 = "MFTCJPWADHKNRUYBEIGLOQSVXZ"
DATA3 = "ETAOINSHRDLUCMPFYWGBVKJXZQ"

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
    
print(f'Comparing by order: {DATA1}')

total = comparison_total(bst1)
print(f'Total Comparisons: {total}')

print()

print(f'Comparing by order: {DATA2}')

total = comparison_total(bst2)
print(f'Total Comparisons: {total}')

print() 

print(f'Comparing by order: {DATA3}')

total = comparison_total(bst3)
print(f'Total Comparisons: {total}')
    



