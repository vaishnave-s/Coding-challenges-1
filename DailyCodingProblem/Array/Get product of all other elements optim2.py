"""Looking up an element up by value 
typically requires an entire traversal of the array, unless it is sorted in some way. 
Deleting an element from an array means that all subsequent elements have to be 
shifted left by one, leading to an 0( n) time operation."""

"""Given an array of integers, return a new array such that each element at index i of 
the new array is the product of all the numbers in the original array except the one 
at i. 
For example, if our input was [ 1, 2, 3, 4, 5], the expected output would be [ 120, 
60, 40, 30, 24]. If our input was [3, 2, 1],the expected output would be [2, 
3, 6]."""
from functools import reduce

def productPuzzle(nums): 
	# Use reduce() to apply a lambda function over numbers
	product = reduce(lambda item1,item2:item1*item2, nums)
	# Print the result
	return [int(product/value) for value in nums]


a =  [ 1, 2, 3, 4, 5]
print("The product array is: ",a)
print("The product array is: ",productPuzzle(a))


