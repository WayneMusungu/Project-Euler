#Contains Duplicate
#Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
#Example 1:

#Input: nums = [1,2,3,1]
#Output: true

#Example 2:
#Input: nums = [1,2,3,4]
#Output: false

#Example 3:
#Input: nums = [1,1,1,3,3,4,3,2,4,2]
#Output: true


#Pseudocode 
#1. Create empty list
#2. Loop through given list
#3. In each visit check if the visited element is in our newly created list and save the visited element in the newly created list

myList = [1, 20, 30, 44, 5, 56, 57, 8, 19, 10, 31, 12, 13, 14, 35, 16, 27, 58, 19, 21]

def isUnique(list):
	a = []
	for i in list:
		if i in a:
			print(i)
#The elements here are not unique
			return False
		else:
			a.append(i)
	return True

print(isUnique(myList))
