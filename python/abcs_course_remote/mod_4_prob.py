'''Look at the number of operations this function does.'''
def printFirstItem(array):
  '''
  Return the first item in list. Running time: 0(1) one operation is conducted to get the first item
  '''
  print('One Item')
  print(array[0])

# Time Complexity: 0(1)
# No matter how long the array is that we pass in, it will always only take 2 steps to execute (it doesn't have to go beyond the first item) the number of operations does not grow as the input grows

def printAllItems(array):
  print('All')
  # Get every element in an array by its position
  for i in range(len(array)): # Using an interator variable to access every element in the array
    print(array[i])


# printAllPairs(a1)
# printAllPairs(a2)
# printAllPairs(a3)

# We do not create  an array use within the function to Data strucutres like this does not create a new array  - (above^^) array is passed in by reference


'''Count the loops'''
def printAllPairs(array):
  print('All pairs')
  for i in range(len(array)):
    for j in range(len(array)):
      print(array[i], array[j])

a1 = [1, 2, 3]
a2 = [1, 2, 3, 4, 5, 6]
a3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

# printAllPairs(a1)
# printAllPairs(a2)
# printAllPairs(a3)

# Time Complexity: 0(n * n) for n is length of the array 

''' Another way to solve it single_number problem from mod_3_prob - Using guided video in Problem Solving Course
'''
# Input non-empty array of integers
# Output: the single element in the list wihtout a pair
# Filter - Solution Idea 

# Psudeocode
# for every element in the input list
# if I have seen this element before
# remove it from the list of elements I have seen before
# otherwise:
#     add it to the list of elements I have seen before

def single_number(integers):
  numbers_i_have_seen_before = []
  for element in integers:
    # filter input data
    if element in numbers_i_have_seen_before: # secret loop
      numbers_i_have_seen_before.remove(element)
      # searches the list for the element then remove it once it finds the element
    else:
      numbers_i_have_seen_before.append(element)
  return numbers_i_have_seen_before.pop()

# Look at operations that grow in respect to the input n
# Lines that cause our execution times to grow 3, 4, and 5

# Time Complexity: 0(n) (loop through every int) + 0(m) (loop through numbers_i... or m to see if element is in there) + O(m) (search for element in numbers_i... or m to remove it) = 0(n + m) = 0(n)
# Space Complexity:0(n - d) (store every int except one that has a duplicate)

def single_number2(integers):
  numbers_i_have_seen_before = set()
  for element in integers:
    # filter input data
    if element in numbers_i_have_seen_before:  # secret loop
      numbers_i_have_seen_before.remove(element)
      # searches the list for the element then remove it once it finds the element
    else:
      numbers_i_have_seen_before.add(element)
  return numbers_i_have_seen_before.pop()

# Time Complexity:
# Space Complexity:

# current_list = [4, 1, 2, 1, 2]

# Lines that cause our execution times to grow 0
# Now can we do this in place (0(1) space complexity)
  # We can use some math, what we can do is have them cancel out
    # I had to look this up
    # I had to do was remember all the tricks about sequences of integers and so this is something you can learn and you can identify in an interview, but it is not something that they may, that they usually want to just like know from first principals and just know because you know math this is one of those math tricks
def single_number3(integers):
  sum_of_list = sum(integers)
  sum_of_set = 2 * sum(set(integers))
  singleton = sum_of_set - sum_of_list
  return singleton

# single_number([2, 2, 1])  # 1
print(single_number3([4, 1, 2, 1, 2]))  # 4

# Time Complexity: 0(n)(get sum) + 0(n)(create set) = 0(n)
# Space Complexity: 0(1)(store sum of list) + 0(n-d)(store set with no duplicate integers) + 0(1) + 0(1) (store unique value) = less than so 0(n-d)

'''
Reverse Operations
- Way do an operation on that data and return the reverse (how it was before)
- You can switch two variables intend of creating another variable
'''
x = 15
y = 10

x = x + y

y = x - y # Turn y into what x was

x = x - y

'''
Bitwise Operation Or - Bitwise ZOR (Exclusize Or)
- breaks a integer down into its binary parts then it goes number by number and compares each bit, there is bitwise or, bitwise just going to show you or because it is a form of a reverse operation
- "0b" tells python hey treat this as binary
- aka Inverse Operations
'''
a = 25
b = 15
binary_a = bin(a)
binary_b = bin(b)

a ^= b

binary_a = bin(a)
binary_b = bin(b)

a ^= b

binary_a = bin(a)
binary_b = bin(b)

# A Solution
nums = [4, 1, 2, 3, 2, 4, 3]

a = 0
binary_a = bin(a)
for i in nums:
  a ^= i # bitwise or
  binary_i = bin(i)
  binary_a = bin(a)


# print(a)

normal_list = [1,2,3,4,5,6,7]

doubled_list = [x**2 for x in range(5,125,5)]
print(doubled_list)

a_cool_set = {1,2,3}

print(a_cool_set)

another_cool_set = {str(x) for x in doubled_list}

print(another_cool_set)

print([x**2 for x in [x * 2 for x in doubled_list]])

# Where I left off: https://zoom.us/recording/play/0B6YxLPiJbqsXDIN_mZaHisOt0vKJXQDLEe7RPh0VAqIhPYz3I2c1WMC5n98_516?continueMode=true
# And where I'm at in the course: https://canvas.instructure.com/courses/1578976/pages/guided-topic-session-on-arrays-sets-and-inverse-functions-single-number-problem?module_item_id=23875609

