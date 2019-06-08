# LeetCode Problem: Given a 32-bit signed integer, reverse digits of an integer.
# Examples:
'''
Example 1:
Input: 123
Output: 321

Example 2:
Input: -123
Output: -321

Example 3:
Input: 120
Output: 21
'''
# Restate the problem
    # - Reverse the digits of an integar
# Ask clarifying questions
    # - Can I modify the input? Never modify input
    # - What is the output? The reversed number.
    # - Are their duplicates? There can be but in the examples I have given you no.

# State assumptions
    # - Cannot modify input
    # - There are negatives integers
    # - if 0 is the first digit don't show it
    # - The input is only integars with only negative symbols and digits
    # - No duplicates
# Think through process out loud
    # Brainstorm solutions ideas
        # ALWAYS
        # Check if given integer is in range  [−2^31,  2^31 − 1]
            # Check if given integar has a negative symbol in front of it if so append it to result
        # ---
        # Then for the length of the integer pop the digit off the front and append it to the back
        # ---
        # Put digits in a list use slicing to reverse the list
        # join the string and give it as output
    # Explain Rationale
        # I want to make sure I catch the negative symbol early so that it is in the output before I reverse the integer
        # ---
        # I want decrease time complexity by not having to loop through the digits or making that process faster by slicing

    # Discuss Tradeoffs
        # O(n) loop through each digit in the integer
            # Keep track of the item that is being deleted and append it to the end - low space complexity b/c we are only tracking one variable
        # ---
        # Highly utilizing built-in functions
        # Increase in space complexity for creating a list of the given integer
        # Time complexity is according to the number of characters in the slice
    # Suggest improvements
        # Using a dat structure to hold the reversed integer that produces zero time complexity

class Solution:
    def reverse(self, x: int) -> int:
        num_list = [num for num in str(x)]
        num_list = num_list[::-1]
        return int(''.join(num_list))
