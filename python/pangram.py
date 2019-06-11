"""Exercism Problem: Determine if a sentence is a pangram - a sentnece usng every letter
of the alphabet at least once"""

# Clarifying Quesitons
# Find if the input has all the letters of the alphabet.
# What is the return value?
# What is the return value if a pangram is not found?
# is there duplicate values?

# Assumptions
# - Return a boolean
# - False
# - There are duplicates

# Brainstorm Solutions
# First
    # If there aren't enough characters is match the alphabet or it is empty
    # return False
    # For every letter if the alphabet check if the letter is found in the given text
    # the first time it is found increment a counter by 1 and at the end of the
    # alpahabet if the counter is equal to the length of alphabet return true
# Second
    # we can sort (make string list) the input then compare if the sorted given input is the same as
    # as list of the input

# Explain Rationale
# - I want to loop through the aplhabet to make sure every character in the alphabet
# is found in the given text
# - I want to sort the given text so that the search of each character is faster - saving time.

# Discuss Tradeoffs
# - This is an increase in time complexity because were performing a double for loop
# It doesn't use any memory
# - This is a better solution because it decrease time complexity
# It increases space complexity to store the sorted text

# Suggest Improvement
# Make search faster by keeping track of position in string

import string
alpha_letters = string.ascii_lowercase

def is_pangram(sentence):
    char_found = 0
    if len(sentence) < 26 or sentence == '':
        return False
    # Lowercase all letters and remove spaces
    sentence = sentence.lower()
    sentence = sentence.replace(" ", "")
    # check if each character in the alphabet is found in the sentence
    for char in alpha_letters:
        if char in sentence:
            char_found += 1
    if char_found == 26:
        return True
    else:
        return False

if __name__ == '__main__':
    print(is_pangram('"Five quacking Zephyrs jolt my wax bed."'))
