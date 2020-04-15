'''
Given an array of characters, compress it in-place.

The length after compression must always be smaller than or equal to the original array.

Every element of the array should be a character (not int) of length 1.

After you are done modifying the input array in-place, return the new length of the array.

 
Follow up:
Could you solve it using only O(1) extra space?

 
Example 1:
# write = 6
# anchor = 4
# read = 6
# c = "c"
Input:
["a","a","b","b","c","c","c"]
["a","2","b","2","c","3","c"]
Output:
Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]

Explanation:
"aa" is replaced by "a2". "bb" is replaced by "b2". "ccc" is replaced by "c3".
 

Example 2:

Input:
["a"]

Output:
Return 1, and the first 1 characters of the input array should be: ["a"]

Explanation:
Nothing is replaced.
 

Example 3:

Input:
["a","b","b","b","b","b","b","b","b","b","b","b","b"]

Output:
Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].

Explanation:
Since the character "a" does not repeat, it is not compressed. "bbbbbbbbbbbb" is replaced by "b12".
Notice each digit has it's own entry in the array.
 

Note:

All characters have an ASCII value in [35, 126].
1 <= len(chars) <= 1000.
'''
# Given list of characters return the length of a compressed version of the list

# Details
# Implement soluiton in place
# the character and the number of occurances are side by side
# if it only appears once don't compress
# Each digit has it's own entry in the array # => ["a","b","1","2"]

# Soluton Ideas
# dictionary also used a list of tuples that will stay in order
# add characters and occurances to dictionary
# loop through list and dict
# find occurances value
# delete the occurances
# Big O Space: 0(u) for u characters in the given list
# Big O Time: 0(u) for u characters in the given list

# loop list
# look starting from next index
# check if curr character is seen

# Big O Space: 0(1)
# Big O Time: 0(n^2) for u characters in the given list


# Input: ["a","a","b","b","c","c","c"] => 
# Output: ["a", "2", "b", "2", "c", "3"]

# ["a"] = > 1
def compress1(chars) -> int: # ["a", "a", "b", "b", "c", "c", "c"]
    # simple Edge Case
    if len(chars) == 1:
        return 1
    # dictionary also used a list of tuples that will stay in order
    seen_dict = dict() # {"a": 2, "b":2, "c":3}
    # add characters and occurances to dictionary
    for char in chars:
        if char in seen_dict:
            seen_dict[char] += 1
        else: # new char
            seen_dict[char] = 1
    # loop through list and dict
    for i, char in enumerate(chars): # 0, 1, 2
        # ["a","b","c"]
        print("CHAR:", char) # a, b, c
        # find occurances value
        occur = seen_dict[char] - 1 # 3 - 1 = 2
        # deletions_boundary = occur - 1
        # delete the occurances
        for _ in range(0, occur): # [0,1,2]
            chars.pop(i+1)
        chars.insert(i+1, str(seen_dict[char]))
    return chars

# Another way to do it
# def compress(self, chars):
#     anchor = write = 0
#     for read, c in enumerate(chars):
#         if read + 1 == len(chars) or chars[read + 1] != c:
#             chars[write] = chars[anchor]
#             write += 1
#             # add the total occurances correctly to the given arr
#             if read > anchor: # when the read pointer is pasted the anchor we dispkay its occurances
#                 for digit in str(read - anchor + 1):
#                     chars[write] = digit
#                     write += 1
#             anchor = read + 1
#     return write

# we are going to use read or write pointers to know when we read or write to the array and an anchor pointer to hold the starting point for the contigous group of the same letters
# start with a loop
def compress(chars):
    anchor = write = 0
    for read, c in enumerate(chars):
        if read + 1 == len(chars) or chars[read + 1] != c:
            chars[write] = chars[anchor]
            write += 1
            if read > anchor:
                for digit in str(read - anchor + 1):
                    chars[write] = digit
                    write += 1
            anchor = read + 1
    return write

if __name__ == "__main__":
    print(compress(["a", "a", "b", "b", "c", "c", "c"])) # ["a", "2", "b", "2", "c", "3"]
    print(compress(["a"])) # 1
