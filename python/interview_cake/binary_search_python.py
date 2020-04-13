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
        # if ot was to big we need to move the upper boundary down
        elif middle_element > value:
            right = middle - 1

if __name__ == '__main__':
    fruits = ['orange', 'plum', 'watermelon', 'apple']
    fruits.sort(key=len)
    print(fruits)
    print(fruits[find_index(fruits, key=len, value=10)])
    print(find_index(fruits, key=len, value=3))
