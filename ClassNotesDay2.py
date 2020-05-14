"""
*explore*: 
    print this node
    *explore* all its unvisited neighbors (no unvisited neighbors return)
    return
"""

"""
Start of class at 10:04 on Beej mac
"""

class Graph:
    
    def  __init__(self):            # Make a constructor
        self.vertices = {}          # Make a dictionary of vertices
        
    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = set()    # For each of the verts there will be a set of edges
        
    def add_edge(self, v1, v2):     # This edge is connected to 2 verts
        """ Add edge from v1 to v2. - this is for undirected """
        """ For directed, have to add from v2 to v1 also """
        
        if v1 in self.vertices and v2 in self.vertices: # Test to see if v1 and v2 are in the graph
            self.vertices[v1].add(v2)                   # if in the graph then add v2 to one of the edges
                                                        # in the set of edges that are connected to v1
            
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

    def dft_recursive(self, start_vert, visited = None):
        print(start_vert)
        
        if visited is None:
            visited = set()
            
        if path is None:
            path = []
            
        visited.add(start_vert)
        
        # Make a copy of the list, adding the new vert on
        path = path + [start+vert]
        
        # Base case
        if start_vert == target_value:
            return path
        
        for child_vert in self.vertices[start_vert]
            if child_vert not in visitied:
                self.dft_recursive(child_vert, target_valeu, visited, path)
                
                if new_path:
                    return new_path
                
        return None

g = Graph()
g.add_vertex(99)
g.add_vertex(3)
g.add_vertex(3490)
g.add_edge(99, 3490) # Connect node 99 to node 3490
g.add_edge(99, 3)      # Connect node 99 to node 3
g.add_edge(3, 99)      # Connect node 3 to node 99

#print(g.get_neighbors(99))
#print(g.get_neighbors(3))
​
g.bft(99)
        
        
    def get neighbors(self, vertex_id):