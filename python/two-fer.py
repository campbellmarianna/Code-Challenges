"""
Exercism Challenge

Two-fer or 2-fer is short for two for one. One for you and one for me.
One for X, one for me.
When X is a name or you.

If the given name is Alice, the result should be One for Alice, one for me. If no name is given, the result should be One for you, one for me.
"""
def two_fer(name = "you"):
    result = f"One for {name}, one for me."
    # if name is given return sentence with name
    if name is not "you":
        return result
    # else return you in sentence
    return result
