'''
Prompt:
String Problem
Write a function to check whether a given string is "smashable", meaning that it’s a word in a predefined dictionary and can be reduced to a single character, one character at a time, and every intermediate word during the reduction is also in the dictionary of words. (Assume you have a file or list of valid dictionary words, like /usr/share/dict/words)
Example: Given the word SPRINT as input, it should return the following:
SPRINT → PRINT → PINT → PIT → IT → I
'''
word_list = ["sprint", "print", "pint", "pit", "it",
             "i"]  # sample list of valid dictionary words
import copy

# def find_closest(str_word):
#     "Return a word from the dictionary that is one character smaller than the given word and match all except for one of the characters in the given list"
#     copy_new_word = copy.deepcopy(str_word)
#     for i, char in enumerate(str_word):
#         new_word = copy_new_word.pop(i)
#         if new_word in word_list:
#             return new_word
#         else:
#             copy_new_word.insert(i, char)
#     return None

## Iteration #2 
def find_closest(str_word):
    "Return a word from the dictionary that is one character smaller than the given word and match all except for one of the characters in the given list"
    new_word_list = list(str_word)
    for i, char in enumerate(str_word):
    	    new_word_list.pop(i)
    	    new_word = "".join(new_word_list)
    if new_word in word_list:
        return new_word
    else:
    	new_word_list.insert(i, char)
    return None

def is_smashable(str_input):
    new_word = str_input
    while len(new_word) > 1:
        closest_word = find_closest(new_word)
        if closest_word != None:
            new_word = closest_word
            print(new_word)
        else:
            return False
    return new_word

if __name__ == "__main__":
    given_str = "sprint"
    is_smashable(given_str)

# What went well
# - Coming up with a solution
# - Asking clarifying questions
# - writing psudeocode
# - writing comments

# What can be improved
# - coming up with a solution that works and your confident in
# - coming up with your own testcase
# - coming upi with multiple solutions
# - identifying edge cases