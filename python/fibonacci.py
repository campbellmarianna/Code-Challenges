"""
Firecode Problem:
The Fibonacci Sequence is the series of numbers: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ... The next number is found by adding up the two numbers before it.
Write a recursive method fib(n) that returns the nth Fibonacci number. n is 0 indexed, which means that in the sequence 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ..., n == 0 should return 0 and n == 3 should return 2.
Assume n is less than 15.
Restate the problem: Given a number n find the associated fibonacci number.
Ask clarifying questions:
- If I'm given -7 or 16 what should the program return? Invalid Input
- What if the input is a string what should the program to return? The associated fibonacci number
State assumptions:
n > 15
n is an int
Brainstorm solutions (recursion and non-recursion):
#1
- Have the Fib sequence all the way to 15
- loop through the sequence till n is reached
- Time and Space Complexity: 0(n) and 0(n)
#2
- Recursion (Helpful resources below):
    - https://www.firecode.io/blog/5-problem-of-the-week
    - https://www.geeksforgeeks.org/program-for-nth-fibonacci-number/
    - Time and Space Complexity: 0(n) and 0(n)
Source to problem:
"""

def fib(n):                                                                           # Code Resource: https://www.geeksforgeeks.org/program-for-nth-fibonacci-number/
    # Taking 1st two fibonacci numbers as 0 and 1
    fibArray = [0, 1]

    while len(fibArray) < n + 1:
        fibArray.append(0)

    if n <= 1:
        return n
    else:
        if fibArray[n - 1] == 0:
            fibArray[n - 1] = fib(n - 1)

        if fibArray[n - 2] == 0:
            fibArray[n - 2] = fib(n - 2)

    fibArray[n] = fibArray[n - 2] + fibArray[n - 1]
    return fibArray[n]

print(fib(10))
