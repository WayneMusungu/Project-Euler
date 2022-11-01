# We use dictionary implementation to create Graphs in Python
#{ A : [B, C],
#  B : [A, D, E],
#  C : [A, E],
#  D : [B, E, F],
#  E : [C, D, F],
#  F : [D, E]
#}

class Graph:
	def __init__(self, gdict=None):
		if gdict is None:
			gdict = {}
		self.gdict = gdict

	def addEdge(self, vertex, edge):
		self.gdict[vertex].append(edge)

customDict = { "a" : ["b", "c"],
	       "b" : ["a", "d", "e"],
	       "c" : ["a", "e"],
   	       "d" : ["b", "e", "f"],
               "e" : ["d", "f"],
               "f" : ["d", "e"]
              }

graph = Graph(customDict)
graph.addEdge("e", "c")
print(graph.gdict)
#print(graph.gdict["e"])
