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


# print(first_missing_positive_integer2([1]))


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

'''
Prompt:
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?


Example 1:
Input: [2,2,1]
Output: 1

Example 2:
Input: [4,1,2,1,2]
Output: 4

There are several approaches to this problem. Start with one that makes sense to you- so long as you pass all the tests. 

Remember to try to solve the problem first by using the most naive solution, then start asking yourself questions about the operations you're doing to try to reduce the amount of time and space used. 

Below are a few hints that describe each approach. 

Try to get the first one working, then take a look at a few of the approaches.

Approach 1: use another data structure to hold the numbers you have found.
Time complexity (if you use another array) may be up to O(n^2). If you use a hash table, you may be able to get up to O(n). 
Space complexity is O(n), which is not constant space.
Approach 2: use math and Set
Time complexity: likely O(n), as O(n + n) is really just O(n). The number of steps grows linearly.
Space complexity: O(n), as the addition will require the whole list to be duplicated.
Approach 3: Bit Manipulation
Time complexity: O(n)
Space complexity: O(1)
You'll have to look up this approach on your own - what kind of bitwise operations are there? What happens when you use them? 
The solution for this particular problem is easily found on google, so try looking up the Bitwise Operations in Python to try to work through it. 
'''
# I: Int - Single Int
# O: Int: Single Int
# Solutions
  # - create a a hashtable, hashmap, dictionary(in python)
# Psudocode
# func pass in array
#   create dic
#   loop array
#     check in curr_num is in the dict
#       increment key's value
#     else:
#       add curr_num with value 1
#   loop values
#     if a value equal 1
#       return key
    
def single_number(integers):
  '''Return a single element that doesn't appear twice in an array'''
  seen = {}
  for integer in integers:
    if integer in seen.keys():
      seen[integer] += 1
    else: # not seen before
      seen[integer] = 1
  for num in seen.keys():
      if seen[num] == 1:
        return num
  
# print(single_number([4, 1, 2, 1, 2]))

# Time Complexity: 0(n)
# Space Complexity: 0(n)
##### Another way to solve it ##### Using guided video in Problem Solving Course

for every element in the input list
  if I have seen this element before 
    remove it from the list of elements I have seen before
  otherwise:
    add it to the list of elements I have seen before
[2,2,1] #1
[4,1,2,1,2] # 4

'''
Prompt: 
Given numRows, generate the first numRows of Pascal’s triangle.
Pascal’s triangle : To generate A[C] in row R, sum up A’[C] and A’[C-1] from previous row R - 1.
Example:
Given numRows = 5,
Return
[
     [1],
     [1,1],
     [1,2,1],
     [1,3,3,1],
     [1,4,6,4,1]
]

1.
Example:
Given numRows = 7,
Return
[
     [1],
     [1,1],
     [1,2,1],
     [1,3,3,1],
     [1,4,6,4,1]
     [1,5,10,10,5,1]
     [1,6,15,20,15,6,1]
]
'''
def pascal_triangle(numRows): 
  rows = numRows # 5
  triangle = [] # [[1]]
  for i in range(rows): # 1
      row = []
      row.append(1) # [1, ]
      for j in range(i): # 0
          if len(triangle) == 0:  # no previous row to refer to
              break
          if i - 1 == 0:  # if accessing first row no need to add from above
             # the second element in each row is a count - noticed pattern
            row.append(i) 
            break
          try: # try to access previous row
            pre_row = triangle[i - 1]
          except IndexError:
            break
          curr_position = j + 1 # 1
          # Try to access a numbers above
          elem_1 = pre_row[curr_position - 1]
          # elem_1 = pre_row[0]
          try: 
            elem_2 = pre_row[curr_position]
          except IndexError:
            elem_2 = 0
          new_val = elem_1 + elem_2
          row.append(new_val)
      triangle.append(row) 
  return triangle

print(pascal_triangle(7))

#### List Manipulation Assessment #####
'''
Prompt:
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:
Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.

Example 2:
Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
'''
# Wrote Psuedocode on paper
# My Solution 
def plusOne(digits):
        if digits[-1] != 9:
            last_digit = digits.pop()
            result = last_digit + 1
            digits.append(result)
            return digits
        else:
            digits_str = ''
            for num in digits:
                str_num = str(num)
                digits_str += str_num
            big_digits_int = int(digits_str)  # '4999' => 4999
            big_digits_int += 1
            big_digits_str = str(big_digits_int)
            output_list = []
            for num in big_digits_str:
                num_int = int(num)
                output_list.append(num_int)
            return output_list


digits = [4, 9, 9, 9]
plusOne(digits)
# Test Input:
# 4999 => [4, 9, 9, 9]
# 5000 => [5, 0, 0, 0]

# 123
# 124
