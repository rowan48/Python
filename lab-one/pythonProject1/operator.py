#!/usr/bin/python

#The operator module exports a set of efficient functions corresponding to the intrinsic operators of Python. For example, operator.add(x, y) is equivalent to the expression x+y. Many function names are those used for special methods, without the double underscores.
# For backward compatibility, many of these have a variant with the double underscores kept.
# The variants without the double underscores are preferred for clarity.
#example add,sub , mul
# Python code to demonstrate working of
# add(), sub(), mul()


# Import operator module

import operator
# mod = __import__('operator', globals=globals())
# Take two input numbers from user
x = int(input("Enter first integer number:"))
y = int(input("Enter second integer number:"))
# Adding both input numbers
addResult = operator.add(x, y)
# Print result
print("Addition of input numbers given by you is: ", addResult)
