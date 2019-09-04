"""
Leetcode Problem:
Given an array, rotate the array to the right by k steps, where k is non-negative.

Example 1:

Input: [1,2,3,4,5,6,7] and k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
"""
def rotate(nums, k):
    """
    Do not return anything, modify nums in-place instead. 
    Best case running time: 0(n) = O(k + n) k steps given and n 
    numbers in the given list as a result of inserting (takes 0(n)).
    """
    steps = k
    while steps != 0:
        temp = nums.pop()
        nums.insert(0, temp)
        steps -= 1


# Another solution
# def rotate2(nums, k):
#     temp = 0
#     previous = 0
#     for i in range(0, k - 1):
#         previous = nums[len(nums) - 1]
#         for j in range(0, len(nums) - 1):
#             temp = nums[j]
#             nums[j] = previous
#             previous = temp

print(rotate([1, 2, 3, 4, 5, 6, 7], 3))
