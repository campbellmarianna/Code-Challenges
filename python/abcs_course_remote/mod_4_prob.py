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


# print(isPalindrome3("Otto"))
# print(isPalindrome3("abc"))
# print(isPalindrome3("A man, a plan, a canal, Panama"))
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
## Valid Anagram Problem
# Input: t and s
#
# Anagram: Have all the character of a string in a different order

# create a table that

# aaagmnr
# |||||||

# aagmnr

def valid_anagram(s, t):
  # check to see if the strings are the same length
  if len(s) != len(t): # in python when have a structure passed in so when we call it it is 0(1)
    return False
  # sort the strings alphumerically
  s = sorted(s) # two loops
  t = sorted(t)
  # compare the strings
  return s == t # comparison is a loop

'''
Prompt:
Minimum Characters required to make a String Palindromic
You are given a string. The only operation allowed is to insert characters in the beginning of the string. Return the number of characters that are needed to be inserted to make the string a palindrome string

Examples:
Input: BCABC
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

# import copy

# def minimumCharacters(str_1): 'ABC'
#   # we have are string
#   # make copy of input string
#   input_str = copy.deepcopy(str_1)
#   input_len = len(input_str) #3
#   reverse_input = input_str[::-1] # 'CBA'
#   # keep track of count
#   count = -1
#   # keep track of index going backwards
#   # loop chars in string
#   for char_index in range(1, input_len + 1): # 4
#     # add what is last to the front
#     last_index = -char_index # -1
#     print(f"LAST CHAR: {str_1[last_index]}")
#     str_1 = str_1[last_index] + str_1
#     print(f"NEW STRING: {str_1}")
#     count += 1
#     # check slice string is same as copy or the same as reverse copy
#     if str_1[:input_len] == input_str or str_1[:input_len] == reverse_input:
#       return count


# print(minimumCharacters('ABC'))

def minimumCharacters2(str_1): #'ABC'
  # base case -- check if input is palindrome
  if isPalindrome2(str_1) == 1:
    return 0 
  insertions = 0 # 1
  new_string = str_1
  end_index = -1
  num_chars = len(str_1)
  
  while end_index >= -(num_chars):  # 'ABC'
    # Add the end to the front
    end_char = str_1[end_index:] # 'C'
    end_char = end_char[::-1]
    # increment counter
    insertions += 1
    # check if it is palindrome
    if isPalindrome2(end_char + new_string):
      break
    # new_string = end_char + new_string  # 'C + ABC =  CABC'
    print(new_string)
    end_index += -1
    print('End_index', end_index)
  return insertions

# print(minimumCharacters2('ABC'))

# Cleanier


def minimumCharacters3(str_1):  # 'ABC'
  # base case -- check if input is palindrome
  if isPalindrome3(str_1) == 1:
    return 0
  insertions = 0  # 1
  end_index = -1
  num_chars = len(str_1)

  while end_index >= -(num_chars):  
    # Get the end of the string and reverse it
    end_char = str_1[end_index:] 
    end_char = end_char[::-1]
    # increment counter
    insertions += 1
    # Add the end to the front and check if it is palindrome
    if isPalindrome3(end_char + str_1):
      break
    # Not palindrome increment index - to check more characters
    end_index += -1
  return insertions


# print(minimumCharacters3('ABC'))

# Solution Idea Inspirated by Geeks for Geeks https://www.geeksforgeeks.org/minimum-characters-added-front-make-string-palindrome/

def ispalindrome(A):  # ‘ABCBA’
  print("A", A)
  # declare forward and backward indexes
  i = 0  # 1 # 2
  j = 1 - 1  # -2 # -3
  while i <= j:
    print("J", j)
    print("I", i)
    print(f"Comparison: A[i] != A[j] -> {A[i] != A[j]}")
    # compare the beginning and end
    if A[i] != A[j]:
      return False
    # check next two characters
    i += 1
    j -= 1
    
  return True

def minimumCharacters4(string):
  cnt = 0  # 1 # 2
  while len(string) > 0:
    print("iteration")
    #  check if the string is a palindrome
    if ispalindrome(string) == True:
      break
    # if it is not increment a counter
    cnt += 1
    # and take off the last character
    string = string[:-1]
  # return counter
  return cnt

# print(minimumCharacters4('babb'))


def strStr(haystack, needle):
  '''
  Given a string determine if the given substring is found. 
  If it is return the index of where it is first found, if the substring is not found in the string return -1.
  Additionally, if the string is empty return 0.
  '''
  if needle == "":
    return 0
  if len(needle) == 1:
    mainSection = len(haystack)
  else:
    mainSection = len(haystack) - len(needle)+1
  # loop str
  for index in range(mainSection):  
    # expand window to len of sub string
    window = haystack[index:index+len(needle)] 
    # compare
    if window == needle:
      return index
  return -1


haystack1 = "hello"
needle1 = "ll" # 2
haystack2 = "xxxxxxxxy"
needle2 = "y" # 8
haystack3 = "thunderdome"
needle3 = "dome" # 7

# print(strStr(haystack3, needle3))


'''
Prompt:
Implement atoi which converts a string to an integer.

# [x] Step 1
The function first discards as many whitespace characters as necessary until the first non-whitespace character is found.

# [x] Step 2
Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

# [x] Step 3 - after the characters that are  digits are found, the first character you see that is not a digit stop checking and return the number 
The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

# [x] Step 4 - Base case empty, all letters, whitespace, not numbers return Zero. Additionally if the first thing seen is not a integer do not perform conversion exit
If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned.

