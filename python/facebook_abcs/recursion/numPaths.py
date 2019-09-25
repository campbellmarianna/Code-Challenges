'''
Prompt:
A robot is located at the top-left corner of a MxN grid. The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid . How many unique paths are there?

Input Format

Two integers, M and N, both specified in the same line to indicate the size of the grid.

Constraints

1 ≤ M ≤ 10

1 ≤ N ≤ 10

Output Format

An integer for the number of unique paths.

Sample Input 0

3 3
Sample Output 0

6
Explanation 0

In a 3x3 grid, there are 6 possible paths, as shown in the picture below.

image
'''
# How many was can 
def numPaths1(M, N):
  return M + N

# print(numPaths(3, 3))

# Solution Idea provided Geeks for Geeks https://www.geeksforgeeks.org/count-possible-paths-top-left-bottom-right-nxm-matrix/


def numberOfPaths(m, n):
  # If either given row number is first
  # or given column number is first
  if (m == 1 or n == 1):
    return 1

  # If diagonal movements are allowed then the last additon is required
  return numberOfPaths(m-1, n) + numberOfPaths(m, n-1)

print(numberOfPaths(3, 3))

# Followed video explanation to learn about how to implement a recursive function 
# https://www.youtube.com/watch?v=UaJTwEFYltM
def uniquePaths(n, m):
  # If either given row number is first
  # or given column number is first
  if (n == 0 and m == 0):
    return 0

  if n == 0 or m == 0:
    return 1
  
  # If diagonal movements are allowed then the last additon is required
  return uniquePaths(n-1, m) + uniquePaths(n, m-1)


# print(uniquePaths(3, 3))

