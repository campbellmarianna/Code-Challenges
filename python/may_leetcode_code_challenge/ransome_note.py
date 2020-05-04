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
        ran_dict = dict()
        mag_dict = dict()
        for char in ransomNote:
            if char in ran_dict:
                ran_dict[char] += 1
            else:
                ran_dict[char] = 1
        for char in magazine:
            # print("char", char)
            if char in mag_dict:
                mag_dict[char] += 1
            else:
                mag_dict[char] = 1
        # loop ransome
        for char in ransomNote:
            # check if char in dict
            if char in mag_dict:
                if mag_dict[char] == 0:
                    return False
                else:
                    mag_dict[char] -= 1
            else:
                return False
        return True
