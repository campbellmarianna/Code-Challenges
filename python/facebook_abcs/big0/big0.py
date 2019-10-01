'''
Prompt:
Compute Big O - I
Find the runtime of this function, where A is an array of integers, and n is the size of array A.

int foo(int A[], int n) {
  int j = 0;
  for(int i = 0; i < n; ++i) {
    while(j < n && A[i] < A[j]) {
      j++;
    }
  }
  return j;
}
In Python:

def foo(A, n):
  j = 0
  for i in range(0, n):
    while(j < n and A[i] < A[j]):
      j += 1
  return j

Input Format
Elements of the array each separated from the other by space, like so:
5 4 3 2 7 8

Constraints
None

Output Format
One of the following
O(log n)
O(n)
O(n log n)
O(n^2)
O(n^3)
O(2^n)
O(n^n)
'''

# I: [2, 3, 1, 4], 4
# O: 2

def foo(A, n):
  j = 0 # 1, 2
  for i in range(0, n): # 0, 1, 2, 3
        # 0 < 4 and 2 < 2
        # 0 < 4 and 3 < 2
        # 0 < 4 and 1 < 2 (True!)
        # 2 < 4 and 4 < 1
    while(j < n and A[i] < A[j]): # 1 < 4 and 1 < 3 (True!) # 2 < 4 and 1 < 1
      print(f"This is what was found true {j} < {n} and {A[i]} < {A[j]} iterator: {i}")
      j += 1
  return j # 2

# Time Complexity: 0(n)

# - Visit Python Tutor 
# - Try multiple inputs and loop for pattern

# print(foo([2, 3, 1, 4], 4))

# Fibonacci Sequence Problem
# int Fibonacci(int number) {
#     if (number <= 1) return number
#     return Fibonacci(number - 2) + Fibonacci(number - 1)
# }

def fibonacci(number):
  if number <= 1:
    return number
  return Fibonacci(number - 2) + Fibonacci(number - 1)

'''
Compute Big O - V
Find the runtime of this function, where n is an integer.

int quux(int n) {
  int a = 0;
  int b = n;
  int c;
  while (b - a > 0) {
    c = (a + b) / 2;
    if (c > rand()*n) {
      a = c;
    } else {
      b = c;
    }
  }
  return c;
}
In Python:

def quux(n):
  a = 0
  b = n
  while (b - a > 0):
    c = (a + b) / 2
    if (c > rand()*n):
      a = c
    else:
      b = c
  return c

Input Format
int n = 10;

Constraints
None

Output Format
One of the following
O(log n)
O(n)
O(n log n)
O(n^2)
O(n^3)
O(2^n)
O(n^n)
'''

# I: 10
# O: 
import random

def quux(n): # 10
  a = 0 # 
  b = n # 10, 5, 2.5, 1.25, 0.625, 0.3125, 0.15625
       # 10-0 > 0
       # 5 - 0 > 0
       # 2.5 - 0 > 0
       # 1.25 - 0 > 0 
       # 0.625 - 0 > 0
       # 0.3125 - 0 > 0
       # 0.15625 - 0 > 0
  while (b - a > 0):
    c = (a + b) / 2 
  # 5 = (0 + 10) /2
  # 2.5 = (0 + 5) / 2
  # 1.25 = (0 + 2.5) / 2
  # 0.625 = (0 + 1.25) /2
  # 0.3125 = (0 + 0.625) /2
  # 0.15625 = (0 + 0.3125) /2
  # 0 = (0 + 0.15625) /0.078125

    # 5 > 5*5
    # 2.5 > 2*10
    # 1.25 > 6*10
    # 0.625 > 8*10
    # 0.3125 > 9*10
    # 0.15625 > 3*10
    if (c > random.randint(0,n)*n): # 5, 2, 6, 8, 9, 3, 1
      a = c
    else:
      b = c
  return c

print(quux(10))

# Time Complexity: 0(log n)
# Line of code that causes our execution time to grow is 137 where be is being reduced by have each time


def bar(n):
  count = 0
  i = n
  while i > 0:
    for j in range(0, i): [0, 1, 2, 3, 4, 5, 6, 7, ..]
      count += 1
    i /= 2
  return count

# O(log n)* n