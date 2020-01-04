'''
Count the number of prime numbers less than a non-negative number, n.
'''
# Given positive number n return the range/group of numbers that are prime before reaching n
# Prime number - a number only divisible by 1 and itself
import sys
    # 5 = 5 * 1
# What is the type of the output? Int
# Input -> 4 Processing -> 2,3 Output -> 2
# Input -> 16 Processing -> 2,3,5,7,11,13 Output -> 6
# 0 is not prime
# 1 doesn't count


def isPrime(n):
    '''
    Return True if give number is prime and False if it is not prime
    '''
    for current_num in range(2, n):
        # check if the number is not prime
        if n % current_num == 0:
            return False
    return True

def countPrimes(n):
    '''
    Given positive number n return the range/group of numbers that are prime before reaching n
    '''
    num_of_primes = 0
    for num in range(2, n):
        print(num)
        if isPrime(num):
            num_of_primes += 1 
    return num_of_primes

# print(countPrimes(16))
            
######################################################## # Solution Submitted to InterviewBit
# Practice Problem #1
def fizzBuzz(A):                             
    output_list = []
    for curr_num in range(1, A + 1):
        if curr_num == 1:
            output_list.append(str(curr_num))
            continue
        if curr_num % 5  == 0 and curr_num % 3  == 0:
            output_list.append('FizzBuzz')
            continue
        if curr_num % 3 == 0:
            output_list.append('Fizz')
            continue
        if curr_num % 5 == 0:
            output_list.append('Buzz')
            continue
        output_list.append(str(curr_num))
    return output_list

# print(fizzBuzz(5))

################################################### # Repl.it
# Another Way to Solve FizzBuzz Problem
def fizzbuzz(n):                        
    for current_number in range(1, n+1):
        if current_number % 3 == 0 and current_number % 5 == 0:
            print("fizzbuzz")
        elif current_number % 3 == 0:
            print("fizz")
        elif current_number % 5 == 0:
            print("buzz")
        else:
            print(current_number)

# fizzbuzz(15)
# Psudocode
# for every number up to and including the Input
#     is that number divisible by 3?
#         print fizz
#     is that number divisible by 5?
#         print buzz
#     is that number divisible by 3 and 5?
#         print fizzbuzz

######################################################
# Practice Problem #2
'''
Given a column title as appears in an Excel sheet, return its corresponding column number.

Examples:
Input: A -> Output: 1

B -> 2

C -> 3

...

Z -> 26

AA -> 27

AB -> 28

CC -> 81

ABC -> 731
'''
# Given a column title return the associated column number.

# Return corresponding column number
# What is the input? Column Title
# What is the data type of input? string
# What is the format of the output? Column number
# What is the data type of the output?Int
# Make sure valid column_title => no numbers in it
# We can asume all column titles are valid

# sequence = [A, ... Z]
# A
# 0+1 = 1
# column number is 1
# B
# 1+1 = 2
# column number is 2
# C
# 2 + 1 = 3
# column number is 3
# Z
# 25 + 1 = 26
# column number is 4

# AA
# 0 + 1 = 1
# len(sequence) + 0 + 1 = 27
# column number is 27

# AB
# 0 + 1 = 1
# len(sequence) + 1 + 1 = 28

# AAA
# 0 + 1 = 1
# len(sequence) + 1 + 1 = 28
# 0 + 1 = 1
# 0 + 1 = 1
# create sequence of alphabet letters from A to Z
# Create function here given column title
# for character in column_title
#     for letter in alphabet
#         check if letter is the same as the character
#             Increment the column_number by the index of the letter plus 1
#             break
#         else:
#             go to next letter
# return the column number
# Time Complexity -> O(n^2)
# Space Complexity -> 0(n) for column number, 0(n) for alphabet list

## Faster Option - Psudeocode
# create sequence of key value pairs: keys being alphabet letters and values being order number in alphabet 
#     alphabet_dict = {}
#     loop through range of ascii letters a to z
#         access dict and set asciiletter(key) to value index

# Create function here given column title
    # check if the column title length to less than 2
    #     return result of getting column title(key) value plus 1
    # else
    #     create column_number # 
    #     Increment the column_number by:
    #         by the length of the column title minus one multiplied by the alphabet_dict length # 1 * 26 = 26
    #     for character in column_title
    #         Increment the column_number by value_index of character # 26 + 0 + 1 = 27
    #     return Increment column_number by 1 # 28

