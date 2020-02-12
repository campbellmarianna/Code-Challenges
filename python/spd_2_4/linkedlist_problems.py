""" 
Prompt #1
Given a singly-linked list, reverse the order of the list by modifying the nodes links.

Prompt #2 
Rotate a given linked list counter-clockwise by k nodes, where k is a given integer.
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
    
    def rotate(self, k):
        curr = self.head
        prev = None
        node_counter = 0

        while curr is not None:
            if node_counter == k:
                self.head = curr
                prev.next = None
                break

            self.insert(curr.data)
            node_counter += 1
            prev = curr
            curr = curr.next



if __name__ == "__main__":
    ll = LinkedList()
    print(ll)
    ll.insert('A')
    ll.insert('B')
    ll.insert('C')
    ll.insert('D')
    ll.insert('E')
    ll.insert('F')
    # ll.display_ll_data()
    # ll.reverse()
    k = 4
    ll.rotate(k)
    ll.display_ll_data()

