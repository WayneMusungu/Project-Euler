#1. Craete a Head and Tail and initialize it with null
#2. Initialize the node with reference and values
#3. Create a brand new Linked List ans assign a value and reference to linked list nodes

# Time Complexity O(1)


class Node:
	def __init__(self, value=None):
		self.value = value
		self.next = None


class SLinkedList:
	def __init__(self):
		self.head = None
		self.tail = None

singlyLinkedList = SLinkedList()
node1 = Node(1)
node2 = Node(2)

singlyLinkedList.head = node1
singlyLinkedList.head.next = node2
singlyLinkedList.tail = node2
