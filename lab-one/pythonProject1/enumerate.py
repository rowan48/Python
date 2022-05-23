#Enumerate() method adds a counter to an iterable and returns it in a form of enumerating object.
# This enumerated object can then be used directly for loops or converted into a list of tuples using the list() method.
#example
# Python program to illustrate
# enumerate function in loops
l1 = ["rowan", "israa", "hadeer"]

# printing the tuples in object directly
for ele in enumerate(l1):
	print (ele)
#output
# (0, 'rowan')
# (1, 'israa')
# (2, 'hadeer')
# changing index and printing separately
for count, ele in enumerate(l1, 100):
	print (count, ele)
#output
# 100 rowan
# 101 israa
# 102 hadeer

# getting desired output from tuple
for count, ele in enumerate(l1):
	print(count)
	print(ele)
#output
# 0
# rowan
# 1
# israa
# 2
# hadeer


