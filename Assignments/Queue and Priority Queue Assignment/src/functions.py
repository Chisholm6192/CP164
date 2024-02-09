"""
-------------------------------------------------------
Assignment 4 Functions
-------------------------------------------------------
Author:  Ryan Chisholm
ID:      169027577
Email:   chis7577@mylaurier.ca
__updated__ = "2023-02-11"
-------------------------------------------------------
"""
# Imports
from Queue_array import Queue
from Priority_Queue_array import Priority_Queue

# Constants



def queue_combine(source1, source2):
    """
    -------------------------------------------------------
    Combines two source queues into the current target queue.
    When finished, the contents of source1 and source2 are interlaced
    into target and source1 and source2 are empty.
    Order of source values is preserved.
    (iterative algorithm)
    Use: target = queue_combine(source1, source2)
    -------------------------------------------------------
    Parameters:
        source1 - a queue (Queue)
        source2 - a queue (Queue)
    Returns:
        target - a queue (Queue)
    -------------------------------------------------------
    """
    target = Queue()    
    n = True
    
    while source1.is_empty() == False and source2.is_empty() == False: #add removed values alternatively until one of the source queues are empty
        if n == True:
            target.insert(source1.remove())
        else:    
            target.insert(source2.remove())
            
        n = not n
        
        
    #depending on if either of the lists are larger than the other, continue to add values after while loop ends
    if source1.is_empty() == False: 
        while source1.is_empty() == False:
            target.insert(source1.remove())
        
    elif source2.is_empty() == False:
        while source2.is_empty() == False:
            target.insert(source2.remove())
        
    return target    



def pq_split_key(source, key):
    """
    -------------------------------------------------------
    Splits a priority queue into two depending on an external
    priority key. The source priority queue is empty when the method
    ends.
    Use: target1, target2 = pq_split_key(source, key)
    -------------------------------------------------------
    Parameters:
        source - a priority queue (Priority_Queue)
        key - a data object (?)
    Returns:
        target1 - a priority queue that contains all values
            with priority higher than key (Priority_Queue)
        target2 - priority queue that contains all values with
            priority lower than or equal to key (Priority_Queue)
    -------------------------------------------------------
    """
    target1 = Priority_Queue()
    target2 = Priority_Queue()
    
    while source.is_empty() == False: #run until source is empty
        value = source.remove() #set remove to variable, to allow for comparison without removing extra data
        
        if value < key: #if removed value is higher priority
            target1.insert(value)
            
        else: #if removed value is equal or lesser priority
            target2.insert(value)
            
    return target1, target2
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    