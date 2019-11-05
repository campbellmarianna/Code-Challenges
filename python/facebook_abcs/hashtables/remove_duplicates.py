# loop the arr 'a
  # loop the arr a
    # check if there same
    # delete that value
# return the array
# Runtime (N^2)

# Hashtable
# Space: 0(n)
# Time: 0(n)
# str_input = input()
# print(type(str_input))
def removeDuplicates(str_input): #'aabc'
  ht = {}
  # loop arr create hashtable
  for char in str_input:
    if char in ht:
      # Increment char value
      ht[char] += 1
    else: # new char
      ht[char] = 1
  # check charc in hashtable
  i = 0 #3
  # result = ''
  while i < len(str_input):
    charValue = ht.get(str_input[i]) #1
    # only appears once we can move to the next char
    if charValue == 1:
      i += 1
      # result += 
      continue
    # found a duplicate
    if charValue >= 2:
      ht[str_input[i]] -= 1
      str_input = str_input[:i] + str_input[i+1:]
      
  # return array
  return str_input


# print(removeDuplicates(sample_input_4_dups))  # cba

## Iteration 2
# check if it is in ht
  # append to new result
# Not in the hashtable it is a duplicate and we speak


def removeDuplicates2(str_input):  # 'aabc'
  ht = {}
  # loop arr create hashtable
  for char in str_input:
    if char in ht:
      # Increment char value
      ht[char] += 1
    else:  # new char
      ht[char] = 1
  # check charc in hashtable
  i = 0  # 3
  result = '' #ab
  while i < len(str_input):
    # check if it is in ht
    if str_input[i] in ht:
      # append to new result
      result += str_input[i]
      ht.pop(str_input[i])
    i += 1
     # Not in the hashtable it is a duplicate and we skip and go to next number
  return result


sample_input_2_dups = 'aabc'
sample_input_4_dups = 'ccbabacc'
print(removeDuplicates2(sample_input_4_dups))  # cba
