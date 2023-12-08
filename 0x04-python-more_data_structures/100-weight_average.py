#!/usr/bin/python3

def weight_average(my_list):
    if not my_list or not isinstance(my_list, list):
        return 0

    num = sum(value * weight for value, weight in my_list)
    denom = sum(weight for _, weight in my_list)

    return num / denom if denom != 0 else 0
