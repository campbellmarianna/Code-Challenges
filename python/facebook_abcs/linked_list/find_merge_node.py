'''
Prompt:
This challenge is part of a tutorial track by MyCodeSchool

Given pointers to the head nodes of  linked lists that merge together at some point, find the Node where the two lists merge. It is guaranteed that the two head Nodes will be different, and neither will be NULL.

In the diagram below, the two lists converge at Node x:

[List #1] a--->b--->c
                     \
                      x--->y--->z--->NULL
                     /
     [List #2] p--->q
Complete the int findMergeNode(SinglyLinkedListNode* head1, SinglyLinkedListNode* head2) method so that it finds and returns the data value of the Node where the two lists merge.

Input Format

Do not read any input from stdin/console.

The findMergeNode(SinglyLinkedListNode,SinglyLinkedListNode) method has two parameters,  and , which are the non-null head Nodes of two separate linked lists that are guaranteed to converge.

Constraints

The lists will merge.
.
 .

Output Format

Do not write any output to stdout/console.

Each Node has a data field containing an integer. Return the integer data for the Node where the two lists merge.

Sample Input

The diagrams below are graphical representations of the lists that input Nodes  and  are connected to. Recall that this is a method-only challenge; the method only has initial visibility to those  Nodes and must explore the rest of the Nodes using some algorithm of your own design.

Test Case 0

 1
  \
   2--->3--->NULL
  /
 1
Test Case 1

1--->2
      \
       3--->Null
      /
     1
Sample Output

2
3
Explanation

Test Case 0: As demonstrated in the diagram above, the merge Node's data field contains the integer .
Test Case 1: As demonstrated in the diagram above, the merge Node's data field contains the integer .
'''

def nodeDataFound(head2, otherNodeData):
  '''Return true if given data is found in the given linked list.'''
  node = head2
  while node is not None:
    if node.data == otherNodeData:
      return True
    node = node.next


def findMergeNode(head1, head2):
  node = head1
  headData = head1.data
  while node is not None:
    # skip head node
    if node.data == headData:
      node = node.next 
    # check if data of curr node is found in LL2
    if nodeDataFound(head2, node.data):
      return node.data
    node.next

####### Another attempt
# solution idea from Mayinblack on https://leetcode.com/problems/intersection-of-two-linked-lists/discuss/49846/Python-solution-for-intersection-of-two-singly-linked-lists

def findMergeNode2(head1, head2):
  node1 = head1
  node2 = head2
  while node1 and node2 and node1 != node2:
    node1 = node1.next
    node2 = node2.next
    if node1 == node2:
      return node1

####### Another attempt
# solution idea from ... on https://leetcode.com/problems/intersection-of-two-linked-lists/discuss/49846/Python-solution-for-intersection-of-two-singly-linked-lists


def findMergeNode3(head1, head2):
  node1 = head1
  node2 = head2
  list1_len = 0
  list2_len = 0
  while node1 is not None:
    list1_len += 1
    node1 = node1.next
  while node2 is not None:
    list2_len += 1
    node2 = node2.next
  if list1_len > list2_len:
    for i in range(list1_len - list2_len):
      node1 = node1.next
      node2 = node2.next
  if list2_len > list1_len:
    for i in range(list2_len - list1_len):
      node1 = node1.next
      node2 = node2.next
  while node1 != node2:
    node1 = node1.next
    node2 = node2.next
  return node1




