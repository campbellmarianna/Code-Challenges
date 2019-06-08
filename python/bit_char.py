# Restate Question
# Given a string of one bit characters and two bit characters find the string where the last character in the string is is one bit
# Ask clarifying questions
    # Is the input small or big?
    # What is the return value? According to the examples a boolean.
# State assumptions
    # 1 <= len(bits) <= 1000
    # There are only 0 and 1 elements in the array
# Think through process out loud
    # Brainstorm solution ideas
        # Get the modulo of the length of the list by two and if it equals zero
        ---
        # For the length of the list minus one
            # put two elements from the list in a tuple (bit, bit) until there are one               or two elements left in the list
            # then if the bit is one element return True otherwise return false
    # Explain your rationale
        # I want to quickly get to a point where I know the state of the last                       character but I cannot do that until I know the condition of the whole                    string
        ---
        # With the elements of the string either being 1 or 0 I can make an educated               guess that when there is an odd number of bits last digit can be one bit while           there are an even number the last digit is two bits
    # Discuss tradeoffs
        # Low time and space complexity
        ---
        # O(n) for looping through the string
        # Then creating two more data structures for the tuple holding 2 characters and             the data structure list holding the tuples
    # Suggest improvements
        # In the second idea, to decrease space complexity increment a counter and get             rid of tuple and list storage

class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        if len(bits) % 2 == 0:
            return False
        else:
            return True
