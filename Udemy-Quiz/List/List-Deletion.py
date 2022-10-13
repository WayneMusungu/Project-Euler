#List Methods for deletion

#Space Complexity for list deletion is O(1)

#1. pop()
#2. delete()
#3. remove()

#1. pop()

#Time Complexity => O(1) for deleting the last element / O(n)

myList = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
#myList.pop()
#If empty it will delete the last index
myList.pop(1)
print(myList)

#2. delete()

#Time Complexity => O(n)

myList = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
del myList[2]
print(myList)

#3. delete() => Very useful when you know the element itself, no need to provide the index

#Time Complexity O(n)

myList = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
myList.remove('e')
print(myList)


