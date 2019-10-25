# add two arrays
# loop through arr by i till last elem minus 1
  # check if left is less than right
  # store right 
  # set right now to left value
  # set left to stored right

# Merge two arrays together
# Check element one by one to see if one element is greater than another if it is not I swap the values
def mergeTwoSortedArr(arr1, arr2):
  '''
  Return one sorted array which is the result of two sorted arrays
  '''
  mergedArr = arr1 + arr2
  for i in range(len(mergedArr) - 1):
    left = mergedArr[i]
    right = mergedArr[i + 1]
    if left > right:
      temp = right
      mergedArr[i + 1] = left
      mergedArr[i] = temp
  return mergedArr

 
print(mergeTwoSortedArr([1,6], [2,5]))
print(mergeTwoSortedArr([2, 4], [2, 7,8,9]))
