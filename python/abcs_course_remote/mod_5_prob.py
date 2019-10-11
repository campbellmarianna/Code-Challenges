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
  # return 1
# otherwise 
  # return 0
import re
regex = re.compile('[^a-zA-Z]')
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


print(isPalindrome('A man, a plan, a canal, Panama.'))  # na
