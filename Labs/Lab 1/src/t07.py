"""
-------------------------------------------------------
Lab 1 Task 7
-------------------------------------------------------
Author:  Ryan Chisholm
ID:      169027577
Email:   chis7577@mylaurier.ca
__updated__ = "2023-01-18"
-------------------------------------------------------
"""
# Imports
from Movie_utilities import read_movies

# Constants

fv = open('movies.txt', 'r', encoding='utf-8')

fv_list = list(fv)
movies = read_movies(fv_list)
print(movies)
fv.close()
