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
    largest_k = [] # [5,1,3]
    for i in range(k):
        largest_k.append(a[i])
    i = k
    while i < len(a):
        num = a[i]
        print(num)
        for largest_num in largest_k:
            if num > largest_num:
                largest_k.pop(largest_num)
                largest_k.append(num)
                print("NEW LARGEST ARR:", largest_k)
        i += 1
    return largest_k

if __name__ == "__main__":
    a = [5, 1, 3, 6, 8, 2, 4, 7]
    k = 3
    print(find_k_largest1(a, k)) # [6,8,7]

