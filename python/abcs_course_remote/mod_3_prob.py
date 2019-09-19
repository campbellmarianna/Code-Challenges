'''
Prompt #1:
Given an unsorted integer array, find the first missing positive integer.

Example:
Given [1,2,0] return 3,
[3,4,-1,1] return 2,
[-8, -7, -6] returns 1
Your algorithm should run in O(n) time and use constant space.

'''
# Key action: Find the first missing positive integer
# Input: Unsorted Integar array
  # Positive and Neg nums
# Output: Integer
## Attempted Solution
def isNegatives(integers):
  '''Return True if given list of integers are all negatives'''
  for num in integers:
    if num > 0: # found a positive
      return False
  return True

def first_missing_positive_integer1(integers): # [1, 2, 0]
  '''Return the first missing positive in a given unsorted integer array'''
  # Check if all ints are negative return one
  if isNegatives(integers):
    return 1
  sorted_arr = sorted(integers) # [0, 1, 2]
  print(f"Sorted_arr: {sorted_arr}")
  correct_seq = [] # [0, 1, 2]
  for num in range(sorted_arr[0], len(sorted_arr) + 1):
    correct_seq.append(num)
  print(f"Correct_seq: {correct_seq}")
  # Take out 0 if there is no zero in sorted_arr
  zero = 0
  if zero not in sorted_arr and zero in correct_seq:
    correct_seq.remove(0)
  print(correct_seq)
  for i in range(0, len(sorted_arr)):
    if sorted_arr[i] != correct_seq[i]:
      print(f"comparing: {sorted_arr[i]} == {correct_seq[i]}")
      # Check if current num is positive
      if correct_seq[i] > 0:
        return correct_seq[i]
  return sorted_arr[len(sorted_arr) - 1] + 1
  # only compare psitive vales


# print(first_missing_positive_integer1([-5, 2, -4, 1, 2, 2]))

## Follow UMPIRE Process
# Found all positive integers from the highest integers
# I could use a list or a hashmap which is a dictionary in python

# 1 -
# 2
# 3 -
# 4 -

# Psudocode
# create an empty list
# for every number in the input list
#   if the number is smaller than 0, ignore the number
#   if the number is larger than the curent length of the list, resize the list be of at length
#   set the value of the place in the list corresponding with that integer to True

def first_missing_positive_integer2(integers):  # [1, 2, 4]
  '''Return the first missing positive in a given unsorted integer array'''
  found_integers = []  # 0
  for integer in integers:
    if integer < 0:
      continue  # ignore the number
    if integer + 1 > len(found_integers):
      extend_size = integer - len(found_integers) + 1
      found_integers.extend([False] * extend_size)
    found_integers[integer] = True
  missing_integer = 0
  for position in range(1, len(found_integers)):
    if found_integers[position] == False:
      missing_integer = position
      return missing_integer
  # check if the integers were all negative
  if missing_integer == 0 and len(found_integers) == 0:
    return 1
  elif missing_integer == 0 and len(found_integers) > 0:
    return len(found_integers)


print(first_missing_positive_integer2([-8, -7, -6]))


'''
Prompt #2:
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


# rotate_array([1, 2, 3, 4, 5, 6, 7], 3)
