### Second Iteration
def merge(nums1, m, nums2, n) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # take out zeros
        for num in range(0, n):
            nums1.pop(-1)
        # base case - check if merge is an empty nums1 with values from nums2
        if len(nums1) == 0 and len(nums2) > 0:
            for item in nums2:
                nums1.append(item)
        else:
            midpoint = len(nums1)//2
            print("nums1:", nums1)
            print("Midpoint in nums1:", midpoint)
            for item in nums2:
                print("NEW ITEM:", item)
                # check item is greater than midpoint
                if item > nums1[midpoint]:
                    index = midpoint
                else:
                    index = 0
                #check of item is a duplicate of the midpoint
                if item == nums1[midpoint]:
                    nums1.insert(midpoint, item)
                else:
                    for i in range(index, len(nums1)):
                        if nums1[i] == item or nums1[i] > item:
                            nums1.insert(i, item)
                            break
                        # check if the item is greater than all other values
                        last_num_index = len(nums1) - 1
                        if last_num_index == i and item > nums1[len(nums1) - 1]:
                            nums1.append(item)

        print(nums1)

### First Iteration
def merge(nums1, m, nums2, n) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # n_len = len(nums2) # take outs
        # m_len = len(nums1) # take outs
        for num in range(0, n):
            nums1.pop(-1)
        midpoint = len(nums1)//2 # change here to fix index error
        print("nums1:", nums1)
        print("Midpoint in nums1:", midpoint)
        for item in nums2:
            print("NEW ITEM:", item)
            # check item is greater than midpoint
            if item > nums1[midpoint]:
                index = midpoint
            else:
                index = 0
            #check of item is a duplicate of the midpoint
            if item == nums1[midpoint]:
                nums1.insert(midpoint, item)
            else:
                for i in range(index, len(nums1)):  # change here to fix index error
                    if nums1[i] == item or nums1[i] > item:
                        nums1.insert(i, item)
                        break
                    # add item to the end if the item is greater than all other values # addon
                    last_num_index = len(nums1) - 1
                    if last_num_index == i and item > nums1[len(nums1) - 1]:
                        nums1.append(item)

        print(nums1)



if __name__ == "__main__":
    # nums1 = [1, 2, 3, 0, 0, 0] # output [1, 2, 2, 3, 5, 6]
    # m = 3
    # nums2 = [2, 5, 6]
    # n = 3
    nums1 = [0] 
    m = 0
    nums2 = [1]
    n = 1

    merge(nums1, m, nums2, n)  # [1]
