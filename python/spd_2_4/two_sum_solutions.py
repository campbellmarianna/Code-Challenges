'''
Two Sum Problem: 
Given an array a of n numbers and a target value t, find two numbers whose sum is t.
Example: a=[5, 3, 6, 8, 2, 4, 7], t=10  =>  [3, 7] or [6, 4] or [8, 2]

There are multiple ways to solve Two Sum.
What is described below:
- solution ideas
- code implementations
'''
# Solution Idea #1 
    # - create a set of all items, get number from set subtract from target and see if the complement is in the set if it is return those two numbers in a list as the result
def two_sum1(a, t):
    result = []
    seen = set() # {5, 3, 6, 8, 2, 4, 7}
    for num in a:
        seen.add(num)
    for num in seen:
        complement = t - num 
        if complement == num:
            continue
        if complement in seen:
            result.append(num)
            result.append(complement)
            return result

if __name__ == '__main__':
    a = [5, 3, 6, 8, 2, 4, 7]
    t = 10
    print(two_sum1(a, t))

# Solution Idea #3
    # - sort w/2 pointers front and back

