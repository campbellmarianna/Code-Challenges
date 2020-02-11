'''
Given two arrays a and b of numbers and a target value t, find a number from each array whose sum is closest to t.
Example: a=[9, 13, 1, 8, 12, 4, 0, 5],  b=[3, 17, 4, 14, 6],  t=20  =>  [13, 6] or [4, 17] or [5, 14]

a = [9, 13], b = [3, 17] t = 20 => [13, 3], [9, 17]
'''
# Given two arrays and a target, find a number in each array that has a sum closest to the target
# input: arr1 and arr2
# out a list of two nums that have a sum closest two the target
# a: 9 
# b: 3
# sum: 12
# a: 9
# b: 17
# sum: 26
# a: 9
# b: 4
# sum: 13
# a: 9
# b: 14
# sum: 23 * 3
# a: 9
# b: 6
# sum: 13

# a: 13
# b: 3
# sum: 16
# a: 13
# b: 17
# sum: 30
# a: 13
# b: 4
# sum: 17
# a: 13
# b: 14
# sum: 27
# a: 13
# b: 6
# sum: 19 * 1

# a: 1
# b: 3
# sum: 4
# a: 1
# b: 17
# sum: 18 * 2
# a: 1
# b: 4
# sum: 5
# a: 1
# b: 14
# sum: 15 * 5
# a: 1
# b: 6
# sum: 7

# a: 8
# b: 3
# sum: 11
# a: 8
# b: 17
# sum: 25
# a: 8
# b: 4
# sum: 12
# a: 8
# b: 14
# sum: 22 * 2
# a: 8
# b: 6
# sum: 14

# a: 12
# b: 3
# sum: 15
# a: 12
# b: 17
# sum: 29
# a: 12
# b: 4
# sum: 16
# a: 12
# b: 14
# sum: 26
# a: 12
# b: 6
# sum: 18

# a: 4
# b: 3
# sum: 7
# a: 4
# b: 17
# sum: 21 * 1
# a: 4
# b: 4
# sum: 8
# a: 4
# b: 14
# sum: 18
# a: 4
# b: 6
# sum: 10

# a: 0
# b: 3
# sum: 3
# a: 0
# b: 17
# sum: 17
# a: 0
# b: 4
# sum: 4
# a: 0
# b: 14
# sum: 14
# a: 0
# b: 6
# sum: 6

# a: 5
# b: 3
# sum: 8
# a: 5
# b: 17
# sum: 22 * 2
# a: 5
# b: 4
# sum: 9
# a: 5
# b: 14
# sum: 19 * 1
# a: 5
# b: 6
# sum: 11

# the numbers that have a sum with the lowerest difference is the winner
# histogram that stores the difference of the (target and sum)

# Plan
    # the gets the sum
        # - get the sum of arrs with the same length of two
    # the gets the difference of the sum and the target
        # get the sum of only two pairs
    # the returns the 2 numbers that have a sum with the lowest difference fromt the target
        # - find the first one

# Implement Plan Test 1
# first function returns this list of lists
# [[9, 3, 12]
# [9, 17, 26]
# [13, 3, 16]
# [13, 17, 30]]

# second function
# 20 - 12 = 8
# [9, 3, 12, 8]
# 20 - 26 = 6   # make sure get absolute
# [9, 17, 26, 6]
# 20-16 = 4
# [13, 3, 16, 4]
# 20-30 = 10
# [13, 17, 30, 10]

# third function return the two nums in a list that is closet the sum
# [[13, 3, 16, 4],
# [9, 17, 26, 6],
# [9, 3, 12, 8],
# [13, 17, 30, 10]]
# return [13, 3]


### Solution #1
def get_sums(a,b):
    '''
    Return a list of lists of the possible combinations of numbers of each list and their sums
    inner list = [a_item, b_item, sum]
    '''
    sums = []
    for a_num in a:
        for b_num in b:
            sum_list = []
            curr_sum = a_num + b_num
            sum_list.extend([a_num, b_num, curr_sum])
            sums.append(sum_list)
    return sums

