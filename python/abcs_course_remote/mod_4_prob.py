'''Look at the number of operations this function does.'''
def printFirstItem(array):
  '''
  Return the first item in list. Running time: 0(1) one operation is conducted to get the first item
  '''
  print('One Item')
  print(array[0])

# Time Complexity: 0(1)
# No matter how long the array is that we passIt will always only takes 2 steps to execute (it doesn't have to go beyond the first one) the number of operations does not grow as the input grows
def printAllItems(array):
  print('All')
  # Get every element in an array by its position
  for i in range(len(array)): # Using an interator variable to access every element in the array
    print(array[i])



def printAllPairs(array):
  print('All pairs')
  for i in range(len(array)):
    for j in range(len(array)):
      print(array[i], array[j])

    a1 = [1, 2, 3]
    a2 = [1, 2, 3, 4, 5, 6]
    a3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

    printAllPairs(a1)
    printAllPairs(a2)
    printAllPairs(a3)

# Time Complexity: 