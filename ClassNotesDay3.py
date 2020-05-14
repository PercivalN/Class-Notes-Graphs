"""
The structure and interpretation of computer programs (book recommendation)

If in Denver which city is the farthest awaydatetime A combination of a date and a time. 

DFS - 

BFS - When ever think about distance, think BFS.

What is a traversal
"""

"""
islands = [[0, 1, 0, 1, 0],
           [1, 1, 0, 1, 1],
           [0, 0, 1, 1, 0],
           [1, 0, 1, 0, 0],
           [1, 1, 0, 0, 0]]

def island_counter(matrix):
    # Create a "visited" data structure
    visited = []
    
    for i in range(len(matrix)):
        visited.append([False] * len(matrix[0]))    # What does matrix[0] mean
        
        island_counter = 0
        
        # Walk through all the nodes, elements in the input matrix
        for col in range(len(matrix[0])):
            for row in range(len(matrix)):
                
                # If it's not visited:
                if not visited[row][col]:
                    # If the value in the matrix at this position is a 1:
                    if matrix[row][col] == 1:
                        # Do a traversal and mark each as visited
                        visited = dft(row, col, matrix, visited)
                        
                        # Increment island counter
                        island_counter += 1
                        
                    else:
                        # We hit water (0)
                        visited[row][col] = True
                        
    return island_counter

def 

def get_neighbors(row, col, matrix): 
    neighbors = []
    
    # Check north
    if row > 0 and matrix[row - 1][col] == 1:
        neighbors.append((row-1, col))
        
    # Check south
    if row < len(matrix) - 1 and matrix[row + 1][col] == 1:
        neighbors.append((row+1, col))
        
    # Check west
    if col > 0 and matrix[row][col - 1] == 1:
        neighbors.append((row, col - 1))
        
    # Check east

"""
""" redo @ 10:32 Beejs clock """


"""
Generating random data
----------------------

If you have a deck of cards, how can you choose 10 at random?
"""

def populate_graph(self, num_users, avg_friendships):
    # Reset graph
    self.last_id = 0
    self.users = {}         # Nodes
    self.friendships = {}   # Edges
    
    # Generate the users
    
    
    # Generate all friendship combinations
        # But not the duplicate combinations
            A <-> B
            B <-> A
            
    # Shuffle them
    
    # Choose the first X out of the list

    
    