'''
Link: https://www.geeksforgeeks.org/find-number-distinct-palindromic-sub-strings-given-string/
Given a string produce all possible polindrome substrings.
EX:
input: str = "geek"
output:
"g"
"ee"
"k"
"e"
'''
# input: str
# output: list of strings

# gold
# output:
["g", "o", "l", "d"]
# no numbers
# outputing letters that appear consecutivel

# check the whole string if it is a palindrome
# check the string except last character if if it is a palindrome
# no so check middle characters if if it is a palindrome
# yes I add that as ouput 
# Break up substring in half and check if it is a palindrome
# yes output
# other half

# NOTE: before putting in output check if the substring is already there
# NOTE: make sure the strategy checks all substrings of the string
# - add each unique character to the ouput (being a set)
# - whole string
# - excuss the last character
# - check 

def is_palindrome(s):
    '''Big O Time: 0(n), Big 0(2n), n is the characters within the given string'''
    pass

def find_substring_palindrome(s):
    '''Big O Time: 0(n), Big 0(n*palindrome), n is the characters within the given string'''
    output = set()
    # add all unquie single letter palindromes
    for char in s:
        if char in output:
            continue
        else:
            output.add(char)
    return output
# Python program Find all distinct palindromic sub-strings
# of a given string

# Function to print all distinct palindrome sub-strings of s


def palindromeSubStrs(s):
	m = dict() # {}
	n = len(s) # 4

	# table for storing results (2 rows for odd-
	# and even-length palindromes start with column as you go create the rows
	R = [[0 for x in xrange(n+1)] for x in xrange(2)] 
    # 0, - 2
        # 0 - 5

    [
        # Odd [],
        # Even []
    ]

	# Find all sub-string palindromes from the given input
	# string insert 'guards' to iterate easily over s
	s = "@" + s + "#"

	for j in xrange(2):
		rp = 0  # length of 'palindrome radius'
		R[j][0] = 0

		i = 1
		while i <= n:

			# Attempt to expand palindrome centered at i
			while s[i - rp - 1] == s[i + j + rp]:
				rp += 1  # Incrementing the length of palindromic
				# radius as and when we find valid palindrome

			# Assigning the found palindromic length to odd/even
			# length array
			R[j][i] = rp
			k = 1
			while (R[j][i - k] != rp - k) and (k < rp):
				R[j][i+k] = min(R[j][i-k], rp - k)
				k += 1
			rp = max(rp - k, 0)
			i += k

	# remove guards
	s = s[1:len(s)-1]

	# Put all obtained palindromes in a hash map to
	# find only distinct palindrome
	m[s[0]] = 1
	for i in xrange(1, n):
		for j in xrange(2):
			for rp in xrange(R[j][i], 0, -1):
				m[s[i - rp - 1: i - rp - 1 + 2 * rp + j]] = 1
		m[s[i]] = 1

	# printing all distinct palindromes from hash map
	print "Below are " + str(len(m)) + " pali sub-strings"
	for i in m:
		print i


# Driver program
palindromeSubStrs("abaaa")
# This code is contributed by BHAVYA JAIN and ROHIT SIKKA

if __name__ == "__main__":
    s = "geek"
    print(find_substring_palindrome(s))
