class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


node_one = ListNode(100)
root_one = node_one
node_one.next = ListNode(2000)
node_one = node_one.next
node_one.next = ListNode(4000)

node_two = ListNode(101)
root_two = node_two
node_two.next = ListNode(3000)
node_two = node_two.next
node_two.next = ListNode(4000)


# Company X just merged with company Y and they're merging their databases.
# Their accounts are currently sorted by revenue amount (smallest first) as linked lists
# Write code to merge their lists and return a new list.

# Example:

# Input: 100->2000->4000, 101->3000->4000
# Output: 100->101->2000->3000->4000->4000

# Definition for singly-linked list.

# Notes
# can modify
# smallest to largest

# create revenue amounts list
# loop ll 1
# add node data
# loop ll 2
# add node data
# sort list
# create new ll
# insert a new node to ll list

# def mergeTwoLists(node_one: ListNode, node_two: ListNode):
def mergeTwoLists(node_one, node_two):
    rev_amounts = []  # 100, 101, 2000, 3000, 4000, 4000
    while node_one is not None and node_two is not None:
        if node_one.val < node_two.val:
            rev_amounts.append(node_one.val)
            node_one = node_one.next
        else:
            rev_amounts.append(node_two.val)
            node_two = node_two.next
    # after exiting the while loop, we know that one of the lists (or maybe both) doesn't have any nodes left
    while node_one is not None:
        rev_amounts.append(node_one.val)
        node_one = node_one.next
    while node_two is not None:
        rev_amounts.append(node_two.val)
        node_two = node_two.next
    # create result ll
    # make the root the first item in the list 
    # then started from the second item add a new node with the current data to the list
    result_head = ListNode(rev_amounts[0])
    i = 1
    while i < len(rev_amounts) and :
        data = rev_amounts[i]
        ListNode(data)
    # 
    return rev_amounts


print(mergeTwoLists(root_one, root_two))
# compare
#add smallest to result ll
# move forward with smallest


# Edges cases:
# List 1 and 2 have nodes
# List 1 has nodes and List 2 doesn't
# List 2 has nodes and List 1 doesn't


# List 1: 100->2000->4000
# List 2: 101->3000->4000->5000

# List 3:
# compare 100 and 101 --> add 100, move forward
# compare 101 and 2000 --> add 101, move forward
# compare 2000 and 3000 --> add 2000, move forward
