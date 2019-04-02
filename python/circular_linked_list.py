class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

class Circular_linked_list():
    def __init__(self):
        self.head = None
        self.tail = None


if __name__ == "__main__":

    ll = Circular_linked_list()

    a = Node(1)
    b = Node(2)
    c = Node(3)

    b.next = c
    c.next = a
