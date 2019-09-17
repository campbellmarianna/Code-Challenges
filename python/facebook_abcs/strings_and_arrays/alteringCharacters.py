'''
Prompt:
You are given a string containing characters  and  only. Your task is to change it into a string such that there are no matching adjacent characters. To do this, you are allowed to delete zero or more characters in the string.

Your task is to find the minimum number of required deletions.

For example, given the string , remove an  at positions  and  to make  in  deletions.

Function Description
Complete the alternatingCharacters function in the editor below. It must return an integer representing the minimum number of deletions to make the alternating string.

alternatingCharacters has the following parameter(s):

s: a string

Input Format
The first line contains an integer , the number of queries.
The next  lines each contain a string .

Constraints
Each string  will consist only of characters  A and B

Output Format
For each query, print the minimum number of deletions required on a new line.

Sample Input
5
AAAA
BBBBB
ABABABAB
BABABA
AAABBB

Sample Output
3
4
0
0
4

Explanation
The characters marked red are the ones that can be deleted so that the string doesn't have matching consecutive characters.

'''
# Key action: Return the minimum number of deletions to make the alternating string
# Input string: s
# Output: int : Minimum number of deletions

# Examples:
# Input: AAAA
# Output: 3

# check if the first character (A) matches the second character (A)? yes
# delete the second character 
# increment a deletion counter by 1

# Psudeocode
# loop through the sequence of A's and B's  # [A, B]
#   check if the current character(A) and the character after it match
#     delete the current character
#     increment a deletion counter by 1 # 1
#     if the len of the string is 1 
#       return the deletion counter
#   return the deletion counter

# Time complexity: 0(n), 
# Space Complexity: 0(n) Create list


def alternatingCharacters(s):
  '''Return the minimum number of deletions to make an alternating string'''
  s_list = list(s)
  del_count = 0  
  # check if all characters are the same                                  Check all characters code source (1)
  if all(charc == s_list[0] for charc in s_list):
        return len(s_list) - 1
  i = 0 
  while len(s_list) > 2 and i != len(s_list) - 1:
    if s_list[i] == s_list[i+1]:
        s_list.pop(i)
        del_count += 1
        if len(s_list) == 1:
            break
    else:  # Continue to the next iteration
        i += 1
  return del_count

# (1) https: // stackoverflow.com/questions/3787908/python-determine-if-all-items-of-a-list-are-the-same-item

# print(alternatingCharacters('AAABBB'))

# Psudeocode
# loop through the sequence of A's and B's not len if the arr minus 2  # [B, A, B, A, B, A]
#   check if the current character(A) and the character after it match
#     increment a deletion counter by 1 # 1, 2, 3, 4, 5
# check if the deletion counter is the len of the array
  # return the len of the array minus 1
# return the deletion counter

## Another way to solve it 
def alternatingCharacters2(s):
  s_list = list(s)
  del_count = 0
  for i in range(0, len(s_list) - 1):
    if s_list[i] == s_list[i + 1]:
      del_count += 1
  if del_count == len(s_list):
    return len(s_list) - 1
  else:
    return del_count

# Time complexity: 0(n),
# Space Complexity: 0(n) Create list

print(alternatingCharacters2('AAAA'))