# Implementation
import string

def createAlphabetDict():
    '''
    Return a sequence of key value pairs: keys being alphabet letters and values being order number in alphabet
    '''
    ascii_letters = string.ascii_uppercase
    alphabet_dict = {}
    # loop through range of ascii letters A to Z
    for i in range (0, len(ascii_letters)):
        # access dict and set asciiletter(key) to value index
        alphabet_dict[ascii_letters[i]] = i
    return alphabet_dict

def excel_column_to_number(column):
    '''
    Given a column title return the associated column number.
    '''
    alphabet_dict = createAlphabetDict()
    if len(column) < 2:
        return alphabet_dict[column] + 1
    else:
        column_number = 0
        # Carry over the position value of going to another column - already went offer the first set of letters lets go through it again +26)
        lengthAlphabet = len(alphabet_dict) # 26
        multipleOfColumn = len(column) - 1 # 2 - 1 = 1
        column_number += lengthAlphabet ** multipleOfColumn
        for character in column:
            # Find the character in the alphabet_dict and increment the column_number by it value
            column_number += alphabet_dict[character] 
        column_number += 1
        return column_number

# print(excel_column_to_number('CC'))
'''
problem link: https://canvas.instructure.com/courses/1578976/assignments/11432599?module_item_id=23601324

Not passing all tests:
Traceback (most recent call last):
  File "/home/runner/unit_tests.py", line 52, in test_column_translate
    self.assertEquals(excel_column_to_number('CC'), 81)
AssertionError: 31 != 81
------------------------
Traceback(most recent call last):
  File "/home/runner/unit_tests.py", line 55, in test_three_digit_column
  self.assertEquals(excel_column_to_number('ABC'), 731)
AssertionError: 56 != 731
'''
# Solution Guidance Quiz:
def order_func_test():
  # n = ord('A')
  # print("\n")
  n = ord('H') - ord('A') + 1
  return n

# print(order_func_test())
# Considering the information I got from the quiz
# function definiton
# ord func A - ord func A + 1


# A -> 1
# 65 - 65 + 1 = 1

# B -> 2
# 66 - 65 + 1 = 2

# C -> 3
# 67 - 65 + 1 = 3

# Z -> 26
# 90 - 65 + 1 = 26

# AA -> 27
# 65 + 65 - 65 + 1 = 66

# def Number(C):
#   return ord(C) - ord('A') + 1;

# Column = "AD";

# x = Number(Column[0]) * 26; # 1 * 26 = 26
# y = Number(Column[1]); # 4
# n = x + y;
# print(n)

'''Understand, Match, Plan for Excel Column from canvas course'''
# What is the key action we are returning a number
# 27 
# 20 + 7

# 2389
# 2000 + 300 + 80 + 9

# BDF
# B - 2 * 26 ** 2 = 676 = 1352
# D - 4 * 26 ** 1 = 104
# F - 6 * 26 ** 0 = 6

def excel_column_to_number2(column):

  return ord(column) - 64 # translates individual characters into their ASCII values

# for every letter in the string and it's position within the string, starting with the right-most letter
  # convert the letter into a numerical value
  # multiply the letter's by 26 to the power of it's position (starting with the right-most)
  # add the value of the above value to the total

# print(excel_column_to_number2('A'))
# print(excel_column_to_number2('B'))
# print(excel_column_to_number2('C'))
# print(excel_column_to_number2('C'))
# print(excel_column_to_number2('ABC'))

# Solution after learning problem solving process and given psudeocode


def excel_column_to_number3(column):
  '''
  Given a column title return the associated column number.
  '''
  total = 0
  # for every letter in the string and it's position within the string, starting with the right-most letter
  for i, letter in enumerate(reversed(column)):
    # convert the letter into a numerical value
    num_value = ord(letter) - 64
    # multiply the letter's by 26 to the power of it's position (starting with the right-most)
    pos_value = num_value * 26 ** i
    # add the value of the above value to the total
    total += pos_value
  return total
# print(excel_column_to_number3('ABC'))

######################################################
# Practice Problem #3
'''
Last Factorial Digit
Given a non-negative number, N, return the last digit of the factorial of N.

The factorial of N, which is written as N!, is defined as the product of all of the integers from 1 to N.

Given 3 as N, the factorial is 1 x 2 x 3 = 6
Given 6 as N, the factorial is 1 x 2 x 3 x 4 x 5 x 6 = 720
Given 9 as N, the factorial is 1 x 2 x 3 x 4 x 5 x 6 x 7 x 8 x 9 = 362,880

As you can see, the number can grow to be quite large, quite quickly.

Write a function that will return only the last digit of N!, given N.
'''

