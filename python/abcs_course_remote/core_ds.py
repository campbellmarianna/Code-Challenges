'''
Key Topics:
-Strings and Arrays
- Trees and Graphs
- Recursion and DP

Steps to know the key topics
1. Implement Data Structure
2. Implement common methods of the data structure
3. Solve or review (use steps in notebook) a compound algorithm (solving a problem using the primary data structure with another)
'''

#### Strings and Arrays
# 1. Implement Data Structure
my_str = 'marianna'
arr = []

# 2. Implement common methods of the data structure
# len(str)  #1
str() 
my_str2 = my_str[0:4] # slicing # O(c) for the number of characters copied

print(my_str.count('a'))

len(arr) # O(1)
arr.append('give') # O(1)
arr.index('give') # O(n) for the number of indexs it take to get to the one that matches the index in python it is O(1)

# 3. Solve or review(use steps in notebook) a compound algorithm(solving a problem using the primary data structure with another)
# Reverse a string https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/879/
9 -7
'''
Prompt: 
Write a function that reverses a string. The input string is given as an array of characters char[].

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

You may assume all the characters consist of printable ascii characters.

Example 1:

Input: ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:

Input: ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
'''
# input: list of strings
# output: return nothing modify list
# iterator front to back, back to front and switch items in the list


def reverseString(a):  # ["h","e","l","l","o"]
    # create i 3 and j 1
    i, j = 0, len(a) - 1
    while i < j:
        a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1
    return a

print(reverseString(["h", "e", "l", "l", "o"]))

#### Trees and Graphs

