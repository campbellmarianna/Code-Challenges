'''
Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note.

Note:
You may assume that both strings contain only lowercase letters.

canConstruct("a", "b") -> false
canConstruct("aa", "ab") -> false
canConstruct("aa", "aab") -> true
'''
# Given two strings, a ransom note and letters from all the magazines return true of the ransome note is a substring of the letters in the magazines
# all lowercase input
# ransome note is all letters also
# only needs to appear once
# letters in the ransome note must be in the same order as in the other str
# empty ransome note => false

# check if ransome is in letters from magazine
# Time O(n), Space: 0(1)


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # check if ransome is in letters from magazine
        if ransomNote in magazine:
            return True
        return False