# What is the key action? return
# What is the input and type? num: int
# What is the output? num : int

# 3 -> 6
# 1 * 1 = 1
# 1 * 2 = 2
# 2 * 3 = 6
# ------------


# 6 -> 720
# 1 * 1 = 1
# 1 * 2 = 2
# 2 * 3 = 6
# 6 * 4 = 24
# 24 * 5 = 120
# 120 * 6 = 720 

# 9 -> 362,880
# 1 * 1 = 1
# 1 * 2 = 2
# 2 * 3 = 6
# 6 * 4 = 24
# 24 * 5 = 120
# 120 * 6 = 720
# 720 * 7 = 5,040
# 5,040 * 8 = 40,320
# 40,320 * 9 = 362,880

# Psuedocode
# Create last digit variable to store product starting at 1
# Create a sequence from 1 to N (including N) and have the element in the sequence be num # [1,2, 3, 4]
#   Multiple the last digit by the num # 6
# After that return the last digit # 6


def last_factorial_digit(n):
  '''Return the last digit of factorial N'''
  product = 1
  for num in range(1, n + 1):
    product *= num
  # get the last digit of product
  last_digit = product % 10
  return last_digit

# for i in range(1, 50):
#   print(last_factorial_digit(i))
# numbers greater than a certain point return zero
# print(last_factorial_digit(5))

## Another way to solve it
# T = int(input()) # T = 6

# while T > 0:
#     T = T - 1 # 5

#     N = int(input()) # 

#     if N == 1 or N == 2 or N == 4:
#         # print output
#         continue

#     if N == 3:
#         # print output;
#         continue

    # print output for all other numbers;


# Kattis Specific changes:
# T = the number of test cases
# Input:
# 3 # first line of input contains a positive integer greater than 1 and less than 10 
# 1 # the next T lines contains a single positive integer N
# 2
# 3
# Output: 
# 1
# 2
# 6
# read the 

# for i in range(1, 50):
#   print(last_factorial_digit(i))

## Code
#-- Using functionality I did already
def last_factorial_digit2():
  T = int(input()) # T = 6

  while T > 0:
      T = T - 1 # 5

      N = int(input()) #

      print(last_factorial_digit(N))

# last_factorial_digit2()

# -- New idea (noticing a pattern in the data)
# for i in range(1, 10):
#   print(f"Number: {i}",last_factorial_digit(i))
# numbers greater than a certain point return zero
def last_factorial_digit3():
  T = int(input())

  while T > 0:
      T = T - 1 

      N = int(input()) #

      if N == 1 or N == 2 or N == 4:
          # print output
          print(N)
          continue

      elif N == 3:
          # print output;
          print(6)
          continue
      else:
        print(0)
    
# last_factorial_digit3()

## MATH Module Assessment
# I am sure I can solve problems involving numerical operators 
# I am sure I can solve problems involving numerical comparisons
"""
Given an integer, write a function to determine if it is a power of three.

Example 1:
Input: 27
Output: true

Example 2:
Input: 0
Output: false

Example 3:
Input: 9
Output: true

Example 4:
Input: 45
Output: false
"""
# key action: write a function to determine if a given integer is a power of three
# input -> int
# output -> boolean
# 27 -> true
# 1*1*1 = 1
# 2*2*2 = 8
# for i in range(1, 28):
#   print(f"{i}*{i}*{i}: {i*i*i}")
#   if i % 3 == 0:
#     print(f"Can be a power of three?? {i}")
# Ex:
# 36 -> true 
# 48 -> False
# create a function that takes in an integer num
#   check if given num is 0
#     return False
#   loop through 1 to given num with i as the iterator
#     multiply i by itself 3 teams
#     check if the product is equal to the given num
#       return True
#   return False
# Time Complexity: 0(n) n being given integar
# Space: 0(1)

# create a function that takes in an integer num
#   check if given num is 0
#     return False
#   check if the num is divisible by three
#       return True
#   return False

# Time: Constant
# Space: 0(1)

def power_of_three(n):
  if n == 0:
    return False
  elif n % 3 == 0:
    return True
  else:
    return False

