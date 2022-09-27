#Linear Search Algorithm 
# This is a method of finding elements from one end and check every element of the list until the desired element is found. This is the simplest searching algorithm,

#Linear Search Simple Approach
# 1. Start from the leftmost element of an array[] and one by one compare x with each element of the array[]
# 2. If x matches with the element, return the index
# 3. If x doesn't match with any of the index, return -1

array = [1,10,15,7,8,9,6,3]
x = 10

def linearSearch(array,x):
	for i in range(0,len(array)):
		if array[i] == x:
			return i
	return -1
print(linearSearch(array,x))

#1. Data Structure
#Linear Search is flexible with all the data structures like an array, list, linked list
#2. Prerequisites
#Linear Search can be performed on all types of data, data can be random or sorted
#3. Use case
#Linear Search is generally preferred for smaller and random datasets
#4. Effectiveness
#Linear Search is less efficient in the case of larger datasets
#5. Time Complexity
#In Linear Search, the best-case complexity is 0(1)-Constant Time, where the element is found at the first index. Worst-case is 0(n)-Linear Time, the time complexity increases linearly with the size input. This occurs when the element is foound at the last index or the element is not present in the array
