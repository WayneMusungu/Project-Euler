# Graph Traversal
 # It is the process of visiting all vertices in a given graph

# Breadth First Search
 # This is an algorithm used for traversing graphs or trees

# It is a traversing technique, where you 
# select a random initial node (source or root node)
# and start traversing then graph layer-wise in such
# a way that all the nodes and their respective children nodes are visited


# Time Complexity: O(V+E)
# Space Complexity: O(V+E)



class Graph:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict
    
    def addEdge(self, vertex, edge):
        self.gdict[vertex].append(edge)
    
    def bfs(self, vertex):
        visited = [vertex]
        queue = [vertex]
        while queue:
            deVertex = queue.pop(0)
            print(deVertex)
            for adjacentVertex in self.gdict[deVertex]:
                if adjacentVertex not in visited:
                    visited.append(adjacentVertex)
                    queue.append(adjacentVertex)					

customDict = { "a" : ["b", "c"],
	       "b" : ["a", "d", "e"],
	       "c" : ["a", "e"],
   	       "d" : ["b", "e", "f"],
               "e" : ["d", "f"],
               "f" : ["d", "e"]
              }

graph = Graph(customDict)
graph.bfs("a")
