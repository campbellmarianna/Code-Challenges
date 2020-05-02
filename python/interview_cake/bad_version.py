'''
You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which will return whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

Example:

Given n = 5, and version = 4 is the first bad version.

call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true

Then 4 is the first bad version. 
'''
# Find the first bad version of the program that doesn't pass the quality check.
# Given isBadVersion(version)


# Minize the number of calls to the API
# Input: Version Number
# Output: The first bad version

# Edge case
# Not a number => None
# Bad from the start return None
# Assume more than one more version
# 

# Example:
# 1, 2, 3, 4, 5
# access every version
    # check if API func returns false

# Suggested Improvement
# Make the solution faster using BS 
    # Check the midpoint first
def firstBadVersion(n): 
        """
        :type n: int
        :rtype: int
        """
        if type(n) != int:
            return None
        for version in range(1, n + 1): 
            if isBadVersion(version):
                return version
