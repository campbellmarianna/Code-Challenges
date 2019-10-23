# Problem Link: https: // www.hackerrank.com/contests/sf-abcs19-stacks-and-queues/challenges/simple-text-editor
# create the stack
stack = [] # end is where the pushing and popping takes place
# create a state stack
state_stack = ['']
# get user input
Q =  input()
for i in range(Q):
  # based on operation i
  parts = input().strip().split(' ')
  if len(parts) == 2:
    q, item = parts
    # do append - 2
    if int(q) == 1:
      if len(item) == 1:
        stack.append(item)
      else:
        for char in item:
          stack.append(char)
    # do delete - 2
    if int(q) == 3:
      stack.(item)
    do print - 2
  elif len(parts) == 1:
    do undo - 1
  else: 
    print(f"Bad input: {parts}") 
  
  # append the state to the state stack


