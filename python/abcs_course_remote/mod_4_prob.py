'''
Prompt:
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Return 0 / 1 ( 0 for false, 1 for true ) for this problem.

Examples:
"Race Car" # returns 1

"Race a Car" # returns 0

"otto" # returns 1

"A man, a plan, a canal, Panama."
'''
# anna return 1
# make lowercase, take away spaces and all non alpha num char
# take have the string
# reverse left half
# check if both strings are the same
# import copy
  # return 1
# otherwise 
  # return 0
# import re
# regex = re.compile('[^a-zA-Z]')
def isPalindrome(str_1):
  if str_1.isalnum() == False: # non alphanums in string
    # take away spaces and all non alpha num char
    str_1 = regex.sub('', str_1)
  if str_1.islower() == False:
    # make lowercase
    str_1 = str_1.lower()
  # take have the string
  half_str_len = len(str_1)//2
  left_half = ''
  for char_index in range(half_str_len):
    left_half += str_1[char_index]
  # reverse left half
  left_half = left_half[::-1]
  # specify right half
  str_1 = str_1[len(str_1) - half_str_len:]
  # check if both strings are the same
  if left_half == str_1:
    return 1
  else:
    return 0

# print(isPalindrome('A man, a plan, a canal, Panama.'))  # na

# learned how to check for palindrome in one line from YT video: https://www.youtube.com/watch?time_continue=210&v=u1jdar3WADY

import re
regex = re.compile('[^a-zA-Z]')
def isPalindrome2(str_1):
  if str_1.isalnum() == False:  # non alphanums in string
    # take away spaces and all non alpha num char
    str_1 = regex.sub('', str_1)
  if str_1.islower() == False:
    # make lowercase
    str_1 = str_1.lower()
  if str_1 == str_1[::-1]:
    return 1
  else:
    return 0

# print(isPalindrome2('A man, a plan, a canal, Panama.'))

## Reviewing strategy to solve the problem using the canvas course
# palindrome - a string where the characters are the same backwards and forwards
def clean_string(dirty_string):
  print(f"Dirty string: {dirty_string}")
  cleaned_string = ""
  for element in dirty_string:  # 0(n)
    if element.isalpha(): 
      cleaned_string = cleaned_string + element
  return cleaned_string

# Solution that only works when input is all letters
def isPalindrome3(input_str):
  '''
  Return 1/0 1 is True and 0 is False considering if a given string is a palindrome or not 
  Runtime: 0(n) for n input string
  '''
  # size of n is len of input_str
  # considering only alphanumeric characters and ignoring cases.
  cleaned_string = clean_string(input_str) # same size as input_str
  # determine if it is a palindrome
    # Method 1: is the string the same backwards and forwards?
  print(f"Cleaned string: {cleaned_string}")
  if cleaned_string == cleaned_string[::-1]:
    return 1
    # Method 2: is the first half of the string the same as the second half?
  # Return 0 / 1
  return 0


print(isPalindrome3("Otto"))
print(isPalindrome3("abc"))
print(isPalindrome3("A man, a plan, a canal, Panama"))
# print(isPalindrome3("1a2")) # Test case fails

## Refresher on Python Built-in Range Function 
# sum = 0
# for i in range(10):
#   sum = sum + i
# print(sum)

## List and String Slicing
# Activity 1
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#          0, 1, 2, 3, 4, 5, 6, 7, 8, 9
#        -10,-9,-8,-7,-6,-5,-4,-3,-2,-1

# list[start:end:step]

# print(my_list[8::-2])

# Activity 2
sample_url = 'http://coreyns.com'
# print(sample_url)

## Reverse the url
# print(sample_url[::-1])

# # Get the top level domain
# print(sample_url[-4:])

# # Print the url without the http://
# print(sample_url[7:])

# # Print the url without the http:// or the top level domain
# print(sample_url[7:-4])


## Reverse using String Slicing
# >> > x
# 8642
# >> > x = 2442
# >> > x == int(str(x)[::-1])
# True
# >> > x == 123
# False
# >> > x = 123
# >> > x == int(str(x)[::-1])
# False
# >> > a = ['apples'. 'bananas', 'candy']
# File "<stdin>", line 1
# a = ['apples'. 'bananas', 'candy']
# ^
# SyntaxError: invalid syntax
# >> > a = ['apples', 'bananas', 'candy']
# >> > a[::-1]
# ['candy', 'bananas', 'apples']
# >> > a
# ['apples', 'bananas', 'candy']
# >> > a.reverse() # reverse method built in reverses a list inplace

"race a car"
'''
Prompt:
Minimum Characters required to make a String Palindromic
You are given a string. The only operation allowed is to insert characters in the beginning of the string. Return the number of characters that are needed to be inserted to make the string a palindrome string

Examples:
Input: ABC
Output: 2

Input: AACECAAAA
Output: 2
'''


def minCharsisPalindrome(str_1):
  '''Return the minimum number of characters that are needed to a make the string a palindrome.'''
  # count = 0
  # index = 0
  # original = []
  # for char in str_1:
  #   original.append(char)
  # for char in 
  #   str_2 = 
  #   # increment
  #   # check
  #     return count

import copy

def minimumCharacters(str_1):
  # we have are string
  # make copy of input string
  input_str = copy.deepcopy(str_1)
  input_len = len(input_str)
  reverse_input = input_str[::-1]
  # keep track of count
  count = -1
  # keep track of index going backwards
  # loop chars in string
  for char_index in range(1, input_len + 1):
    # add what is last to the front
    last_index = -char_index
    print(f"LAST CHAR: {str_1[last_index]}")
    str_1 = str_1[last_index] + str_1
    print(f"NEW STRING: {str_1}")
    count += 1
    # check slice string is same as copy or the same as reverse copy
    if str_1[:input_len] == input_str or str_1[:input_len] == reverse_input:
      return count


# print(minimumCharacters('ABC'))
