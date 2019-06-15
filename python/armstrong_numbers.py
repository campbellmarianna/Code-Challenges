# Exercism Problem: Armstrong Numbers
# Find out if a number is the sum of its own digits each raised to the power of
# number of digits

'''
Technical Interview Problem Solving Strategy
1. Generate reasonable test inputs
2. Understand the problem = Solve it!
    a. Simplify the problem if needed
3. Find a pattern in your solution
4. Make a plan - Write pseudocode
5. Follow a plan - Write real code
6. Check your work - Test your code
'''
def is_armstrong_number(number): # 153
    sum = 0
    result = 0
    string_version = str(number)
    power = len(string_version)
    # get the sum
    for i in range(0, power):
        individual_num = int(string_version[i])
        result = individual_num**power
        sum += result
    # check if the sum equals the given number
    if sum == number:
        return True
    else:
        return False

if __name__ == '__main__':
    print(is_armstrong_number(153))
