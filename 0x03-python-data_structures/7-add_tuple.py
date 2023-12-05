#!/usr/bin/python3


from itertools import zip_longest

def add_tuple(tuple_a=(0, 0), tuple_b=(0, 0)):
    added_tuple = tuple(x + y for x, y in zip_longest(tuple_a, tuple_b, fillvalue=0))
    return added_tuple
