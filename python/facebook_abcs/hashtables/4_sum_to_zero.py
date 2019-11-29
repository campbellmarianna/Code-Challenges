'''
Prompt:
Given four lists A, B, C, D of integer values, compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.

Input Format

Array A, space separated integers

Array B, space separated integers

Array C, space separated integers

Array D, space separated integers

Constraints

Arrays A, B, C and D are of the same size

Output Format

N, number of tuples for which A*i* + B*j* + C*k* + D*l* = 0

Sample Input 0

1 2
-2 -1
-1 2
0 2
Sample Output 0

2
Explanation 0

The two tuples are:

(0, 0, 0, 1) -> A[0] + B[0] + C[0] + D[1] = 1 + (-2) + (-1) + 2 = 0
(1, 1, 0, 0) -> A[1] + B[1] + C[0] + D[0] = 2 + (-1) + (-1) + 0 = 0
Hence the answer is 2.
'''
# array a
# 1
# array b
# -2
# array c
# -1
# arr d
# 0
# add them 1 + -2 + -1 + 0
# check does the sum equal 0? no
# next value in arr a
# 2
# arr b
# -2
# arr c
# -1
# arr d
# 0
# add them 2 + -2 + -1 + 0
# check does the sum equal 0? no

# arr 1
# 1
# arr 
# -2
# add them 1 + -2 = -1
# what do I need to get zero -1 need 1 and 0
# is 0 or 1 in arr c

# # A B
# [0, 0] => [1, -2] => -1 :0 
# [0, 1] => [1, 1] => 2 :0 
# [1, 0] => [2, -2] => 0 :0 
# [1, 1] => [2, -1] => 1 :0 

# # C D
# [0, 0] = > [-1, 0] = > -1  
# [0, 1] = > [-1, 2] = > 1 
# [1, 0] = > [2, 0] = > 2 
# [1, 1] = > [2, 2] = > 4

# result += 0 + 0
# when you have four values and you want to see what combination of values equal zero you can get the sum of two values, get the sum of the other two values and see if they equal zero

# Very simplified way to solve the problem is to have four for loops and check every combination of numbers and check if they equal zero if they are increment and counter and return the counter at the end
import fileinput
def four_sum(A,B,C,D):
  match_counter = 0
  for a in A:
    for b in B:
      for c in C:
        for d in D:
          sum = a + b + c + d
          if sum == 0:
            match_counter += 1
  return match_counter

A = [1, 2]
B = [-2,-1]
C = [-1, 2]
D = [0, 2]
# print(four_sum(A, B, C, D))

# pos: Sum to numbers # neg: Sum to numbers
# 4                  + -4                   = 0

# Solution Idea inspired by Another Casual Coder http://anothercasualcoder.blogspot.com/2016/12/leetcode-4sum-ii.html
def FourSumCount(A, B, C, D):
  ht = {}
  for c in C:
    for d in D:
      sum = c + d
      if ht.get(sum) == None:
        ht[sum] = 0
      else:
        ht[sum] += 1
  result = 0
  for a in A:
    for b in B:
      sum = -(a+b)
      if ht.get(sum) != None:
        result += 1
  return result


# print(FourSumCount(A, B, C, D))

# Third Iteration

# get user input
four_list = []
n = int(input())
for i in range(n):
  arr = input().strip().split(' ')
  print(arr)
  four_list[i] = arr
A = four_list[0]
B = four_list[1]
C = four_list[2]
D = four_list[3]

def four_sum_count(A, B, C, D):
  ht = {}
  for c in C:
    for d in D:
      sum = c + d
      if ht.get(sum) == None:
        ht[sum] = 0
      else:
        ht[sum] += 1
  desired_sum_found = 0
  for a in A:
    for b in B:
      sum = -(a+b)
      if ht.get(sum) != None:
        desired_sum_found += 1
  return desired_sum_found


# print(four_sum_count(A, B, C, D))


