"""
LeetCode Problem:
Given a pattern and a string str, find if str follows the same pattern.
Here follow means a full match, such that there is a bijection between a letter
in pattern and a non-empty word in str.
Problem Source: https://leetcode.com/problems/word-pattern/
Example:
Input: pattern = "abba", str = "dog cat cat dog"
Output: true
"""


def word_pattern(pattern, str):
    """Return true or false by finding if the string matches the pattern."""
    counter_p = 0
    counter_str = 0
    for char_1 in pattern:
        for char_2 in pattern:
            if char_1 == char_2:
                counter_p += 1
    for word_1 in str:
        for word_2 in str:
            if word_1 == word_2:
                counter_str += 1
    if counter_p == counter_str:
        return True
    return False


if __name__ == '__main__':
    print(word_pattern("abba", "pig cat pig cat"))
    print(word_pattern("aaaa", "aaaa"))
