#!/usr/bin/python3


a = 10
b = 5

from calculator_1 import add, sub, mul, div

result_add = add(a, b)
result_sub = sub(a, b)
result_mul = mul(a, b)
result_div = div(a, b)

print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))
print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))
print("{:d} / {:d} = {:d}".format(a, b, div(a, b)))
