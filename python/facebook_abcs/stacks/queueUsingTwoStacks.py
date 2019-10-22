def queuewithStacks(q, num=None):
    if q == 1:
        # Enqueue
        stack.append(num)
    if q == 2:
        # Delete
        stack.pop(0)
    if q == 3:
        # Print
        print(stack[0])


# get the number of queries
N = input()  # num of queries
# create stack
stack = []
# look that many times and call maximumElements func
for i in range(int(N)):
    # iput is query type and item
    parts = input().strip().split(' ')
    if len(parts) == 2:
        case, item = parts
        queuewithStacks(int(case), int(item))
    else:  # len(parts) == 1:
        case = parts[0]
        queuewithStacks(int(case))
