# Protobuffs Coding Challenge
# Hacker Rank Problem: https://www.hackerrank.com/challenges/mini-max-sum/problem
# Given 5 positive integars Find the minimum and maxium that could be calculated
# by suming 4 of them.
# Input: [1, 2, 3, 4, 5]
# Output: [10,14]
# total = []
# loop the array
# for num in array:
    # total += num # keep track of the total
    # first_sum = total - # subtract the minimum
# subtract the maxium
# join the list with a space and return it
def min_max_sum(input):
    # Initilize max and min
    min = input[0]
    max = input[0]
    total = 0
    output = []
    # capture each number and do a check
    for num in input:
        # add number to total
        total += num
        # check if num at num is smaller than min
        if num < min:
            # set min to num
            min = num
        # check if num at index is greater than maxium
        if num > max:
            # set max to num
            max = num
    # once that is done so we have checked all the numbers in the input
    # subtract min from total and store it in first_sum
    first_sum = total - min
    # append first_sum to output list
    output.append(first_sum)
    # subtract max from total and store it in
    second_sum = total - max
    # append first_sum to output list
    output.append(second_sum)
    # output list
    # converting integer list to string list and joining the list using join()
    # res = int("".join(map(str, output)))
    return output

if __name__ == '__main__':
    print(min_max_sum([1,2,3,4,5]))
