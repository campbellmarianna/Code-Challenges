# All cookies have sweetness greater than value K
# Combine cookies with low sweetness
# Check if sweetness is greater than K
# Do this procedure for every cookie in the collection
# Return num of procedure and -1 if there is 0 num of procuedures
# Complete the cookies function below.

# loop through a
# check each cookie's sweetness check if it is greater than K
# if it is go to the next cookie
# if it is not combine the first and second cookie and check pop them out of the collection and append the new sweetness


def cookies(k, A):
    op_counter = 0
    i = 0
    # loop through a cookies - while we still have cookies
    while len(A) > 0:
        # check each cookie's sweetness check if it is greater than K
        if A[i] >= k:  # high cookie sweetness
            # if it is go to the next cookie
            # index += 1
            A.pop(i)
            continue
        else:  # low cookie sweetness
            # if it is not combine the first and second cookie and check pop them out of the collection and                   append the new sweetness
            op_counter += 1
            new_sweetness_index = i
            second = A.pop(i+1)
            first = A.pop(i)
            sweetness = 1 * first + 2 * second  # 5, 11
            A.insert(new_sweetness_index, sweetness)
    return op_counter
