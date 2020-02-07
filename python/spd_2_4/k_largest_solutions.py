'''
Given an array a of n numbers and a count k find the k largest values in the array a.
Example: a=[5, 1, 3, 6, 8, 2, 4, 7], k=3  =>  [6, 8, 7]

There are multiple ways to solve Two Sum.
What is described below:
- solution ideas
- code implementations
'''
# sort given list and return a slice as the length of k
def find_k_largest1(a, k):
    a_sorted = sorted(a)
    return a_sorted[-k:]

# - start a largest with the length of k
# - interate the array and check if it is greater than any number in the largests array if so pop out the lesser value and and input the new greater value

def find_k_largest2(a,k):
    # create a copy of the list
    a_copy = a[:]
    largest_vals = []
    max_val = 0
    # find the largest and pop it
    while len(largest_vals) < k:
        max_val = max(a_copy)
        max_val_index = a_copy.index(max_val)
        a_copy.pop(max_val_index)
        print("max_val:", max_val)
        largest_vals.append(max_val)
        print("LENGTH OF ARR:", len(largest_vals))
        # add it to the result
        # check the length of the result that it is less than k
            # if it is keep interating
        # otherwise stop and return result
    return largest_vals

if __name__ == "__main__":
    a = [5, 1, 3, 6, 8, 2, 4, 7]
    k = 3
    print(find_k_largest2(a, k)) # [6,8,7]

