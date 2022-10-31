# Binary Search

#- Faster than Linear Search
#- Half of the remaining elements can be eliminated at a time, instead of eliminating them one by one
#- Binary Search only works for sorted arrays

# Binary Search Pseudocode 
#1. Create function with two parameters which are a sorted array and a value
#2. Create two pointers:
	# a left pointer at the start of the array
	# a right pointer at the end of the array
#3. Based on left and right pointers calculate middle pointer
#4. While middle is not equal to the value and start <=end loop:
	# if the middle is greater than the value move the right pointer down
	# if the middle is less than the value move the left pointer up
#5. If the value is never found return -1


import math
def binarySearch(array, value):
    start = 0
    end = len(array)-1
    middle = math.floor((start+end)/2)
    while not(array[middle]==value) and start<=end:
        if value < array[middle]:
            end = middle - 1
        else:
            start = middle + 1 
        middle = math.floor((start+end)/2)
        # print(start, middle, end)
    if array[middle] == value:
        return middle
    else:
        return -1
        



custArray = [8, 9, 12, 15, 17, 19, 20, 21, 28]
print(binarySearch(custArray, 15))
