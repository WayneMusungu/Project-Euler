#1. Creating Dictionary

#English to Spanish
#Print a single element in a dictionary

engToSp = {"one":"uno", "two":"dos", "three":"tres"}
print(engToSp)
engToSp['one']


myDict = dict()
print(myDict)


#2. Insert/Update an element in a Dictionary

#(a). Update
# Time Complexity: O(1)
# Space Complexity: O(1)

myDict = {"name":"Eddy", "age":20}
myDict["age"] = 21
print(myDict)

#(b). Insertion
# Time Complexity: O(1)
# Space complexity: amortized O(1)

myDict = {"name":"Eddy", "age":20}
myDict["address"] = "Shenyang"
print(myDict)

#3. Traversing through a Dictionary
# Time Complexity: O(n)
# Space Complexity: O(1)
myDict = {"name":"Eddy", "age":20, "address":"Shenyang"}

def traverseDict(dict):
	for key in dict:
		print(key, dict[key])
traverseDict(myDict)

#4. Search for an element in a Dictionary
# Time Complexity: O(n)
# Space Complexity: O(1)


myDict = {"name":"Eddy", "age":20, "address":"Shenyang"}

def searchDict(dict,value):
	for key in dict:
		if dict[key] == value:
			return key, value
	return "The value does not exist"
print(searchDict(myDict, 20))


#5 Delete or remove an element from a Dictionary
#(a). pop() => Removes an item with the provided key and returns the value of the deleted pair

myDict = {"name":"Eddy", "age":20, "address":"Shenyang"}
print(myDict.pop("name"))
print(myDict)

#(b). popitem() => It selects randomly a pair and deleting it
myDict = {"name":"Eddy", "age":20, "address":"Shenyang"}
print(myDict.popitem())
print(myDict)

#(c). clear() => It deletes all pairs from the dictionary
#This method does not take any parameter and it does not return any value, it returns none by default
myDict = {"name":"Eddy", "age":20, "address":"Shenyang"}
print(myDict.clear())
print(myDict)

#(d). del() => Deletes any pair in the dictionary
myDict = {"name":"Eddy", "age":20, "address":"Shenyang"}
del myDict["age"]
print(myDict)
