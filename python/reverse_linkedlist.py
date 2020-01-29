def reverseList(self, head: ListNode) -> ListNode:
        curr = head
        prev = None
        next = None
        while curr is not None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev
