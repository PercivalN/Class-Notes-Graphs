"""
Breadth-First Traversal

Add starting node to a queue

While queue isn't empty:
    Dequeue the first vert
    If that vert isn't visited:
        MArk as visited
        Add all its unvisited neighbors to the queue
        
        
Depth-First Trasversl

Add starting node to a stack

While stack isn't empty:
    Pop the first vert
    If that vert isn't visited:
        Marked as visted
        Push all its unvisited neighbors to the stack
        
"""

"""
1. What is distance 0, 1, 2?
2. Do a graph with Queues - FIFO
3. Do a graph with Stacks - FILO
4. What's breadth first search?
    Explore as wide as possible
5. What's depth first search?
    Explore as deep as possible
6. Parent nodes - keeping track of the parent nodes is a good way to find the shortest path
7. Get the terminology in, from videos
8. Look at pseudo code for bft

"""
    
    
"""
Day2 questions:
1. recursive needs base case (review recursive again)
2.

"""

"""
Day2:

How to solve any graph problem
1. Translate the problem into graph terminology
2. Build the graph
3. Traverse it

Word Ladders Problem
--------------------

begin:  hit
end:    cog

hit -> hot -> cot -> cog

begin:  sail
end:    boat

sail -> bail -> 
BFS is the shortest possibles to get from one to another

begin:  hungry
end:    happy   

"""