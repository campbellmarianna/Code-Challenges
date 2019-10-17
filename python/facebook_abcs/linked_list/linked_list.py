class Node:
  int data
  Node.next

function hasCycle(head: Node) -> bool:
  if not head:
    return False
  slow = head
  fast = head.next
  while (slow is not None and fast is not None):
    if (slow.data == fast.data):
      return True
      slow = slow.next
      fast = fast.next.nextMeekness7
      