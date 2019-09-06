'''
Count the number of prime numbers less than a non-negative number, n.
'''
# Given positive number n return the range/group of numbers that are prime before reaching n
# Prime number - a number only divisible by 1 and itself
    # 5 = 5 * 1
# What is the type of the output? Int
# Input -> 4 Processing -> 2,3 Output -> 2
# Input -> 16 Processing -> 2,3,5,7,11,13 Output -> 6
# 0 is not prime
# 1 doesn't count


def isPrime(n): # 3
    '''
    Return True if give number is prime and False if it is not prime
    '''
    for current_num in range(2, n):
        # check if the number is not prime
        if n % current_num == 0:
            return False
    return True

# Define functon given n
def countPrimes(n):
    '''
    Given positive number n return the range/group of numbers that are prime before reaching n
    '''
    num_of_primes = 0
    for num in range(2, n): # 3
        print(num)
        if isPrime(num):
            num_of_primes += 1 # 1
    return num_of_primes




print(countPrimes(16))
            


