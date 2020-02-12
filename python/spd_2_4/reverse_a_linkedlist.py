""" Prompt:
Given a singly-linked list, reverse the order of the list by modifying the nodes links.
"""
class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None
    
    def insert(self, item):
        new_node = Node(item)
        node = self.head 
        if self.head == None:
            self.head = new_node
        else:
            while node is not None:
                if node.next == None:
                    node.next = new_node
                    break
                node = node.next
    def display_ll_data(self):
        '''Return one by one the data of the nodes in the LinkedList'''
        node = self.head
        while node is not None:
            print(node.data)
            node = node.next
            
    def reverse(self):
        curr = self.head
        prev = None
        next = None
        while curr is not None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        self.head = prev

# run and test code
if __name__ == "__main__":
    ll = LinkedList()
    print(ll)
    ll.insert('A')
    ll.insert('B')
    ll.insert('C')
    ll.insert('D')
    ll.insert('E')
    # ll.display_ll_data()
    ll.reverse()
    ll.display_ll_data()

