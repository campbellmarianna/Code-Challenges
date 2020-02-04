# node class
class Node():
    def __init__(self, data):
        self.data = data
        self.next = next
clss LinkedList():
    def __init__(self):
        self.head = None
    
    def reverse(self):
        curr = self.head
        prev = None
        forward_one = None
        while node is not None:
            curr.next = prev
            prev = curr
            curr = node.next
        return self.head

# linkedlist
# Function
if __name__ == "__main__":
    new_node = Node(4)
    print(new_node.data)
