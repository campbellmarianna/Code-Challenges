'''
Prompt:
Given a  2D Array, :

1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
We define an hourglass in  to be a subset of values with indices falling in this pattern in 's graphical representation:

a b c
  d
e f g

There are  hourglasses in , and an hourglass sum is the sum of an hourglass' values. Calculate the hourglass sum for every hourglass in , then print the maximum hourglass sum.

For example, given the 2D array:

-9 -9 -9  1 1 1 
 0 -9  0  4 3 2
-9 -9 -9  1 2 3
 0  0  8  6 6 0
 0  0  0 -2 0 0
 0  0  1  2 4 0

We calculate the following  hourglass values:

-63, -34, -9, 12, 
-10, 0, 28, 23, 
-27, -11, -2, 10, 
9, 17, 25, 18
Our highest hourglass value is  from the hourglass:

0 4 3
  1
8 6 6

Note: If you have already solved the Java domain's Java 2D Array challenge, you may wish to skip this challenge.

Function Description

Complete the function hourglassSum in the editor below. It should return an integer, the maximum hourglass sum in the array.

hourglassSum has the following parameter(s):

arr: an array of integers
Input Format

Each of the  lines of inputs  contains  space-separated integers .

Constraints

Output Format

Print the largest (maximum) hourglass sum found in .

Sample Input

1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 2 4 4 0
0 0 0 2 0 0
0 0 1 2 4 0

Sample Output
19

The hourglass with the maximum sum () is:

2 4 4
  2
1 2 4
'''
# Given a 2D array return the highest hourglass sum
# Input: 2D array
# Output: int - highest hourglass sum
# Hourglass
#    a b c
#      d
#    e f g
# Psudeocode
# create a func that takes in 2darray
  # creater a counter
  # create a hg sum list
  # reach every value in the 2d array sequence
    # check to see if this value can produce and hourglass and return it's sum or None
    # if the sum is not None add it to the hg sum list otherwise continue to the next element
  # return the highest hg sum

# create a func to get the sum of one hourglass
  # go to each position
  # check if the element at the index gives you a index error if so continue to next number and if it does not add the number to the counter the value before adding to the counter
  # increment a counter by the value
  # return the value

# Code
import math
import os
import random
import re
import sys


def hourglassSum(arr, i, j): 
  '''Return the sum of one hourglass'''
  hg_counter = 0
  top = arr[i][j] + arr[i][j+1] + arr[i][j + 2]
  middle = arr[i + 1][j + 1]
  bottom = arr[i + 2][j] + arr[i + 2][j + 1] + arr[i + 2][j + 2]
  hg_counter = top + middle + bottom
  return hg_counter

def maxHourglassSum(arr):
  '''Return the largest (maximun) hourglass sum found in given 2D array.'''
  hg_sum_list = []
  # reach every value in the 2d array sequence
  for i in range(0, len(arr)): # accessing each inner list
    for j in range(0, len(arr[i])): # accessing the element in the inner list
      # only reach valid elements where a hourglass can be formed
      if i < 4 and j < 4:
        hg_sum_list.append(hourglassSum(arr, i, j))
  return max(hg_sum_list)



if __name__ == '__main__':
    # fptr = open(
    #     os.environ['./2d_array_output.txt'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    # result = hourglassSum(arr)
    print(maxHourglassSum(arr))

    # fptr.write(str(result) + '\n')

    # fptr.close()
