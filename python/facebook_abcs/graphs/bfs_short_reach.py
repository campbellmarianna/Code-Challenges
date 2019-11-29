'''
Prompt:
Consider an undirected graph where each edge is the same weight. Each of the nodes is labeled consecutively.

You will be given a number of queries. For each query, you will be given a list of edges describing an undirected graph. After you create a representation of the graph, you must determine and report the shortest distance to each of the other nodes from a given starting position using the breadth-first search algorithm (BFS). Distances are to be reported in node number order, ascending. If a node is unreachable, print  for that node. Each of the edges weighs 6 units of distance.

For example, given a graph with  nodes and  edges, , a visual representation is:

image
The start node for the example is node . Outputs are calculated for distances to nodes  through : . Each edge is  units, and the unreachable node  has the required return distance of .

Function Description

Complete the bfs function in the editor below. It must return an array of integers representing distances from the start node to each other node in node ascending order. If a node is unreachable, its distance is .

bfs has the following parameter(s):

n: the integer number of nodes
m: the integer number of edges
edges: a 2D array of start and end nodes for edges
s: the node to start traversals from
Input Format

The first line contains an integer , the number of queries. Each of the following  sets of lines has the following format:

The first line contains two space-separated integers  and , the number of nodes and edges in the graph.
Each line  of the  subsequent lines contains two space-separated integers,  and , describing an edge connecting node  to node .
The last line contains a single integer, , denoting the index of the starting node.
Constraints

Output Format

For each of the  queries, print a single line of  space-separated integers denoting the shortest distances to each of the  other nodes from starting position . These distances should be listed sequentially by node number (i.e., ), but should not include node . If some node is unreachable from , print  as the distance to that node.

Sample Input
2 # the number of queries
4 2 # n: number of nodes m: number of edges in the graph
1 2 # u and v: describing an edge connecting node u to node v
1 3 
1
3 1
2 3
2 # s: denoting the index of the starting node.

Sample Output
6 6 -1
-1 6
'''
# Very helpful Bread First Search is looping through a sorted array and adding to a queue
# https: // www.youtube.com/watch?v = -uR7BSfNJko

# Getting user input Iteration #1
# N = int(input())
# print(N)
# for _ in range(N):
#     parts = input().strip().split(' ')
#     print(parts)


for line in fileinput.input():
    parts = line.strip().split(' ')
    print(parts)

# Along with Breadth First Search Algorithm by lorisrossi https://www.hackerrank.com/challenges/bfsshortreach/forum 
def bfs(n, m, edges, s):
    from collections import deque

    # Build graph
    graph = {}
    for num in range(1, n+1):
        graph[num] = set()
    for l, r in edges:
        graph[l].add(r)
        graph[r].add(l)

    reached = {}
    # Explore graph once
    frontier = deque([(s, 0)])
    seen = {s}

    while frontier:
        curr_node, curr_cost = frontier.popleft()
        for nbour in graph[curr_node]:
            if nbour not in seen:
                seen.add(nbour)
                reached[nbour] = curr_cost+6
                frontier.append((nbour, curr_cost+6))

    result = []
    for node in range(1, n+1):
        if s != node:
            result.append(reached.get(node, -1))

    return result
