#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        formatted_row = map('{:d}'.format, row)
        print(*formatted_row, sep=' ')
