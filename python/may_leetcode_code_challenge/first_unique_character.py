# Return the first non-repeating character in a given string and return -1 if not found
# You may assume the string contain only lowercase letters.
# I: "ulop"
# O: "0"

# create dict {"char": [index, count]}
# check for char with count of 1 and return its index


class Solution:
    def firstUniqChar(self, s: str) -> int:
        # Create storage of relevant data that can accessed quickly - dict {"char": [index, count]}
        hist = dict()
        for i, c in enumerate(s):
            if c in hist:
                hist[c][1] += 1
            else:
                hist[c] = [i, 1]
        # Check for a unique character
        for c in s:
            if hist[c][1] == 1:
                return hist[c][0]
        return -1
