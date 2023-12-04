#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for table in matrix:
        print(' '.join(map('{:d}'.format, table)))
