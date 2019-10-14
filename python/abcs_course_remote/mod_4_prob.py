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

print(isPalindrome2('A man, a plan, a canal, Panama.'))

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
print(sample_url)

## Reverse the url
# print(sample_url[::-1])

# # Get the top level domain
# print(sample_url[-4:])

# # Print the url without the http://
print(sample_url[7:])

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
