#This is an algorithm that compares twp adjacent elements until they are in intended order
lst = [2,10,13,28,29,5,4,3,1]
def bubble_sort(lst):
	for i in range(0, len(lst)):
		for j in range (0, len(lst)):
			if lst[i] < lst[j]:
				lst[i], lst[j] = lst[j], lst[i]
	return lst
print(bubble_sort(lst))


