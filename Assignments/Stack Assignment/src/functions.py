"""
-------------------------------------------------------
Assignment 3
-------------------------------------------------------
Author:  Ryan Chisholm
ID:      169027577
Email:   chis7577@mylaurier.ca
__updated__ = "2023-02-03"
-------------------------------------------------------
"""
# Imports
from Stack_array import Stack
from enum import Enum

# Constants
OPERATORS = "+-*/"

# Enumerated constant
MIRRORED = Enum('MIRRORED',
                {'IS_MIRRORED': "is a mirror", 'TOO_MANY_LEFT': "too many characters in L",
                 'TOO_MANY_RIGHT': "too many characters in R", 'MISMATCHED': "L and R don't match",
                 'INVALID_CHAR': "invalid character", 'NOT_MIRRORED': "no mirror character"})




def stack_split_alt(source):
    """
    -------------------------------------------------------
    Splits the source stack into separate target stacks.
    When finished source stack is empty. Values are
    pushed alternately onto the returned target stacks.
    Use: target1, target2 = stack_split_alt(source)
    -------------------------------------------------------
    Parameters:
        source - the stack to split into two parts (Stack)
    Returns:
        target1 - contains alternating values from source (Stack)
        target2 - contains other alternating values from source (Stack)
    -------------------------------------------------------
    """
    #create stack objects to push to
    target1 = Stack()
    target2 = Stack()
    
    target = True #alternating boolean variable
    
    while source.is_empty() == False: #run until source is empty
        if target == True:
            target1.push(source.pop())
        else:
            target2.push(source.pop())
            
        target = not target #flip value of target each time
    
    return target1, target2



def is_palindrome_stack(string):
    """
    -------------------------------------------------------
    Determines if string is a palindrome. Ignores case, digits, spaces, and
    punctuation in string.
    Use: palindrome = is_palindrome_stack(string)
    -------------------------------------------------------
    Parameters:
        string - a string (str)
    Returns:
        palindrome - True if string is a palindrome, False otherwise (bool)
    -------------------------------------------------------
    """
    chars = Stack()
    palindrome = True #string is a palindrome until proven otherwise
    
    
    for i in string:
        if i.isalpha() == False:
            string = string.replace(i, '')
            #remove all non alphabetic characters in string
        
    string = string.lower() #convert to lower case to eliminate case sensitivity
    
    i = 0
    while i < len(string):
        chars.push(string[i]) #push all chars to stack
        
        i += 1
        
    j = len(string) - 1   
    while j >= 0 and chars.is_empty() == False:
        #iterate through string in reverse order to match with values popped from stack
        if chars.pop() != string[j]:
            palindrome = False
            
        j -= 1
        
            
    return palindrome



def postfix(string):
    """
    -------------------------------------------------------
    Evaluates a postfix expression.
    Use: answer = postfix(string)
    -------------------------------------------------------
    Parameters:
        string - the postfix string to evaluate (str)
    Returns:
        answer - the result of evaluating string (float)
    -------------------------------------------------------
    """
    operands = Stack() #create stack of operands
    string = string.split() #split string at each space
    
    for i in string:
        if i not in OPERATORS: #if char isn't an operator
            operands.push(float(i)) #add int of char to stack
            
        elif i in OPERATORS:
            if i == '+':
                operands.push(operands.pop() + operands.pop()) #add the values from the top 
                
            elif i == '-':
                operands.push(-operands.pop() + operands.pop()) #subtract the values from the top
                
            elif i == '*':
                operands.push(operands.pop() * operands.pop()) #multiply the values from the top
                
            elif i == '/':
                operands.push((operands.pop() ** -1) * operands.pop()) #divide the value from the top
                    
                    
    answer = operands.pop()     
                
    return answer



def stack_maze(maze):
    """
    -------------------------------------------------------
    Solves a maze using Depth-First search.
    Use: path = stack_maze(maze)
    -------------------------------------------------------
    Parameters:
        maze - dictionary of points in a maze, where each point
            represents a corridor end or a branch. Dictionary
            keys are the name of the point followed by a list of
            branches, if any. First point is named 'Start', exit
            is named 'X' (dict)
    Returns:
        path - list of points visited before the exit is reached,
            None if there is no exit (list of str)
    -------------------------------------------------------
    """
    path = [] #list of paths chosen
    maze_stack = Stack() #maze pathway stack
    value = []
    
    start = ''.join(maze['Start']) #starting point
    
    maze_stack.push(start)
    
    while 'X' not in value and maze_stack.is_empty() == False: #until exit is found in one of the pathways or it is determined that there is no exit
        key = maze_stack.pop() 
        value = maze[key]
        path.append(key) #search maze for index of top value in stack
                
        for i in range(len(value)): #run through maze pathway to check for new paths or exit
            maze_stack.push(value[i]) #add new pathways to stack
            
    if 'X' in value:
        path.append('X') #when it eventually finds the exit, add the exit path onto pathway list
    
    else:
        path = None
    
    return path



def is_mirror_stack(string, valid_chars, m):
    """
    -------------------------------------------------------
    Determines if string is a mirror of characters in valid_chars around the pivot m.
    A mirror is of the form LmR, where L is the reverse of R, and L and R
    contain only characters in valid_chars.
    Use: mirror = is_mirror_stack(string, valid_chars, m)
    -------------------------------------------------------
    Parameters:
        string - a string (str)
        valid_chars - a string of valid characters (str)
        m - the mirror pivot string (str - one character not in valid_chars)
    Returns:
        mirror - the state of the string (Enum MIRRORED)
    -------------------------------------------------------
    """
    assert m not in valid_chars, \
        f"cannot use '{m}' as the mirror character"
        
    stack_mirror = Stack() #create mirror stack object
    mirror = MIRRORED.IS_MIRRORED #string is a mirror until proven otherwise
    
    
    if m not in string: #if mirror character isn't in string
        mirror = MIRRORED.NOT_MIRRORED
    
    elif m in string: 
        for char in string:
            if char not in valid_chars and char != m: #if any char in string isn't in the list of valid chars
                mirror = MIRRORED.INVALID_CHAR
    
    
    
    if mirror == MIRRORED.IS_MIRRORED: #if the string hasn't yet been proven to not be a mirror
        i = 0  
        while i < len(string) and string[i] != m:
            stack_mirror.push(string[i]) #add chars to stack until mirror value is reached
            
            if i >= (len(string) / 2) - 1: #if the number of chars on the left > chars on right
                mirror = MIRRORED.TOO_MANY_LEFT
            
            i += 1
            
        if i < (len(string) // 2): #if the number of chars on the left < chars on right
            mirror = MIRRORED.TOO_MANY_RIGHT
        
        i += 1
                
    if mirror == MIRRORED.IS_MIRRORED: #if string hasn't yet been proven to not be a mirror
        
        while i < len(string) and stack_mirror.is_empty() == False:        
            if stack_mirror.pop() != string[i]: #if values on left and right side are not matching up
                mirror = MIRRORED.MISMATCHED
                
            i += 1
        
            
    return mirror
        
        
    
        
        
            
    
             



    
    
    
    
    
