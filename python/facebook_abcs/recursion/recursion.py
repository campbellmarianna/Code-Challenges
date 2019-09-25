#!python
def fact_recursive(num):
  'Return factorial of given number using a recursive implementation'
  if num == 0:
    return 1
  else:
    return num * fact(num - 1);

# I: 5
# O: 120
# print(fact_recursive(5))

# Psudocode
# pass in num
# create product
# loop from 1 to num
  # mutiply curr_num by product
# return product


def fact_iterative(num):
  'Return factorial of given number using a iterative implementation'
  product = 1
  for curr_num in range (1, num + 1):
    product *= curr_num
  return product

print(fact_iterative(5))

'''
Problem Link: https://www.hackerrank.com/challenges/reverse-a-linked-list/problem
Prompt: 
You’re given the pointer to the head node of a linked list. Change the next pointers of the nodes so that their order is reversed. The head pointer given may be null meaning that the initial list is empty.

Input Format

You have to complete the SinglyLinkedListNode reverse(SinglyLinkedListNode head) method which takes one argument - the head of the linked list. You should NOT read any input from stdin/console.

The input is handled by the code in the editor and the format is as follows:

The first line contains an integer , denoting the number of test cases.
Each test case is of the following format:

The first line contains an integer , denoting the number of elements in the linked list.
The next  lines contain an integer each, denoting the elements of the linked list.

Constraints
...
, where  is the  element in the list.
Output Format

Change the next pointers of the nodes that their order is reversed and return the head of the reversed linked list. Do NOT print anything to stdout/console.

The output is handled by the code in the editor. The output format is as follows:

For each test case, print in a new line the elements of the linked list after reversing it, separated by spaces.

Sample Input

1
5
1
2
3
4
5
Sample Output

5 4 3 2 1 
Explanation

The initial linked list is: 1 -> 2 -> 3 -> 4 -> 5 -> NULL

The reversed linked list is: 5 -> 4 -> 3 -> 2 -> 1 -> NULL
'''
# For your reference:
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next

class SinglyLinkedListNode:
  'Return a LinkedList Node with data and a next property'
  
  def __init__(self, data):
    self.data = data
    self.next = None


# class LinkedList():
#   '''Return a LinkedList that has a head takes in nodes'''
#   def __init__(self, items=None):
#     self.head = None
#     self.tail = None
#     print("Created LinkedList with head and tail")
#     # Append given items
#     if items is not None:
#       for item in items:
#         self.append(item)

#   def append(self, item):
#     '''Add given item as a node to this Linked List'''
#     new_node = SinglyLinkedListNode(item)
#     if self.head == None:
#       self.head = new_node
#       self.tail = new_node
#     else:
#       self.tail.next = new_node
#     print("Inserted")

# Create node class
# Create linked list class
# Take in the head of a linked list
# create reversed linked list
# loop backwards through the given linked list
  # make the data a ll node
  # append it the reversed ll
# return the head of the reversed linkedlist node
def reverse(self):  # asume you have access to a created linkedlist
    # Return new head
    node = self.head
    reversed_items = []
    while node is not None:
      reversed_items.insert(0, node.data)
      node = node.next
    reversed_ll = LinkedList(reversed_items)
    return reversed_ll.head.data
  

# Psudocode by Geeks for Geeks  # https://www.geeksforgeeks.org/reverse-a-linked-list/
# 1. Initialize three pointers prev as None, curr as head and next as None
# 2. Iterate through the linked list. In loop, do following.
#   - Before changing next of current
#   - Store next node # like next = curr.next
#   - Now change next of current
#   - This where actual reversing happens # like curr.next = prev
#   - Move prev and curr one step forward # like prev = curr, curr = next
def reverse2(self):
  '''Return the head of the reversed Linkedlist
    Method Details: Change the next pointers of the nodes so that their order is reversed.'''
  # The reverse of the empty list or a single element list is the same
  if self.head is None or self.head.next is None:
    return self.head
  
  prev = None
  curr = self.head
  next = None

  while curr is not None:
    next = curr.next
    curr.next = prev
    prev = curr
    curr = next

example_ll = LinkedList([1, 2, 3])
# print(example_ll.reverse())

# Final Solution:
def reverse_iterative(head):
  '''Return the head of the reversed Linkedlist
    Method Details: Change the next pointers of the nodes so that their order is reversed.'''
  # The reverse of the empty list or a single element list is the same
  if head is None or head.next is None:
    return head

  prev = None
  curr = head
  next = None

  while curr is not None:
    next = curr.next
    curr.next = prev
    prev = curr
    curr = next
  head = prev
  return head

# Psudeocode
1) Divide the list in two parts - first node and rest of the linked list.
2) Call reverse for the rest of the linked list.
3) Link rest to first.
4) Fix head pointer

# Solutions from GeeksforGeeks https://www.geeksforgeeks.org/reverse-a-linked-list/
def reverse_recursive(head): 
  if head is None or head.next is None:
    return head
  # reverse the rest list and put the first element at the end 
  rest=reverse_recursive(head.next)
  next = head
  next.next = head

  head.next = None

  # fix the head pointer
  return rest

  class LinkedList():
    '''Return a LinkedList that has a head takes in nodes'''
    def __init__(self, items=None):
      self.head=None
      self.tail=None
      print("Created LinkedList with head and tail")
      # Append given items
      if items is not None:
        for item in items:
          self.append(item)

    def append(self, item):
      '''Add given item as a node to this Linked List'''
      new_node=SinglyLinkedListNode(item)
      if self.head == None:
        self.head=new_node
        self.tail=new_node
      else:
        self.tail.next=new_node
      print("Inserted")

  def reverseUtil(self, curr, prev):
    # If last node mark it head
    if curr.next is None:
      self.head = curr

      # Update next to prev node
      curr.next = prev
      return
    
    # Save curr.next node for recursive call
    next = curr.next

    # And update next
    curr.next = prev

    self.reverseUtil(next,curr)

  def reverse_recursive(self):
    if self.head is None:
      return
    self.reverseUtil(self.head, None)