# print(power_of_three(45))

def power_of_three3(n): 
  if n == 0:
    return False
  # numOfThree = 0
  if n == 3:
    return True
  if n % 3 == 0:
    return True
  for i in range(1, n + 1):
    numOfThree = i * i * i
    if numOfThree == n:
      return True
  return False


# print(power_of_three3(45))
# question how can 9 be a power of 3

'''
Understand A Way to Think and Solve the Problem (Uderstand, Match, Plan) using Leetcode Article https://leetcode.com/articles/power-of-three/
'''
# Pseudocode
# create func to taken in n 
# check if the n is 0 return false
# while n is divisible by 3
#   divide n by 3
# check if n is 1 then return True and if it is not return False

def power_of_three4(n):
  '''
  Return True if a given number is a power of three and False if is not a power of three.
  '''
  # 0 is not a power of 3
  if n == 0:
    return False

  while n % 3 == 0:
    n //= 3
  
  return n == 1
print(power_of_three4(9))

"""
Prompt:
You are in charge of a server that needs to run some submitted tasks on a first-come, first-served basis. Each day, you can dedicate the server to run these tasks for at most T minutes. Given the time each task takes, you want to know how many of them will be finished today.

Display (by printing) the number of tasks that can be completed in T minutes on a first-come, first-served basis.


Sample Input 1
6 180
45 30 55 20 80 20

Sample Output 1
4


Sample Input 2
10 60
20 7 10 8 10 27 2 3 10 5

Sample Output 2
5
"""
Key action? display
Input 
  - First line n:int, T: int
  - Second line one number (n) after another to symbolizing this list of how long each task will take
Output int (number of tasks that can be completed)
Can we manipulate passed in T? yes

# setup - put n's in list
# loop the task time list
  # deincrement the task 

# n = 6
# T = 180
# ns = 45 30 55 20 80 20
# T 180 - 45
# is that result positive? yes
#   increment task counter by 1 # 1
# otherwise return 0

# My progress ( I did this question very easily in the future :) and above /\ where I started months before. )
'''
Prompt:
You are in charge of a server that needs to run some submitted tasks on a first-come, first-served basis. Each day, you can dedicate the server to run these tasks for at most T minutes. Given the time each task takes, you want to know how many of them will be finished today.

Consider the following example:

Assume T = 180 and the tasks take 

45, 30, 55, 20, 80 and 20 minutes(in the order that they are submitted). Then, only four tasks can be completed. The first four tasks can be completed because they take 150 minutes, but not the first five, because they take 230 minutes which is greater than 180. Notice that although there is enough time to perform the sixth task(which takes 20 minutes) after completing the fourth task, you cannot do that because the fifth task is not done yet.


Input
The input consists of a two lines.

The first line contains two integers n and T.
1 ≤ n ≤ 50 is the number of tasks
1 ≤ T ≤ 500 is the total amount of execution time available.

The second line contains n positive integers, separated by spaces, smaller than 100, indicating how long each task takes in order they are submitted(the same order they must be evaluated in).
1 < n < 100 - the input looks like this:
n n n n n

Output
Display(by printing) the number of tasks that can be completed in T minutes on a first-come, first-served basis.


Sample Input 1
6 180
45 30 55 20 80 20

Can I do this task 180 >= 45? Yes
180 - 45
Task completed 1
Can I do anoter task 135 >= 30? Yes
130 - 35
Task completed 2
Can I do anoter task 105 >= 55? Yes
105 - 55
Task completed 3
Can I do anoter task 50 >= 20? Yes
50 - 20
Task completed 4
Can I do anoter task 30 >= 80? No
Completed tasks is 4

Sample Output 1
4


Sample Input 2
10 60
20 7 10 8 10 27 2 3 10 5 #5

Sample Output 2
5
'''


def server_time_check(task_config, task_times):
    '''
    Return the estimated number of completed tasks given a list of 
    task times each task will take and the total execution time the server has available.
    '''
    n, T = task_config.split()
    T = int(T)
    n = int(n)
    t_times = []
    t_times = task_times.split()
    tasks_completed_counter = 0
    # Evaluate each task time to see if it can be excuted by the server
    for task_time in t_times:
        task_time = int(task_time)
        # Check if there is enough execution time to do the task
        if T >= task_time:
            T -= task_time
            tasks_completed_counter += 1
        else:
            break
    print(tasks_completed_counter)