def find_difference(numbers_and_sums, t):
    '''
    Return list of lists with the difference (sum - t) added to end of each inner list
    inner list = [a_item, b_item, sum, difference]
    '''
    for data_list in numbers_and_sums:
        sum_of_vals = data_list[2]
        diff = abs(t-sum_of_vals)
        data_list.append(diff)
    return numbers_and_sums


def num_closet_to_t(numbers_sums_diff):
    '''
    Return a list of two nums, one num from each input array that is closest to the target
    '''
    result = []
    numbers_sums_diff_sorted = sorted(
        numbers_sums_diff, key=lambda data: data[3])
    print(numbers_sums_diff_sorted)
    result.extend([numbers_sums_diff_sorted[0][0],
                   numbers_sums_diff_sorted[0][1]])
    return result

# Solution #2
# - sort first array (only), then loop over second array, calculate complement of number and binary search for closest value to comp. in first array


# sort first array
# a = [9, 13]
# loop over second array, calculate complement of number
# b = [3, 17]
# 9 + 3 = 12 # storing difference in BST
# 20 - 12 = 8
# 9 + 17 = 26
# 20 - 26 = 6 # make sure to use absolute because of this case
# 13 + 3 = 16
# 20 - 16 = 4
# 13 + 17 = 30
# 20 - 30 = 10 # make sure to use absolute because of this case


# loop first array and get 

# create the tree
# insert nodes into the tree
# search to find the node with the smallest value

# loop the list again find the complement and if it equals the smallest difference return the two nums from each array

# Solution Idea #3 - Find the list that with a bigger sum then with the bigger list find the item closest to the target then sort the second list and find the item closest to the complement return the two nums
# a = [9, 13, 1, 8, 12, 4, 0, 5]
# b = [3, 17, 4, 14, 6]
# t = 20

# [0, 1, 4, 5, 8, 9, 12, 13] # get highest value
# result = [13]
# complement = 20-13 = 7
# b = [3, 4, 6, 14, 17]
# result = [13, 6]

def binary_search_closest_item(arr, t):  # [0, 1, 4, 5, 8, 9, 12, 13] # 20
    '''
    Return the item closest to the given t using binary search

    This solution idea has a constrint of only find values that are closest to the target but only less than the target.
    '''
    midpoint = len(arr)//2 # 4
    end = len(arr) # 8
    i = midpoint # 7
    prev = 0 # 8, 9, 12
    closest_item = 0
    while i < end and i > 0:
        # keep track of the previous value
        if i != 0:
            prev = arr[i-1]
        
        if arr[i] < t:
            i += 1
        else:
            closest_item = prev
            break
        if i == len(arr)-1:
            closest_item = arr[i]
    return closest_item

def find_closest(arr1, arr2, t):
    result = []
    # figure out which list is bigger
    if sum(arr1) > sum(arr2):
        bigger_arr = arr1
        smaller_arr = arr2
    else:
        bigger_arr = arr2
        smaller_arr = arr1
    # find item closest to target
    item_closest_to_target = binary_search_closest_item(bigger_arr, t)
    result.append(item_closest_to_target)
    smaller_arr.sort()
    # calculate complement
    complement = t - item_closest_to_target
    # find item closest to complement
    item_closest_to_complement = binary_search_closest_item(smaller_arr, complement)
    result.append(item_closest_to_complement)
    return result

if __name__ == '__main__':
    # a = [9, 13]
    # b = [3, 17]
    a = [9, 13, 1, 8, 12, 4, 0, 5]
    b = [3, 17, 4, 14, 6]
    numbers_and_sums = get_sums(a, b)
    t = 20
    numbers_sums_diff = find_difference(numbers_and_sums, t)
    # print(num_closet_to_t(numbers_sums_diff))
    print(find_closest(a,b, t))
