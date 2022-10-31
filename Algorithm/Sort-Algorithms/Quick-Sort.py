# Quick Sort

# This is a divide and conquer algorithm
# Find pivot number and make sure smaller numbers located at the left of pivot and bigger numbers are located at the right of the pivot
# Unlike merge sort extra space is not required

def partition(customList, low, high):
    i = low - 1
    pivot = customList[high]
    for j in range(low,high):
        if customList[j] <= pivot:
            i += 1
            customList[i], customList[j] = customList[j], customList[i]
    customList[i+1], customList[high] = customList[high], customList[i+1]
    return (i+1)

def quickSort(customList, low, high):
    if low < high:
        pi = partition(customList, low, high)
        quickSort(customList, low, pi-1)
        quickSort(customList, pi+1, high)

cList=[2,1,7,6,5,3,4,9,8]
quickSort(cList, 0, 8)
print(cList)

# Time Complexity O(NLogN)
# Space Complexity O(N)


# When to use Quick sort
 # When aveerage expected time is O(NLogN)

# When to avoid Quick Sort
 # When space is a concern
 # When you need a stable sort
