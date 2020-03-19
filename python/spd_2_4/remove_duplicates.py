'''
Prompt:
Array Problem
Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Example 1:

Given nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.

It doesn't matter what you leave beyond the returned length.
Example 2:

Given nums = [0,0,1,1,1,2,2,3,3,4],

Your function should return length = 5, with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively.

It doesn't matter what values are set beyond the returned length.
Clarification:

Confused why the returned value is an integer but your answer is an array?

Note that the input array is passed in by reference, which means modification to the input array will be known to the caller as well.

Internally you can think of this:

// nums is passed in by reference. (i.e., without making a copy)
int len = removeDuplicates(nums);

// any modification to nums in your function would be known by the caller.
// using the length returned by your function, it prints the first len elements.
for (int i = 0; i < len; i++) {
    print(nums[i]);
}
'''
def remove_duplicates(arr):
    '''
    Remove duplicate values in given array and return updated length of array
    '''
    if len(arr) == 1:
        return 1
    if len(arr) == 0:
        return 0
    dups = 0
    i = 0
    j = 1
    initial_len = len(arr)
    # at least 2 items in given arr
    while i <= len(arr)-2 and j <= len(arr)-1:
        if arr[i] == arr[j]:
            dups += 1
            arr.pop(j)
        else:
            i += 1
            j += 1
    return initial_len - dups

if __name__ == '__main__':
    arr = [1, 1, 2] # => 2
    # arr = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]  # => 5
    print(remove_duplicates(arr))

## Another way someone solved the problem on Leetcode with higher efficiency

def removeDuplicates(nums) -> int:
    '''
    Note: After reviewing this code solution, one found that all the dupplicates are removed from the array, but positioned to the front of the array
    '''
	new_length = 0
	i = 0
    # iterate through given arr comparing current value to previous value
    while i < len(nums):
        # only increment new length when unique values are found
        if i == 0 or nums[i] != nums[i-1]:
            # moves the value forward (towards the left) in the array
	        nums[new_length] = nums[i]
	        new_length = new_length + 1
	    i = i + 1
    return new_length

arr = [1, 1, 2]  # => 2
# arr = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]  # => 5
print(removeDuplicates(arr))
