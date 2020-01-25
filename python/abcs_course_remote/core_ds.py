'''
Key Topics:
-Strings and Arrays
- Trees and Graphs
- Recursion and DP

Steps to know the key topics
1. Implement Data Structure
2. Implement common methods of the data structure
3. Solve or review (use steps in notebook) a compound algorithm (solving a problem using the primary data structure with another)
'''

#### Strings and Arrays
# 1. Implement Data Structure
my_str = 'marianna'
arr = []

# 2. Implement common methods of the data structure
# len(str)  #1
str() 
my_str2 = my_str[0:4] # slicing # O(c) for the number of characters copied

print(my_str.count('a'))

len(arr) # O(1)
arr.append('give') # O(1)
arr.index('give') # O(n) for the number of indexs it take to get to the one that matches the index in python it is O(1)

# 3. Solve or review(use steps in notebook) a compound algorithm(solving a problem using the primary data structure with another)
# Reverse a string https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/879/
9 -7
'''
Prompt: 
Write a function that reverses a string. The input string is given as an array of characters char[].

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

You may assume all the characters consist of printable ascii characters.

Example 1:

Input: ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:

Input: ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
'''
# input: list of strings
# output: return nothing modify list
# iterator front to back, back to front and switch items in the list


def reverseString(a):  # ["h","e","l","l","o"]
    # create i 3 and j 1
    i, j = 0, len(a) - 1
    while i < j:
        a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1
    return a

print(reverseString(["h", "e", "l", "l", "o"]))

#### Trees and Graphs
### 1. Implement Data Structure
## tree
# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.children = []

# class Tree:
#     def __init__(self):
#         self.root = None

## graph
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.edges = []

#     def add_directed_edge(self, node):
#         self.edgges.append(node)
    
#     def add_undirected_edge(self, node):
#         self.edges.append(node)
#         node.edges.append(node)

# node1 = Node(1)
# node2 = Node(2)
# node1.add_directed_edge(node)

### 2. Implement common methods of the data structure and solve or review (use steps in notebook) a compound algorithm (solving a problem using the primary data structure with another)
## - level order traversal
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None
    
    def print_bfs(self):
        if not self.root:
            return
        
        queue = [self.root]

        while len(queue) > 0:
            current_node = queue.pop(0)
            print(current_node.data)
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)


tree = Tree()
tree.root = Node(9)

tree.root.left = Node(5)
tree.root.right = Node(11)

tree.root.left.left = Node(3)
tree.root.left.right = Node(7)

tree.print_bfs()

## - traverse a graph
class Graph():
    def __init__(self):
        self.nodes = {}

    def add_node(self, node):
        self.nodes[node] = []
    
    def add_edge(self, node_a, node_b):
        self.nodes[node_a].append(node_b)
        self.nodes[node_b].append(node_a)
    
    def subgraph(self, root):
        to_visit = [root]

        visited = set()

        while len(to_visit) > 0:
            node = to_visit.pop(0)
            if node not in visited:
                print(node)
                visited.add(node)

            for neighbor in self.nodes[node]:
                to_visit.append(neighbor)

graph = Graph()

graph.add_node('A')
graph.add_node('B')
graph.add_node('C')
graph.add_node('D')
graph.add_node('E')
graph.add_node('F')
graph.add_node('Z')

graph.add_edge('A', 'B')
graph.add_edge('A', 'C')
graph.add_edge('A', 'D')
graph.add_edge('C', 'E')
graph.add_edge('E', 'F')
graph.add_edge('D', 'B')

graph.subgraph('A')

# Search and Sorting
# Find the minimum element
# input: sorted arr
# output

def find_pivot_index(input_list):
    # List is sorted, but then rotated.
    # Find the minimum element in less than linear time
    # return it's index
    for current_element_index in range(1, len(input_list)):
    if input_list[current_element_index] < input_list[current_element_index-1]:
        return current_element_index
    return 0
    # otherwise, that element is the minimum element
    # return the minimum_element