"""
Given two strings check if both string are anagram.
["Car","arC"] -> True
["rat", "art"] -> True
["rat", "ar"] -> False
"""

# Given two strings return True if the characters and the amount of characters
# are the same and return False if the amount and actual characters are not the
# same.

# input: 2 string, aphlabetic charc
# ouput: boolean
# capples included

# Test Input
#"tea", "ate" -> True
#"dog", "cat" -> False
# ->t , ->a
# Brainstorm Solutions
# base case: string len same



def check_anagram(string_1, string_2):
    """Return True or False based on if the strings are anagrams or not."""
    # base case
    if len(string_1) != len(string_2):
        return False
    # create set that holds second string
    charcter_holder = set()
    for charc in string_2:
        charcter_holder.add(charc)
    charc_match = 0
    # check if each charc in first string is in set
    for charc in string_1:
        if charc in charcter_holder:
            charc_match += 1
    if len(string_2) == charc_match:
        return True
    else:
        return False



print(check_anagram("rat","art"))
