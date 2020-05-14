"""
Start of class at 10:04 on Beej mac
"""

class Graph:
    
    def  __init__(self):
        self.vertices = {}
        
    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = set()    # Set of edges
        
    def add_edge(self, v1, v2):
        """ Add edge from v1 to v2. """
        if v1 in self.vertices and v2 i self.vertices:
            self.vertices[v1].add(v2)
            
        else:
            raise IndexError("Vertex does not exist in graph")
        
    def get_neighbors(self, vertex_id):
        pass
    
    def bft(self, starting_vertex_id):
        """ Breadth first traversal """
        
        q = Queue() # Need a queue
        q.enqueue(starting_vertex_id)   # Add a node to the queue
        
        # Keep track of visited nodes
        visited = set()
        
        # Repeat until queue is empty
        while q.size() > 0:
            
            # Dequeue first vert
            v = q.dequeue()
            
            # If it's not visited:
            if v not in visited:
                print(v)
                
                # Mark as visited:
                visited.add(v)
                
                for next_vert in self.get_neighbors(v):
                    q.enqueue(next_vert)

g = Graph()
g.add_vertex(99)
g.add_vertex(3)
g.add_vertex(3490)
g.add_edge(99, 3490) # Connect node 99 to node 3490
g.add_edge(99, 3)   #
        
        
    def get neighbors(self, vertex_id):