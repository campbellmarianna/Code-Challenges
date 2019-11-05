'''
Prompt:
The median of a set of integers is the midpoint value of the data set for which an equal number of integers are less than and greater than the value. To find the median, you must first sort your set of integers in non-decreasing order, then:

If your set contains an odd number of elements, the median is the middle element of the sorted sample. In the sorted set ,  is the median.
If your set contains an even number of elements, the median is the average of the two middle elements of the sorted sample. In the sorted set ,  is the median.
Given an input stream of  integers, you must perform the following task for each  integer:

Add the  integer to a running list of integers.
Find the median of the updated list (i.e., for the first element through the  element).
Print the list's updated median on a new line. The printed value must be a double-precision number scaled to  decimal place (i.e.,  format).
Input Format

The first line contains a single integer, , denoting the number of integers in the data stream.
Each line  of the  subsequent lines contains an integer, , to be added to your list.

Constraints

Output Format

After each new integer is added to the list, print the list's updated median on a new line as a single double-precision number scaled to  decimal place (i.e.,  format).

Sample Input

6
12
4
5
3
8
7
Sample Output

12.0
8.0
5.0
4.5
5.0
6.0
'''
# Find the median of given array
# Idea:
  # sort array
  # Find median
  # Print array
# Assumptions
  # no negatives
  # Empty => return value error
  # 1 item => 1 item
  # input arr
  # output => decimal number

# Further Psudeocode/Notes:
  # make string
  # loop and check for '.'
  #   that index and forward make slice
  #   check lenof slice is 1
  #   return raw_medium
  # return new slice

## Iteration 1
# def proper_format(med_int):
#   '''
#   Return the given raw_mediant as a float with just one number after the decimal
#   '''
#   med_str[i] = str(med_int)
#   dot_index = 0
#   for i in range(len(med_str)):
#     if med_str[i] == '.':
#       dot_index = i
#       after_dot = med_str[i+1]
#       break
#   if len(after_dot == 1):
#     return med_int
#   else: # round up
#     if med_str[dot_index + 2] > med_str[dot_index + 1]:
#       right = int(med_str[dot_index + 1]) + 1
#       left = med_str[:dot_index+1]
#       new_med_str = left + right
#       return float(new_med_str)
#     else:
#       new_med_str = left + right
#       return float(new_med_str)

# def runningMedian(a):
#   '''
#   Return median as a float of a given array.
#   '''
#   if len(0) == 0:
#     return ValueError('Invalid Input:', a)
#   if len(a) == 1:
#     return float(a[0])
#   # given valid array
#   if len(a)/2 % == 0: # check if even
#     first = a[(len(a)/2)-1]
#     second = a[(len(a)/2)]
#     raw_median = (first+second)/2
#     final_median = proper_format(raw_median)
#   else:
#     return float(a[len(a)//2])

## Iteration 2

def runningMedian2(a):
  '''
  Return median as a float of a given array.
  '''
  if len(a) == 0:
    return ValueError('Invalid Input:', a)
  if len(a) == 1:
    if isinstance(a[0], float):
      return round(a[0], 1)
    else:
      return float(a[0])
  # sort given array
  a.sort()
  if len(a)%2 == 0:  # check if even
    first = a[(len(a)//2)-1] 
    second = a[(len(a)//2)]
    raw_median = (first+second)/2 #
    if isinstance(raw_median, float):
      final_median = round(raw_median, 1) # 2.5
      return final_median
    else:
      result = float(raw_median)
      return result
  else: # the length of given a is odd
    final_median_index = len(a)//2
    result = float(a[final_median_index])
    return result


odd_len_arr = [1, 2, 3] # 2.0
even_len_arr = [1, 2, 3, 4] # 2.5
default_ex = [12, 4, 5, 3, 8, 7]
print(runningMedian2([12, 4, 5, 3, 8, 7]))
