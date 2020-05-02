def find_index(elements, value, key):
    # set the lower and upper boundaries
    left, right = 0, len(elements) -1
    # to keep going 
    while left <= right:
        # identify middle element to see if it has desired value
        middle = (left + right) // 2
        middle_element = key(elements[middle])
        # if the middle was a match return its index
        if middle_element == value:
            return middle
        # Otherwise if it was too small, then we need to move the lower boundary up
        if middle_element < value:
            left = middle + 1
        # if it was to big we need to move the upper boundary down
        elif middle_element > value:
            right = middle - 1

def contains_v1(elements, value, left, right):
    '''
    Return bool  
    Params: list, int
    '''
    if left <= right:
        # identify middle element to see if it has a desired value
        middle = (left + right) // 2
        middle_element = elements[middle]

        # if the middle was a match return its index
        if middle_element == value:
            return True
        # use the slicing operator to chop off the list
        if middle_element < value:
            return contains(elements, value, middle+1, right)
        
        elif middle_element > value:
            return contains(elements, value, left, middle - 1)

    return False

# --- OR
def contains_v2(elements, value):
    return recursive(elements, value, 0, len(elements) - 1)

def recursive(elements, value, left, right):
    pass # ...

# --- OR
def contains(elements, value):
    def recursive(elements, value, left, right):
        if left <= right:
            middle = (left + right) // 2
            middle_element = elements[middle]

            if middle_element == value:
                return True
            
            if middle_element < value:
                return recursive(elements, value, middle + 1, right)

            if middle_element > value:
                return recursive(elements, value, left, middle-1)

        return False
    return recursive(elements, value, 0, len(elements)-1)


if __name__ == '__main__':
    # fruits = ['orange', 'plum', 'watermelon', 'apple']
    # fruits.sort(key=len)
    # print(fruits)
    # print(fruits[find_index(fruits, key=len, value=10)])  # watermelon
    # print(find_index(fruits, key=len, value=4)) # plum
    sorted_fruits = ['apple', 'banana', 'orange', 'plum']
    print(contains(sorted_fruits, 'apple'))

# Credits
# - https://realpython.com/binary-search-python/#implementing-binary-search-in-python
