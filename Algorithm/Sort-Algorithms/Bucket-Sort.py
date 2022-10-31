# Bucket Sort
# Is a sorting algorithm that divides an array's element into sveral buckets. THe buckets are then sorted one at a time, either using a different sorting algorithm or by recursively applying the bucket sorting algorithm

# The bucket sort method is as follows"
# 1. Create buckets and distribute elements of an array into buckets
# 2. Sort buckets individually
# 3. Merge buckets after sorting


# Time Complexity O(N^2)


# Space Complexity: O(N) => we are creating array which takes space memory

# When to use Bucket Sort:
 # When input uniformly distributed over range

# When to avoid Bucket Sort
 # When space is a concern

# Pseudocode
#lst = [5,3,4,7,2,8,6,9,1]

#1. Find the squareroot of the no of elements and round it off
# Number of buckets = round(Sqrt(number of elements))

#round(Sqrt(9))=3

#2. Find which number goes to which bucket
# Appropriate bucket = ceil(Value*number of buckets/maxValue)

# Example of 5
# ceil(5*3/9) = ceil(1.6) = 2

# Therefore number 5 will go to bucket 2

import math


def insertionSort(customList):
    for i in range(1, len(customList)):
        key = customList[i]
        j = i-1
        while j>=0 and key < customList[j]:
            customList[j+1] = customList[j]
            j -= 1
        customList[j+1] = key
    return customList


def bucketSort(customList):
    numberofBuckets = round(math.sqrt(len(customList)))
    maxValue = max(customList)
    # Create a temporary array for our buckets
    arr = []

    for i in range(numberofBuckets):
    #Create 2d arrays inside our array
        arr.append([])
    for j in customList:
        index_b = math.ceil(j*numberofBuckets/maxValue)
        arr[index_b-1].append(j)
    
    for i in range(numberofBuckets):
        arr[i] = insertionSort(arr[i])
    
    k = 0
    for i in range(numberofBuckets):
        for j in range(len(arr[i])):
            customList[k] = arr[i][j]
            k += 1
    return customList

cList = [2,1,7,6,5,3,4,9,8]
print(bucketSort(cList))
