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

# Create node class
# Create linked list class
# Take in the head of a linked list
# create reversed linked list
# loop backwards through the given linked list
  # make the data a ll node
  # append it the reversed ll
# return the head of the reversed linkedlist node


class SinglyLinkedListNode:
  'Return a LinkedList Node with data and a next property'
  
  def __init__(self, data):
    self.data = data
    self.next = None

  

class LinkedList():
  '''Return a LinkedList that has a head takes in nodes'''
  def __init__(self, items=None):
    self.head = None
    self.tail = None
    print("Created LinkedList with head and tail")
    # Append given items
    if items is not None:
      for item in items:
        self.append(item)

  def append(self, item):
    '''Add given item as a node to this Linked List'''
    new_node = SinglyLinkedListNode(item)
    if self.head == None:
      self.head = new_node
      self.tail = new_node
    else:
      self.tail.next = new_node
    print("Inserted")

  def reverse(self):  # asume you have access to a created linkedlist
      '''Change the next pointers of the nodes so that their order is reversed.''' # Return new head
      node = self.head
      reversed_items = []
      while node is not None:
        reversed_items.insert(0, node.data)
        node = node.next
      reversed_ll = LinkedList(reversed_items)
      return reversed_ll.head.data


example_ll = LinkedList([1, 2, 3])
print(example_ll.reverse())