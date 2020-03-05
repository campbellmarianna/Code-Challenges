# Given an unsorted array of integers, find a pair with the given sum in it.
# Example:
# Arr = [8,7,2,5,3,1], sum = 10
# Arr = [8,7,4,5,5,3,1], sum = 10
# Arr = [12,7,-2,5,5,3,1], sum = 10
# Arr = [-8,7,10,5,5,3,1], sum = 2
# Output:
# Pair found at index 0 and 2 (8+2)
# Or
# Pair found at index 1 and 4 (7+3)

#Iteration 1
# All positives
# No values in array return None
# No duplicates

#Iteration 2
# There are duplicates

#Iteration 3
# Negative numbers are in the array


# Loop arr and find complement
# Time Complexity: 0(n)
# Space: 0(n)

# create set (empty)
# Loop arr
# calculate complement
# check if complement in set
# return a list of curr num and complement
# otherwise add complement to set

def two_sum(arr, t):
    if len(arr) == 0:
        return None
    # create set
    seen = set()
    # Loop arr
    for curr_num in arr:  # 8
        # calculate complement
        comp = t - curr_num  # 2
        # find complement
        if comp in seen:
            # return a list of curr num and complement
            return [curr_num, comp]
        else:
             seen.add(curr_num)
    return None


# print(two_sum([8,7,2,5,3,1], 10))
# print(two_sum([8,7,4,5,5,3,1], 10)) # handles duplicates
print(two_sum([12, 7, -2, 5, 5, 3, 1], 10))  # handles negative int

# - Evaluate edge cases
'''
Four Sum Problem
input: [7, 6, 4, -1, 1, 2], 16
output: [[7, 6, 4, -1], [7, 6, 1, 2]]
'''
# Solution Ideas
# - four for loops
# - sliding window

# loop to find complement pair
    # from range 1 to len -1 i
        # range i + 1 to len j
        #currSum = arr[i] + arr[j]
        # diff = target - current
        # check if diff in hash
        # seen[diff] += val_list = {3: [[4,-1]]}

# f = [7, 6] => 13
# s = [4, -1] => 3
# x = 13
# y = 3
#hash =
# {
#     13: [[7, 6]],
#     3: [[4, -1],[1, 2]]
#     10: [[6,4]]
#     0: [[-1, 1]]
# }

def fourNumberSum(array, targetSum):
    seen = {} 
    results_list = []
    result = []
    # fill in hashtable
    i = 0  # 2 
    j = 1  # 3 
    while i <= len(array) - 2 and j <= len(array) - 1:
        val_sum = array[i] + array[j]
        val_list = [[array[i], array[j]]]
        seen[val_sum] = val_list 
        diff = targetSum - val_sum 
        # handle duplication
        if diff == val_sum:
            continue
        if diff in seen:
            complement_vals = seen[diff]
            result.append(val_list[0][0])
            result.append(val_list[0][1])
            result.append(complement_vals[0][0])
            result.append(complement_vals[0][1])
            results_list.append(result)
            result = []

        i += 1
        j += 1

    return results_list

if __name__ == "__main__":
    arr = [7, 6, 4, -1, 1, 2]
    targetSum = 16
    print(fourNumberSum(arr, targetSum))
    


