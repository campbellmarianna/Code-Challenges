# Convert a phrase to its acronym
# Input: "Portable Network Graphics"
# Output: PNG
# Processing:
def abbreviate(words):
    acronym = []
    charc_location = 0
    first_char = words[0]
    acronym.append(first_char)
    charc_location += 1
    for i in range(1, len(words)):
        charc_location_after_space = 0
        if words[i] == ' ' or words[i] == '-' or words[i] == '_':
            charc_location_after_space = i + 1
            charc_after_the_space = words[charc_location_after_space]
            if charc_after_the_space.isalpha():
                acronym.append(sanitize(charc_after_the_space))

    return "".join(acronym)

def sanitize(charc):
    clean_charc = charc.upper()
    return clean_charc

print(abbreviate("Portable network Graphics")) # 9,17 counter = 2
