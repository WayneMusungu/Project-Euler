#1. Creating a Tuple

# Time Complexity 0(1) => We are defining all elements upfront
# Space Complexity 0(n) => It depends on the number of elements of the tuple

newTuple1 = tuple('abcde')

print(newTuple1)


#2. Accessing Tuple elements

# Time Complexity O(1)
# Space Complexity 0(1)

newTuple1 = tuple('abcde')
print(newTuple1[1])


#2. Traversing through Tuple

# Time Complexity 0(n)
# Space Complexity O(1)

newTuple1 = tuple('abcde')

for i in range(len(newTuple1)):
	print(newTuple1[i])

# or

# for i in newTuple:
	print(i)

#3. Search for an element in Tuple

#(a) Use the in operator

# Time Complexity O(n)
newTuple1 = tuple('abcde')
print('a' in newTuple1)


#(b) Use the index method
newTuple1 = tuple('abcde')
print(newTuple1.index('e'))


#Time complexity O(n)
#Space Complexity O(1)


newTuple1 = tuple('abcde')

def searchTuple(p_tuple, element):
	for i in range(0, len(p_tuple)):
		if p_tuple[i] == element:
			return f"The element {element} is found at {i} index"
	return "The element is not found"
print(searchTuple(newTuple1, 'b'))



# Tuple Operations / Functions

myTuple = (1,4,3,2,5)
myTuple1 = (1,2,6,9,8,7)

print(myTuple + myTuple1)


# Star operator for repetition

myTuple = (1,4,3,2,5)
myTuple1 = (1,2,6,9,8,7)

print(myTuple * 4)
