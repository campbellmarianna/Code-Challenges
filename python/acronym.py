# Convert a phrase to its acronym
# Input: "Portable Network Graphics"
# Output: PNG
# Refactor Plan
    # use regular expressions from re package
    # find all words using split or findall methods
    # then adding first letters of those
# Processing:
import re
def abbreviate(words):
    acronym = []
    charc_location = 0
    first_char = words[0]
    acronym.append(sanitize(first_char))
    charc_location += 1
    words_list = words.split()
    for word in words_list:
        charc_location_after_space = 0
        if words[i] == ' ' or words[i] == '-' or words[i] == '_':
            charc_location_after_space = i + 1
            charc_after_the_space = words[charc_location_after_space]
            if charc_after_the_space.isalpha(): # check if charc is a letter
                acronym.append(sanitize(charc_after_the_space))

    return "".join(acronym)

def sanitize(charc):
    clean_charc = charc.upper()
    return clean_charc

print(abbreviate("pin apple tree"))
