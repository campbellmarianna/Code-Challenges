# Problem Link: https: // www.hackerrank.com/contests/sf-abcs19-stacks-and-queues/challenges/simple-text-editor
# create the stack
s = '' # string in text editor
# create a state stack
state_stack = []
# get user input
Q =  input()
for i in range(int(Q)):
  parts = input().strip().split(' ')
  if len(parts) == 2:
    q, item = parts
    q = int(q)
    if q == 1:
      # Append
      s += item
      state_stack.append(s)
    if q == 2:
      # Delete
      item = int(item)
      s = s[:-item]
      state_stack.append(s)
    if q == 3:
      # Print
      item = int(item)
      index = item - 1
      print(s[index])
  elif len(parts) == 1: # Undo
      s = state_stack.pop()
      # check empyt
      if s == '':
        s = state_stack.pop()
  else: 
    print(f"Bad input: {parts}") 
  
## Iteration 2

s = ''  # string in text editor
# create a state stack
state_stack = []
# get user input
Q = input()
for i in range(int(Q)):
  parts = input().strip().split(' ')
  if len(parts) == 2:
    q, item = parts
    q = int(q)
    if q == 1:
      # Append
      s += item
      state_stack.append(s)
    if q == 2:
      # Delete
      item = int(item)
      s = s[:-item]
      state_stack.append(s)
    if q == 3:
      # Print
      item = int(item)
      print(s[int(item) - 1])
  elif len(parts) == 1:  # Undo
      s = state_stack.pop()
      # check empyt
      if s == '':
        s = state_stack.pop()
  else:
    print(f"Bad input: {parts}")


# Optimazation Idea
# - have one stack that tracks state and the last element we do the operation on
