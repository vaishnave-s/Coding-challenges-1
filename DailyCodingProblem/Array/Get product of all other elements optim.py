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

# Python program for product array puzzle
# with O(n) time and O(1) space.

import math

# epsilon value to maintain precision
EPS = 1e-9

def productPuzzle(a):
	n=len(a)
	# to hold sum of all values
	sum = 0
	for i in range(n):
		sum += math.log10(a[i])
	
	# output product for each index
	# antilog to find original product value
	return[int((EPS + pow(10.00, sum - math.log10(a[i])))) for i in range(n)]
	

# Driver code
a =  [ 1, 2, 3, 4, 5]
print("The product array is: ",a)
print("The product array is: ",productPuzzle(a))


"""Complexity Analysis: 

Time Complexity: O(n). 
Only two traversals of the array is required.
Space Complexity: O(1). 
No extra space is required."""

