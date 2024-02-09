"""
-------------------------------------------------------
Assignment 9 Functions
-------------------------------------------------------
Author:  Ryan Chisholm
ID:      169027577
Email:   chis7577@mylaurier.ca
__updated__ = "2023-04-01"
-------------------------------------------------------
"""
# Imports
from Word import Word

# Constants


def insert_words(fv, hash_set):
    """
    -------------------------------------------------------
    Retrieves every Word in file_variable and inserts into
    a Hash_Set. Each Word object in hash_set contains the number
    of comparisons required to insert that Word object from
    file_variable into hash_set.
    Use: insert_words(file_variable, hash_set)
    -------------------------------------------------------
    Parameters:
        fv - the already open file containing data to evaluate (file)
        hash_set - the Hash_Set to insert the words into (Hash_Set)
    Returns:
        None
    -------------------------------------------------------
    """    
    fv = list(fv)
    fv = ''.join(fv)
    fv = list(fv) #get a list of letters from file
    i = 0 
    
    temp_str = '' #temp string for words
    
    while i < len(fv):
        if temp_str != '' and fv[i].isalpha() == False: #each time non alpha char is found
            #and temp string has letters in it, create new word object with temp string, insert to hash set
            w = Word(temp_str.lower())
            hash_set.insert(w)
            
            temp_str = '' #reset temp string
            #end of word, reset to find new word
            
        else:
            if fv[i].isalpha() == True: #current char is alphabetic, add to new word
                temp_str += str(fv[i])
        
        i += 1
            
    return


    
def comparison_total(hash_set):
    """
    -------------------------------------------------------
    Sums the comparison values of all Word objects in hash_set.
    Use: total, max_word = comparison_total(hash_set)
    -------------------------------------------------------
    Parameters:
        hash_set - a hash set of Word objects (Hash_Set)
    Returns:
        total - the total of all comparison fields in the Hash_Set
            Word objects (int)
        max_word - the word having the most comparisons (Word)
    -------------------------------------------------------
    """
    max_word = None
    total = 0
    
    for i in hash_set:
        if max_word is None: #starting max word value
            max_word = i
                
        if i.comparisons > max_word.comparisons: #update max word
            max_word = i
                
        total += i.comparisons #add to total comparisons
        
    return total, max_word
    
    
    
    
    
    
    


