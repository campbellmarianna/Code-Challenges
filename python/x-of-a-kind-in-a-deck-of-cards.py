"""
LeetCode Problem - In a deck of cards, each card has an integer written on it.

Return true if and only if you can choose X >= 2 such that it is possible to split the entire deck into 1 or more groups of cards, where:

Each group has exactly X cards.
All the cards in each group have the same integer.
Link to problem: https://leetcode.com/problems/x-of-a-kind-in-a-deck-of-cards/
Pair Programmed solution with erikbatista42
"""

# Restate Question: Given a collection of numbers and the duplicates are grouped
#together if the groups are not even we return false

# Tests Inputs
# [1,1,1,2,2,2,3,3]   -> False
# [1]                 -> False
# [1,1,5,5,6,6,8,8,1] -> False


# Solution Idea #1
# [1,1,2,2,5,5,7,7,2,2,3,3] -> True
# [[1,1],[2,2,2,2],[5,5],[7,7],[3,3]]
# Time Complexity: 0(n) + 0(n) = 2n = 0(n)

# Psuedocode
# sparate identical duplicates inside lists
# append them to a outer list
# check if each element in the outer list has has an even length
# if they all do return true if not return false

# State Assumptions:
# - No negatives
# - Not sorted

# Solution Idea #2
# put given array in histogram:
# -> 1: 2
#    2,: 2
#    5,: 2
#    7: 2
#    2,: 2
#    3: 3
# check if value for each key is even
# -> 1: 2 -> occurance are even return true  True
#    2: 2 -> True
#    5: 2 -> True
#    7: 2  -> True
#    2: 2 -> True
#    3: 3 if not even return -> False

def cards(arr):
    table = {}
    # make histogram
    for num in arr:
        table[num] = table.get(num, 0) + 1
    # check occurance are even
    for occurence in table.values():
        if occurence % 2 == 0:
            continue
        else:
            return False
    return True


test = cards([1,1,2,2,5,5,7,7,2,2,3,3,3])
print(test)
