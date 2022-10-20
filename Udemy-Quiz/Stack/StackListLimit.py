# Create a stack usig Python List with Limit size

class Stack:
	def __init__(self, maxSize):
		self.maxSize = maxSize
		self.list = []
	
	def __str__(self):
		values = reversed(self.list)
		values = [str(x) for x in self.list]
		return '\n'.join(values)

	# isEmpty()Method
	def isEmpty(self):
		if self.list == []:
			return True
		else:
			return False

	# isFull()Method
	def isFull(self):
		if len(self.list) == self.maxSize:
			return True
		else:
			return False

	# push()Method
	def push(self, value):
		if self.isFull():
			return "The stack is full"
		else:
			self.list.append(value)
			return "The element has been successfully inserted"

	# peek()Method => returs the last element from the stack
	def peek(self):
		if self.isEmpty():
			return "THere is not any element in the stack"
		else:
			return self.list[len(self.list)-1]


	# delete
	def delete(self):
		self.list = None

customStack = Stack(4)
print(customStack.isEmpty())
print(customStack.isFull())
customStack.push(1)
customStack.push(2)
customStack.push(3)
print(customStack)

