#SELECTION SORT
#We traverse the whole array to find the smallest element. Once we find it, we swap the smallest element with the first element of the array.Then we again look for the smallest element in the remaining array(excluding the first element) and swap it with the second element. This process goes on till the whole array gets sorted.

#The algorithm maintains two subarrays in a given array
#    • The sorted subarray
#    • The unsorted subarray

#The Complexity of Selection Sort Algorithm
#The time complexity of the selection sort is the same in all cases O(n2) because it is made up of two nested loops. At every step, you have to find the minimum element and put it in the right place. The minimum element is not known until the end of the array is not reached.

def selectionSort( itemsList ):
    n = len( itemsList )
    for i in range( n - 1 ): 
        minValueIndex = i

        for j in range( i + 1, n ):
            if itemsList[j] < itemsList[minValueIndex] :
                minValueIndex = j

        if minValueIndex != i :
            temp = itemsList[i]
            itemsList[i] = itemsList[minValueIndex]
            itemsList[minValueIndex] = temp

    return itemsList


el = [21,6,9,33,3]

print(selectionSort(el))

#Code explanation:

#Defines a function named selectionSort
#Gets the total number of elements in the list. We need this to determine the number of passes to be made when comparing values.
#Outer loop. Uses the loop to iterate through the values of the list. The number of iterations is (n – 1). The value of n is 5, so (5 – 1) gives us 4. This means the outer iterations will be performed 4 times. In each iteration, the value of the variable i is assigned to the variable minValueIndex
#Inner loop. Uses the loop to compare the leftmost value to the other values on the right-hand side. However, the value for j does not start at index 0. It starts at (i + 1). This excludes the values that have already been sorted so that we focus on items that have not yet been sorted.
#Finds the minimum value in the unsorted list and places it in its proper position
#Updates the value of minValueIndex when the swapping condition is true
#Compares the values of index numbers minValueIndex and i to see if they are not equal
#The leftmost value is stored in a temporal variable
#The lower value from the right-hand side takes the position first position
#The value that was stored in the temporal value is stored in the position that was previously held by the minimum value
#Returns the sorted list as the function result
#Creates a list el that has random numbers
#Print the sorted list after calling the selection Sort function passing in el as the parameter.


# Advantage of selection sort
 # It performs well in small lists, no additional space storage is required

# Disadvantage of selection sort
 # Its poor efficiency when dealing with huge list of items


def selectionSort(customList):
	for i in range(len(customList)):
		min_index = i
		for j in range(i+1, len(customList)):
			if customList[min_index] > customList[j]:
				min_index = j
		customList[i], customList[min_index] = customList[min_index], customList[i]
	print(customList)

cList = [2,1,7,6,5,3,4,9,8]
selectionSort(cList)
