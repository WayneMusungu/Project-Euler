#It is similar to the way one sort playing cards. Values from the unsorted part are picked and placed at the correct position in the sorted part.

#The Complexity of Insertion Sort Algorithm
#Suppose, an array is in ascending order, and you want to sort it in decreasing order. In this case, worst case complexity occurs
#Each element has to be compared with each of other elements so, go every nth element, (n-1) number of comparisons are made. O(n2)

# Divide the given array into two parts
# Take the first element from unsorted array and find its correct position in the sorted array
# Repeat until unsorted array is empty

def insertionSort(customList):
	for i in range(1, len(customList)):
		key = customList[i]
		j = i-1
		while j>= 0 and key < customList[j]:
			customList[j+1] = customList[j]
			j -=1
		customList[j+1] = key
	print(customList)

cList = [2,1,7,6,5,3,4,9,8]
insertionSort(cList)


# When to use Insertion Sort
 # When we have insufficient memory
 # Easy to implement
 # When we have continous inflow of numbers and we want to keep them sorted

# When to avoid Insertion Sort
 # When time is a concern
