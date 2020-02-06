'''
You’re working an internship at Twitter and are tasked to improve suggestions for accounts to follow, which already works great for established accounts because it uses content from your tweets and other accounts you follow to suggest new ones. However, when a new user signs up none of this information exists yet, but Twitter still wants to make some follow suggestions. Your team asked you to implement a function that accepts a new user’s handle and an array of many other users’ handles, which could be very long – Twitter has over 330 million active accounts! You need to calculate a similarity score between a pair of handles by looking at the letters each contains, scoring +1 for each letter in the alphabet that occurs in both handles but scoring –1 for each letter that occurs in only one handle. Your function should return k handles from the array that have the highest similarity score to the new user’s handle.

Example execution:
handles = ['DogeCoin', 'YangGang2020', 'HodlForLife', 'fakeDonaldDrumpf', 'GodIsLove', 'BernieOrBust']
suggest('iLoveDogs', handles, k=2)   should return   ['GodIsLove', 'DogeCoin']

'''
# new user - no data on user to use to make follower recommendations
# In a huge list of twitter handles for every character you find in both handles add 1 and for every different character subtract 1 and return two handles with the highest similarity score

'''
Iteration #1: 
Simplified the problem:
- arr of 1 handle and find score
- handle <= 6 characters
- all lowercase
- no numbers
- just add if a similarity is found
- no duplcates
'''
# Pseudocode
# define func
    # create seen set
    # loop str
        # if not found
            # add set
        # otherwise 
            # increment similarity

def findSimilarityScore(arr):
    dup = 0
    seen = set()
    handle = arr[0]
    for char in handle:
        if char in seen:
            dup += 1
        else:
            seen.add(char)
        return dup
'''
Iteration #2:
- arr of 1 handle and find score
'''

# create seen set
   # loop str 1
        # add every character to set
    # loop str 2
        # if found
        # increment similarity

def findSimilarityScore2(arr):
    dup = 0
    seen = set()
    handle_one = arr[0]
    handle_two = arr[1]
    for char in handle_one:
        if char not in seen:
            print("NEW CHARATER:", char)
            seen.add(char)
    for char in handle_two:
        if char in seen:
            dup += 1
    return dup
        

if __name__ == '__main__':
    arr = ['agile'] # 0
    arr2 = ['agile', 'waterfall'] # 5
    print(findSimilarityScore2(arr2))
