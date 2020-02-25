# loop sequence from start to one passed end
def fizzbuzz_iterative(start, end):
    result_list = []
    for element in range(start, end + 1):
        # check for divisible 
        if element % 3 == 0 and element % 5 == 0:
            result = 'FizzBuzz'
        elif element % 3 == 0:
            result = 'Fizz'
        elif element % 5 == 0:
            result = 'Buzz'
        else:
            result = element
        # append to result list
        result_list.append(result)
    return result_list


def fizzbuzz_recurrsive(start, end):
    
Python gotcha Python for Hitchhikers
- LinkedList
if __name__ == '__main__':
    start = 1
    end = 20
    print(fizzbuzz(start, end))
