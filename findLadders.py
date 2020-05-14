import string

def find_ladders(begin_word, end_word):
    visited = set()
    q = Queue()
    
    q.enqueue([begin_word])
    
    while q.size() > 0:
        
        path = q.dequeue()
        
        v = path[-1] # Look at the last element in the path
        
        if v not in visited:
            visited.add(v)
            
            #Did we reach the end word?
            if v == end_words:
                return path
            
            for neighbor in get_neighbors(v):
                path_copy = list(path)
                path.copy.append(neighbor)
                
                q.enqueue(path_copy)
                
# REead in all the words into a list
with open('words.txt') as f:
    words = f.read().split()
    
# Put all words ina set for 0(1) access
word_set = set()

for w in words:
    word_set.add(w.lower())
    
letters = list(string.ascii_lowercase)

def get_neighbors(word):
    # We return this
    neighbors = []
    
    string_word = list(word)    # ['w', 'o', 'r', 'd']
    
    # For each letter ...
    for i in range(len(string_word)):
        for letter in letters:
            temp_word = list(string_word)
            temp_word[i] = letter
            
            w = "".join(temp_word)  # ['w', 'o', 'r', 'd'] -> "word"
            
            # If it's a valid word, its a neighbor
            # (but don't add a word as a neighbor to itself)
            if w != word and w in word_set:
                neighbors.append(w)
                
    return neighbors