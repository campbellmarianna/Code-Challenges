'''
Prompt:
Given an array, rotate the array to the right by k steps, where k is non-negative.

Input: [1,2,3,4,5,6,7] and k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

Input: [-1,-100,3,99] and k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]

Note:
Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
Could you do it in-place with O(1) extra space?
Do not return anything, modify the input array in-place instead.
'''
# Input: [1, 2, 3, 4, 5, 6, 7] and k = 3
# Output: [5, 6, 7, 1, 2, 3, 4]
# Last three get moved from the end to the front
# for 1 to k:
# end_of_list = take the number from the end of the list 
# put it on the beginning of the list


def rotate_array(input_array, k):
  '''Rotate the array to the right by k steps'''
  for _ in range(0, k):
    end_val = input_array.pop()
    input_array.insert(0, end_val)
  print(input_array)


rotateArray([1, 2, 3, 4, 5, 6, 7], 3)
