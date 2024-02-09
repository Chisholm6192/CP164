"""
-------------------------------------------------------
Assignment 1
-------------------------------------------------------
Author:  Ryan Chisholm
ID:      169027577
Email:   chis7577@mylaurier.ca
__updated__ = "2023-01-18"
-------------------------------------------------------
"""
# Imports

# Constants



def clean_list(values):
    """
    -------------------------------------------------------
    Removes all duplicate values from a list: values contains
    only one copy of each of its integers. The order of values
    must be preserved.
    Use: clean_list(values)
    -------------------------------------------------------
    Parameters:
        values - a list of integers (list of int)
    Returns:
        None
    -------------------------------------------------------
    """
    
    singles = [] #values that aren't duplicates
    
    for i in values:
        if i not in singles: #if it isn't already in the list, add it
            singles.append(i)
            
    values.clear() #clear the original list
    
    for i in singles:
        values.append(i) #add the non-duplicates to the original list
    
    return



def file_analyze(fv):
    """
    -------------------------------------------------------
    Analyzes the characters in a file.
    The contents of the file must be unchanged.
    Use: u, l, d, w, r = file_analyze(fv)
    -------------------------------------------------------
    Parameters:
        fv - an already open file reference (file variable)
    Returns:
        u - the number of uppercase letters in the file (int)
        l - the number of lowercase letters in the file (int)
        d - the number of digits in the file (int)
        w - the number of whitespace characters in the file (int)
        r - the number of remaining characters in the file (int)
    -------------------------------------------------------
    """
    #number of uppercase, lowercase, digits, whitespaces, and characters remaining
    u = 0
    l = 0
    d = 0
    w = 0
    r = 0
    
    fv = " ".join(fv) #combine to string
    
    fv = list(fv) #break into list
    
        
    for i in range(len(fv)):
        if fv[i].isupper() == True:
            u += 1 #add to uppercase count
            
        elif fv[i].islower() == True:
            l += 1 #add to lowercase count
            
        elif fv[i].isdigit() == True:
            d += 1 #add to digits count
            
        elif fv[i] == ' ' or fv[i] == '\n' or fv[i] == '\t':
            w += 1 #add to whitespace count
        
        else:
            r += 1
                
        
    return u, l, d, w, r



def find_subs(string, sub):
    """
    -------------------------------------------------------
    Finds the indices of the locations of sub within string,
        left to right.
    Use: locations = find_subs(string, sub)
    -------------------------------------------------------
    Parameters:
        string - a string to evaluate (str)
        sub - a substring to locate in string (str)
    Returns:
        locations - an ordered list of the indices of the locations
            of sub within string (list of int)
    -------------------------------------------------------
    """
    #put string and substring into list for indexing
    string = list(string) 
    sub = list(sub)
    
    locations = []
    sub_string = True
    
    
    for i in range(len(string)):
        if i <= (len(string) - len(sub)): 
        #to avoid out of range error, make sure that the current index can add the length of substring without going out of range
            for j in range(len(sub)):
                if string[i+j] != sub[j]: #check characters after current index to check if they match the substring
                    sub_string = False
                    
                
            if sub_string == True:
                locations.append(i)
                
            sub_string = True
                    
    return locations



def is_leap_year(year):
    """
    -------------------------------------------------------
    Leap year determination.
    Use: leap_year = is_leap_year(year)
    -------------------------------------------------------
    Parameters:
        year - year to determine if it is a leap year (int > 0)
    Returns:
        leap_year - True if year is a leap year, False otherwise (boolean)
    -------------------------------------------------------
    """
    leap_year = False
    
    if year % 4 == 0: #divisible by 4
        if year % 100 == 0: #divisible by 100 and by 4
            if year % 400 == 0: #divisible by 400, 100 and by 4
                leap_year = True
                
            #if divisible by 100 but not by 400, leap year stays false
                
        else:
            leap_year = True
        #divisible by 4 but not by 100
                
    return leap_year



def is_valid(name):
    """
    -------------------------------------------------------
    Determines if name is a valid Python variable name.
    Variables names must start with a letter or an underscore.
    The rest of the variable name may consist of letters, numbers
    and underscores.
    Use: valid = is_valid(name)
    -------------------------------------------------------
    Parameters:
        name - a string to test as a Python variable name (str)
    Returns:
        valid - True if name is a valid Python variable name,
            False otherwise (boolean)
    -------------------------------------------------------
    """  
    valid = True
    
    if name[0].isalpha() == False and name[0] != '_': #name doesn't start with a letter or underscore
        valid = False 
        
    else:
        for i in range(len(name)):
            if name[i].isalpha() == False and name[i].isdigit() == False and name[i] != '_':
            #character isn't a letter, number or underscore
                valid = False
    
    return valid



