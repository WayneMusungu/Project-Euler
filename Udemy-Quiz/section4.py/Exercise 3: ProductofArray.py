#Product of Array
#Write a function called productOfArray which takes in an array of numbers and returns the product of them all.

#Examples
# 1. productOfArray([1,2,3]) #6
# 2. productOfArray([1,2,3,10]) #60

# Using Recursive Approach

def productOfArray(arr):
	if len(arr) == 0:
		return 1
	else:
		return arr[0] * productOfArray(arr[1::])

arr=[1,2,3]
print(productOfArray(arr))

# Using traversal
def productOfArray(arr):
	total = 1
	for i in range(0, len(arr)):
		total *= arr[i]
	return total
arr=[1,2,3,10]
print(productOfArray(arr))
