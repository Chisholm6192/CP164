"""
-------------------------------------------------------
Lab 2 Task 5
-------------------------------------------------------
Author:  Ryan Chisholm
ID:      169027577
Email:   chis7577@mylaurier.ca
__updated__ = "2023-01-26"
-------------------------------------------------------
"""
# Imports
from utilities import stack_test
from Stack_array import Stack
from Movie_utilities import read_movies

# Constants

fh = open('movies.txt', 'r', encoding = 'utf-8')

fh_list = list(fh)

movies = read_movies(fh_list)

s = Stack()

for i in movies:
    s.push(i)

stack_test(s)

fh.close()