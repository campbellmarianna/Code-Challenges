'''
You have an empty sequence, and you will be given  queries. Each query is one of these three types:

1 x  -Push the element x into the stack.
2    -Delete the element present at the top of the stack.
3    -Print the maximum element in the stack.
Input Format

The first line of input contains an integer, . The next  lines each contain an above mentioned query. (It is guaranteed that each query is valid.)

Constraints



Output Format

For each type  query, print the maximum element in the stack on a new line.

Sample Input

10
1 97
2
1 20
2
1 26
1 20
2
3
1 91
3
Sample Output

26
91
'''
# Input: Number for case as well as item
# Output: Element: int
# Input: Number for case as well as item
# Output: Element: int


def maximumElement(q, num=None):
    stack = []
    if q == 1:
        # Push the element x into the stack.
        stack.append(num)

    if q == 2:
        # Delete the element present at the top of the stack.
        stack.pop()
    if q == 3:
        # Print the maximum element in the stack.
        print(max(stack))

### Second Iteration
# import sys
# for line in sys.stdin:
#     if len(line) <= 3:
#         continue
#     else:
#         maximumElement(line[0], line[2::])
#         print(line)


n = len(input())
for i in range(n):
    '''Get input as variables'''
    stack = []
    # a, b = input().strip().split(' ')
    # print (int(a) + int(b))
    if i <= 3:
        continue
    else:
        a, b = input().strip().split(' ')
        maximumElement(int(a), int(b))

def maximumElement(q, num=None):
    if q == '1':
        # Push the element x into the stack.
        stack.append(num)

    if q == '2':
        # Delete the element present at the top of the stack.
        stack.pop()
    if q == '3':
        # Print the maximum element in the stack.
        print(max(stack))
# n = len(input())
# for i in range(n):
#     a, b = input().strip().split(' ')
#     print (int(a) + int(b))

### Third Iteration
def maximumElement(q, num=None):
  '''Handle a query that is one of these three types
  1 x  -Push the element x into the stack.
  2    -Delete the element present at the top of the stack.
  3    -Print the maximum element in the stack.
  ''''
    if q == '1':
        # Push
        stack.append(num)  
    if q == '2':
        # Delete
        stack.pop()
    if q == '3':
        # Print
        print(max(stack))

# get the number of queries
N = input()  # num of queries
# create stack
stack = []
# look that many times and call maximumElements func
n = len(input())
for i in range(n):
    case, item = input().strip.split(' ')
    maximumElement(case, item)

#### Fourth Iteration
def maximumElement(q, num=None):
    if q == 1:
        # Push
        stack.append(num)
    if q == 2:
        # Delete
        stack.pop()
    if q == 3:
        # Print
        print(max(stack))


# get the number of queries
N = input()  # num of queries
# create stack
stack = []
# look that many times and call maximumElements func
for i in range(int(N)):
    # iput is query type and item
    try:
        parts = input().strip().split(' ')
        if len(parts) == 2:
            case, item == parts
            maximumElement(int(case), int(item))
        elif len(parts) == 1:
            case = parts[0]
            maximumElement(int(case))
        else:
            print(f"Bad input: {parts}")

#### Fifth Interation 
def maximumElement(q, num=None):
    if q == 1:
        # Push
        stack.append(num)
    if q == 2:
        # Delete
        stack.pop()
    if q == 3:
        # Print
        print(max(stack))


# get the number of queries
N = input()  # num of queries
# create stack
stack = []
# look that many times and call maximumElements func
for i in range(int(N)):
    # iput is query type and item
    try:
        parts = input().strip().split(' ')
        if len(parts) == 2:
            case, item = parts
            maximumElement(int(case), int(item))
        else:  # len(parts) == 1:
            case = parts[0]
            maximumElement(int(case))

### Sixeth Iteration 
def maximumElement(q, num=None):
    if q == 1:
        # Push
        stack.append(num)
    if q == 2:
        # Delete
        stack.pop()
    if q == 3:
        # Print
        print(max(stack))


# get the number of queries
N = input()
# create stack
stack = []
# look N times and call maximumElements func
for i in range(int(N)):
    # input is query type and item
    parts = input().strip().split(' ')
    if len(parts) == 2:
        case, item = parts
        maximumElement(int(case), int(item))
    elif len(parts) == 1:
            case = parts[0]
            maximumElement(int(case))
    else:
        print(f"Bad input: {parts}")

### Seventh Iteration
class Stack:
  def __init__(self):
    self.list = list()

  def __repr__(self):
        """Return a string representation of this stack."""
        return 'Stack({} items, top={})'.format(self.length(), self.peek())

  def length(self):
        """Return the number of items in this stack."""
        return len(self.list)

  def peek(self):
        """Return the item on the top of this stack without removing it,
        or None if this stack is empty."""
        # Return top item, if any
        # Check of stack is empty
        if self.is_empty() == True:
            return None
        return self.list[-1]

  def is_empty(self):
    """Return True if this stack is empty, or False otherwise."""
    # Check if empty
    if not self.list:
        return True
    else:  # If first is not empty
        return False

  def push(self, item):
    self.list.append(item)

  def pop(self):
    self.list.pop()

  def printMax(self):
    print(max(self.list))


# get the number of queries
N = input()
# create stack
stack = Stack()
# look N times and call maximumElements func
for i in range(int(N)):
    # input is query type and item
    parts = input().strip().split(' ')
    # print(f"Parts: {parts}")
    # print(f"Stack: {stack.__repr__()}")
    if len(parts) == 2:
        case, item = parts
        if int(case) == 1:
            stack.push(item)
    elif len(parts) == 1:
            case = parts[0]
            if int(case) == 2:
                stack.pop()
            if int(case) == 3:
                stack.printMax()
    else:
        print(f"Bad input: {parts}")
# create an instance of the queue or stack class then check for the case then call different methods based on input

# use two stacks
