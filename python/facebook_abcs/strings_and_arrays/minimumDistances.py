'''
Prompt:
We define the distance between two array values as the number of indices between the two values. Given , find the minimum distance between any pair of equal elements in the array. If no such value exists, print .

For example, if , there are two matching pairs of values: . The indices of the 's are  and , so their distance is . The indices of the 's are  and , so their distance is .

Function Description

Complete the minimumDistances function in the editor below. It should return the minimum distance between any two matching elements.

minimumDistances has the following parameter(s):

a: an array of integers
Input Format

The first line contains an integer , the size of array .
The second line contains  space-separated integers .

Constraints

Output Format

Print a single integer denoting the minimum  in . If no such value exists, print .

Sample Input

6
7 1 3 4 1 7
Sample Output

3
Explanation
Here, we have two options:

 and  are both , so .
 and  are both , so .
The answer is .
'''
# Key action: Return minimun distance of two matching elements in a given array
# Input: First line int:size of the array
#        Second line: ints with spaces
# Output: The minimun distance of one pair of matching elements

# check if there are any matching ints in the array (set) 0(n)
  # get the distance of each 0(n)..X the of matches we find 0(n)
    # get the index of both then subtract them
# return -1
# return the min distance out of them all

# Sample Input:
# 6
# 7 1 3 4 1 7
# Sample Output:
# 3

def minimumDistances(a):
  '''Return the minimum distance between any two matching elements'''
  # Check for matching values
  duplicates = []
  seen = set()
  for num in a:
    if num in seen:
      duplicates.append(num)
    else:
      seen.add(num)
  # check for no duplicate values
  if len(duplicates) == 0:
    return -1
  distances = []
  # get the distance of each matching elements
  for duplicate in duplicates:
    indices = []
    for i in range(0, len(a)):
      if a[i] == duplicate:
        indices.append(i)
        if len(indices) == 2:
          break
    distances.append(abs(indices[0] - indices[1]))
  # After receiving distances return the smallest 
  return min(distances)


# Test Inputs:
# - [7, 1, 3, 4, 1, 7]
# - [3, 2, 1, 2, 3] # 2
# - [1,2,3,4,10]
print(minimumDistances([7, 1, 3, 4, 1, 7]))
