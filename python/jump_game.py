# 9:23 pm
'''
Prompt:
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

Example:

Input: [2,3,1,1,4]
target = 4
curr_index = 0
curr_val = 2
is 2 greater than 1
yes, so 
jump = 1
diff = 4 - 2
check to see if we have 
jumps = 2+1+1 = 3
jumps
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2.
    Jump 1 step from index 0 to 1, then 3 steps to the last index.
'''
# input list all positive numbers
# input: list
# output: minimum number of moves 
# options:
# - take the number of steps identified by the number your on
# - go to next number
# there are duplcates
# empty list return 0
