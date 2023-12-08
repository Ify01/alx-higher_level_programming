#!/usr/bin/python3

def uniq_add(my_list=[]):
    val = 0
    for element in set(my_list):
        val += element
    return val
