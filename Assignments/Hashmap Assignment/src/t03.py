"""
-------------------------------------------------------
Assignment 9 Task 3
-------------------------------------------------------
Author:  Ryan Chisholm
ID:      169027577
Email:   chis7577@mylaurier.ca
__updated__ = "2023-04-02"
-------------------------------------------------------
"""
# Imports
from functions import insert_words, comparison_total
from Hash_Set_BST import Hash_Set

# Constants


h = Hash_Set(20)

fv = open('words.txt', 'r', encoding='utf-8')

insert_words(fv, h)

fv.close()

print('Using Linked BST Hash Set')
print()
print('Insert Words')
for i in h:
    print(i)
    
print()

print('Comparison Total')
total, max_word = comparison_total(h)
print(f'Total Comparisons: {total:,}')
print(f'Word with most comparisons {max_word}')

