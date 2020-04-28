# Return True if any two of the numbers in te first array add up to any number in the second array
# Are there duplicates? No
# Yes potentially, 2 or 3 digit numbers
# Testcase:
# I:[-1], [-1]
# O: False, there aren't two numbers in the array to add and compare

# I:[-1, 8], [3, 7]
# O: True, b/c -1 + 8 is 7, 7 appears in the test array

# I:[-1, 8, 3], [3, 7, 2]
# O: False, there aren't two numbers in the array to add and compare


def find_tester(inputs, tests):#[-1, 8, 3], [3, 7, 2]
    '''
    Return True if any two of the numbers in te first array add up to any number in the second array
    '''
    if len(inputs) <= 1:
        return False
    sums = set()
    second_num_j = 1 
    # Gained sums
    for i, num in enumerate(inputs):
        second_num_j = i+1 
        while second_num_j < len(inputs):
            second_num = inputs[second_num_j]
            a_sum = num + second_num
            sums.add(a_sum) 
            second_num_j += 1
    print(sums)
    # Check if tests values found in sum
    for num in tests:
        if num in sums:
            return True
    return False


if __name__ == '__main__':
    # inputs = [-1]
    # tests = [-1]
    # inputs = [-1, 8]
    # tests = [3, 7]
    inputs = [-1, 8, 3]
    tests = [3, 7, 2]
    print(find_tester(inputs, tests))


