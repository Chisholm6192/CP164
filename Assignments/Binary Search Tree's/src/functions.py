"""
-------------------------------------------------------
Assignment 8 Functions
-------------------------------------------------------
Author:  Ryan Chisholm
ID:      169027577
Email:   chis7577@mylaurier.ca
__updated__ = "2023-03-24"
-------------------------------------------------------
"""
# Imports
from Letter import Letter
# Constants



def do_comparisons(file_variable, bst):
    """
    -------------------------------------------------------
    Retrieves every letter in file_variable from bst. Generates
    comparisons in bst objects. Each Letter object in bst contains
    the number of comparisons found by searching for that Letter
    object in file_variable.
    Use: do_comparisons(file_variable, bst)
    -------------------------------------------------------
    Parameters:
        file_variable - the already open file containing data to evaluate (file)
        bst - the binary search tree containing 26 Letter objects
            to retrieve data from (BST)
    Returns:
        None
    -------------------------------------------------------
    """
    fv = list(file_variable)
    fv = ''.join(fv)
    fv = list(fv) #get a list of letters from file

    # Zeroes out all comparison values in tree nodes
    for node in bst:
        node.comparisons = 0
        
    i = 0
    while i < len(fv): #go through file contents
        
        if fv[i].isalpha() == True: #only check letters
            letter = Letter(fv[i].upper()) #create new letter object for comparison, must be converted to uppercase
            bst.retrieve(letter) #retrieve
                    
        i += 1
        
    return


def comparison_total(bst):
    """
    -------------------------------------------------------
    Sums the comparison values of all Letter objects in bst.
    Use: total = comparison_total(bst)
    -------------------------------------------------------
    Parameters:
        bst - a binary search tree of Letter objects (BST)
    Returns:
        total - the total of all comparison fields in the bst
            Letter objects (int)
    -------------------------------------------------------
    """
    total = 0
    bst.inorder()
    
    for letters in bst:
        total += letters.comparisons
        
    return total
    
    
    
def letter_table(bst):
    """
    -------------------------------------------------------
    Prints a table of letter counts for each Letter object in bst.
    Use: letter_table(bst)
    -------------------------------------------------------
    Parameters:
        bst - a binary search tree of Letter objects (BST)
    Returns:
        None
    -------------------------------------------------------
    """
    print('Letter Count/Percent Table')
    
    total = 0
    bst.inorder()
    
    for letters in bst:
        total += letters.count
    
    print()
    print(f'Total Count: {total:,}')
    print()
    print('Letter  Count       %')
    print('---------------------')
    
    for letters in bst:
        print(f'    {letters.letter}    {letters.count:,}    {(letters.count / total) * 100:>6.2f}%')
    
    
    
    
    
