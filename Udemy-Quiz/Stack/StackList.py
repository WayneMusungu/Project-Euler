# Create a stack usig Python List without size limit

class Stack:
	def __init__(self):
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

	# push()method
	def push(self, value):
		self.list.append(value)
		return "The element has been successfully inserted"

	# pop() method
	def pop(self):
		if self.isEmpty():
			return "There is not any element in the stack"
		else:
			return self.list.pop()


	# peek () method
	def peek(self):
		if self.isEmpty():
			return "THere is not any element in the stack"
		else:
			return self.list[len(self.list)-1]


	# delete
	def delete(self):
		self.list = None
customStack = Stack()
#print(customStack.isEmpty())
customStack.push(1)
customStack.push(2)
customStack.push(3)
#print(customStack)
#print(customStack.pop())
print(customStack.peek())
print(customStack)
