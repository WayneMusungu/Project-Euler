# Find the missing number in an integer array of 1 to 100

mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]

def findMissing(list,n):
# Using summation of first N natural numbers
# Find the sum of the numbers in the range [1, N] using the formula N * (N+1)/2. Find the sum of all the elements in the array and subtract it from the sum of the first N natural numbers. This will give the value of the missing element.
	sum1 = 100*101/2
	sum2 = sum(list)
	print(sum1-sum2)
findMissing(mylist, 100)