def matrix_transpose(a):
    """
    -------------------------------------------------------
    Transpose the contents of matrix a.
    Use: b = matrix_transpose(a):
    -------------------------------------------------------
    Parameters:
        a - a 2D list (list of lists of ?)
    Returns:
        b - the transposed matrix (list of lists of ?)
    -------------------------------------------------------
    """
    b = []
    
    for i in range(len(a[0])): #the number of lists to be created is equal to the dimension on each entry
        t = [] #create new temp list
        
        for j in range(len(a)): #access entries from full length of list
            t.append(a[j][i])
            
        b.append(t) #add temp list to main list
            
        
    return b



def matrixes_multiply(a, b):
    """
    -------------------------------------------------------
    Multiplies the contents of matrixes a and b.
    If a is mxn in size, and b is nxp in size, then c is mxp.
    a and b must be unchanged.
    Use: c = matrixes_multiply(a, b)
    -------------------------------------------------------
    Parameters:
        a - a 2D list (2D list of int/float)
        b - a 2D list (2D list of int/float)
    Returns:
        c - the matrix multiple of a and b (2D list of int/float)
    -------------------------------------------------------
    """
    c = []
    
    for k in range(len(a)): 
    #number of rows in c = number of rows in a, rows only need to be added len(a) times
        t = [] #create new temp list
    
        for i in range(len(b[0])):
        #number of columns in c = number of columns in b, columns only need to be added len(b[0]) times
            dot = 0 #dot product
            
            for j in range(len(b)):
                dot += a[k][j] * b[j][i]
                #third loop lets b access the next set of indexes, while a does not change
                
            t.append(dot) #add dot product to temp list
            
        c.append(t) #add temp list to matrix
                
    return c




def pig_latin(word):
    """
    -------------------------------------------------------
    Converts a word to Pig Latin. The conversion is:
    - if a word begins with a vowel, add "way" to the end of the word.
    - if the word begins with consonants, move the leading consonants to
    the end of the word and add "ay" to the end of that.
    "y" is treated as a consonant if it is the first character in the word,
    and as a vowel for anywhere else in the word.
    Preserve the case of the word - i.e. if the first character of word
    is upper-case, then the new first character should also be upper case.
    Use: pl = pig_latin(word)
    -------------------------------------------------------
    Parameters:
        word - a string to convert to Pig Latin (str)
    Returns:
        pl - the Pig Latin version of word (str)
    ------------------------------------------------------
    """
    pl = ''
    
    if word[0].upper() in 'AEIOU': #first letter is vowel
        pl = word + 'way'
        
    elif word[0].upper() not in 'AEIOU': #first letter is not vowel
        while word[0].upper() not in 'AEIOUY': #run until reaching a vowel
            
            if word[0].isupper() == True: #first letter is uppercase
                word = word[0] + word[1].upper() + word[2:]
                
            elif word[0].islower() == True: #first letter is lowercase
                word = word[0] + word[1].lower() + word[2:]
                
            word = word[1:] + word[0].lower() #move letter to end of word
   
        pl = word + 'ay'    
                  
    return pl       
    
    
def shift(string, n):
    """
    -------------------------------------------------------
    Encipher a string using a shift cipher.
    Only letters are enciphered, and the returned string is
    in upper case.
    Use: estring = shift(string, n):
    -------------------------------------------------------
    Parameters:
        string - string to encipher (str)
        n - the number of letters to shift (int)
    Returns:
        estring - the enciphered string (str)
    -------------------------------------------------------
    """
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' #alphabet letters in order
    estring = ''
    
    for i in range(len(string)):
        j = 0
        
        if string[i].isalpha() == True:
        
            while string[i].upper() != alphabet[j]: #run until matching letter is found
                j += 1
            
            if j + n < len(alphabet): #shift does not go out of range
                estring += alphabet[j+n] #add shifted letter to string
                
                
            elif j + n >= len(alphabet): #shift does go out of range
                overflow = (j + n) - len(alphabet) #find the overflow, which is the index
                estring += alphabet[overflow]
                            
        else:
            estring += string[i]
                    
    return estring
    
    
    
    
    
    
    
    
    
    
    