Note:
# Step 5 - Now that you know you have all integers check to make sure it is within the 32 bit range, if it is output that number if it isn't output the INT_MIN to check take of the negative value. Use this `'{:032b}'.format(100)` to see the binary representation of the number if the len of the reprsentation is greater than 32 then it is not binary. If is 32 bit or less output the number however if it is not check if the first character is a negative sign if so output -2 ** 31 otherwise 2 ** 31.
Only the space character ' ' is considered as whitespace character.
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. If the numerical value is out of the range of representable values, INT_MAX (231 − 1) or INT_MIN (−231) is returned.

Example 1:
Input: "42"
Output: 42

Example 2:
Input: "   -42"
Output: -42
Explanation: The first non-whitespace character is '-', which is the minus sign.
             Then take as many numerical digits as possible, which gets 42.

Example 3:
Input: "4193 with words"
Output: 4193
Explanation: Conversion stops at digit '3' as the next character is not a numerical digit.
Example 4:

Input: "words and 987"
Output: 0
Explanation: The first non-whitespace character is 'w', which is not a numerical
             digit or a +/- sign. Therefore no valid conversion could be performed.
Example 5:

Input: "-91283472332"
Output: -2147483648
Explanation: The number "-91283472332" is out of the range of a 32-bit signed integer.
             Thefore INT_MIN (−231) is returned.
'''
# check if the value is a number using try and catch. If you try to make the number an integer and you don't get an error output true. However, you do get a value error output false
def is_number(char):
  '''Return True if the char is a valid number or False otherwise.'''
  try:
    int(char)
    return True
  except ValueError:
    return False


def atoi(a):
  '''Converts a string into an integar'''
  # remove whitespace at the start and end of the string
  a = a.strip()
  # Base case - If no valid conversion could be performed, a zero value is returned.
  if a == '':
    return 0
  result = '' 
  for char in a:
    # takes an optional initial plus or minus sign
    if a.index(char) == 0:
      if char == '-' or char == '+':
        result += char
        continue
      # If the first non-whitespace char in str is not a valid integral number no valid conversion can be performed
      elif is_number(a[0]) == False:
        return 0
    # take as as many numerical digits as possible, and interprets them as a numerical value
    if is_number(char):
      result = int(str(result) + str(char))
  # Check if the result is within the 32 bit range
  binary_representation = '{:032b}'.format(result)
  if len(binary_representation) > 32:
    if result[0] == '+' or result[0] == '-':


  return result


  Step 5 - Now that you know you have all integers check to make sure it is within the 32 bit range, if it is output that number if it isn't output the INT_MIN to check take of the negative value. Use this `'{:032b}'.format(100)` to see the binary representation of the number if the len of the reprsentation is greater than 32 then it is not binary. If is 32 bit or less output the number however if it is not check if the first character is a negative sign if so output -2 ** 31 otherwise 2 ** 31.
  Only the space character ' ' is considered as whitespace character.
  Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. If the numerical value is out of the range of representable values, INT_MAX(231 − 1) or INT_MIN(−231) is returned.


  # print(a)
a = "-91283472332"
print(atoi(a))

# Question on Leetcode: https://leetcode.com/explore/featured/card/top-interview-questions-easy/127/strings/884/
# Question on Canva: https://canvas.instructure.com/courses/1578976/assignments/11588243?module_item_id=23926299



'''
Prompt:
You are given an array A consisting of strings made up of the letters ‘a’ and ‘b’ only. 
Each string goes through a number of operations, where:
1.	At time 1, you circularly rotate each string by 1 letter.
2.	At time 2, you circularly rotate the new rotated strings by 2 letters.
3.	At time 3, you circularly rotate the new rotated strings by 3 letters.
4.	At time i, you circularly rotate the new rotated strings by i % length(string) letters.

Eg: String is "abaa"

1.	At time 1, string is "baaa", as 1 letter is circularly rotated to the back
2.	At time 2, string is "aaba", as 2 letters of the string "baaa" is circularly rotated to the back
3.	At time 3, string is "aaab", as 3 letters of the string "aaba" is circularly rotated to the back
4.	At time 4, string is again "aaab", as 4 letters of the string "aaab" is circularly rotated to the back
5.	At time 5, string is "aaba", as 1 letters of the string "aaab" is circularly rotated to the back

After some units of time, a string becomes equal to it’s original self. 
Once a string becomes equal to itself, it’s letters start to rotate from the first letter again (process resets). So, if a string takes t time to get back to the original, at time t+1 one letter will be rotated and the string will be it’s original self at 2t time. 
You have to find the minimum time, where maximum number of strings are equal to their original self. 

As this time can be very large, give the answer, modulo 10^9 +7.

Note: Your solution will run on multiple test cases so do clear global variables after using them.


Input:
A: Array of strings.

Output:
Minimum time, where maximum number of strings are equal to their original self.

Constraints:
1 <= size(A) <= 10^5
1 <= size of each string in A <= 10^5
Each string consists of only characters 'a' and 'b'
Summation of length of all strings <= 10^7

Example:

Input
A: [a,ababa,ab]

Output
4

String 'a' is it's original self at time 1, 2, 3 and 4.
String 'ababa' is it's original self only at time 4. (ababa => babaa => baaba => babaa => ababa)
String 'ab' is it's original self at time 3 and 4. (ab => ba => ba => ab => ab)

Hence, 3 strings are their original self at time 4.
'''
A = ['a','b']
# Understand
# Match
# Plan
# Implemnet
# Review
# Evalute
# Minimum time where the maximum number of strings are equal to their original self
# always a or b characters
# "abaa" - each string by 1 letter => "baaa"
# ""

