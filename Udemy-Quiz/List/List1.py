#Ways of inserting values to a list
#1. At the begginning of a list
#2. At any given place in the list
#3. At the end of the list
#4. Inserting another list to the list

# 1. insert() => It inserts an element ain any given location to the list

#Time Complexity O(n)

myList = [1, 2, 3, 4, 5, 6, 7]
print(myList)
myList.insert(0, 9)
print(myList)

# 2. append() =>This function is efficient and only adds element at the end of the list

#Time Complexity O(1)
#Space Complexity O(1) => We just need one location for each element

myList = [1, 2, 3, 4, 5, 6, 7]
myList.append(50)
print(myList)

# 3. extend() => This function adds a list to another list

#Time Complexity O(n)

myList = [1, 2, 3, 4, 5, 6, 7]
newList = [10, 20, 30, 40, 50, 60, 70]
myList.extend(newList)
print(myList)
