'''
Prompt:
We consider two strings to be anagrams of each other if the first string's letters can be rearranged to form the second string. In other words, both strings must contain the same exact letters in the same exact frequency. For example, bacdc and dcbac are anagrams, but bacdc and dcbad are not.

Alice is taking a cryptography class and finding anagrams to be very useful. She decides on an encryption scheme involving two large strings where encryption is dependent on the minimum number of character deletions required to make the two strings anagrams. Can you help her find this number?

Given two strings,  and , that may not be of the same length, determine the minimum number of character deletions required to make  and  anagrams. Any characters can be deleted from either of the strings.

For example,  and . The only characters that match are the 's so we have to remove  from  and  from  for a total of  deletions.

Function Description

Complete the makingAnagrams function in the editor below. It should return an integer representing the minimum number of deletions needed to make the strings anagrams.

makingAnagrams has the following parameter(s):

s1: a string
s2: a string
Input Format

The first line contains a single string, .
The second line contains a single string, .

Constraints

It is guaranteed that  and  consist of lowercase English letters, ascii[a-z].
Output Format

Print a single integer denoting the minimum number of characters which must be deleted to make the two strings anagrams of each other.

Sample Input
cde
abc

Sample Output
4
Explanation

We delete the following characters from our two strings to turn them into anagrams of each other:

Remove d and e from cde to get c.
Remove a and b from abc to get c.
We had to delete  characters to make both strings anagrams.
'''
# Key action : Return the minimum number of of deletions to make the two strings anagrams of each other
# Input 2 strings
# Output int
# Are there any duplicate characters in a string?
# Input:
# cde
# abc

# Output:
# 4

# Psudeocode 1
# add everything in the first string to a set {c, d, e}
# Check if each character in the second string is in the set
  # increment a match counter by 1 # 1
# if not in there
  # add charc to set  # 1, 2
# Subtract the len of set by match  # 5 - 1 = 4
# Return the result

# Psudeocode 2
# add everything in the first string to a set {c, d, e}
# Check if each character in the second string is in the set
  # increment a match counter by 1 # 1
# if not in there
  # increment not found counter by 1 # 1, 2
# Subtract the len of set by match  # 5 - 1 = 4
# Return the result

# Space complextiy 0(s1 + s2)
# Time completiy: 0(n)

def makingAnagramsWithSameLenStr(s1, s2):
  # This works only if the length of s1 and s2 are the same 
  seen = set()
  # Add character in s1 to a set
  for char in s1:
    seen.add(char)
  match = 0
  # Check if there a matching characters in s1 and s2
  for char in s2:
    if char in seen:
      match += 1
    else:
      seen.add(char)
  return len(seen) - match


# put s1 and s2 in separate lists
# check if character in s1 is in s2
  # increment match # 1, 2, 3, 4. 5, 6, 7
# if not
  # increment not found s1 # 1, 2, 3, 4
# check if character in s2 is in s1
  # increment match # 1,
# if not
  # increment not found s1 #
# return not found s1 + not found s2


# Suggest Improvements
# Sort strings
# Binary Search

# More Psudeocode #3 [c, d, e] s2 = [a, b , c]
# if the char in the s1 is found in s2 remove it from string 2
# s2 take away is len(str2) originally minus match
# if the char in the s2 is found in s1 remove it from string 1
# s1 take away is len(str1) originally minus match
# return s1 take away plus s2 take away

# Solution Idea 4:
# Matchs: a 1, s 2, d 3, j 4, a 5, h 6, d 7
# Deletions: s1 (11 - 7) + s2 (13 - 7) = 4 + 6 = 10
# print(makingAnagrams('absdjkvuahd', # a 2 here
#                      'djfladfhiawas')) # here 3 times
# Solution Idea Psudeocode 4:
# check if a character a in s1 is found in s2? yes
# delete a from s1 and s2
# increment match by 1
# check if a character b in s1 is in s2? no
# continue to the next character
# return (s1_len - match ) + (s2_len - match)

# Solution Idea 5:
# Deletions = 10
# print(makingAnagrams('bkvu',  # a 2 here
#                      'flfiwa'))  # here 3 times
# Solution Idea Psudeocode 5:
# check if a character a in s1 is found in s2? yes
# delete a from s1 and s2
# increment match by 1 
# check if a character b in s1 is in s2? no
# continue to the next character
# return len(copyS1) + len(copys2) 
  
# Solution Idea 6:
# add string 1 and string to one giant string
# loop through get one character and its index
  # see in the rest of the string if it is in there 
# Not the best idea: because we have to figure out to do a nested string that is double the size to find a character

def makingAnagrams2(s1, s2):
  '''
  Return the minimum number of of deletions to make the two strings anagrams of each other
  '''
  s1_list = list(s1)
  s2_list = list(s2)
  len_str1 = len(s1_list)
  len_str2 = len(s2_list)  
  i = 0 
  match = 0  
  while i < len(s1_list) and i < len(s2_list): 
    char = s1_list[i] # 
    if char in s2_list: 
      # delete character from s1 and s2
      s1_list.remove(char)
      s2_list.remove(char)
      match += 1 
    else:
      i += 1
  return (len_str1 - match) + (len_str2 - match) 

print(makingAnagrams2('cde', 'abc'))
# Custom Input: absdjkvuahdakejfnfauhdsaavasdlkj, djfladfhiawasdkjvalskufhafablsdkashlahdfa
