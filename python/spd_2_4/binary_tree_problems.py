'''
Prompt:
Given a binary search tree, reverse the order of its values by modifying the nodes’ links.
'''
# Edge cases:
# - no left or no right child 

# Plan (Basic Idea)
# - loop tree
# - get access to children
# - use a temp to store the right node

# Plan 2
# - get array 
# - reverse array
# - build tree based on reversed oder

# Plan 3
# level order traversal
# swap children


# Simplify
# tree nodes >= 3 nodes
# at least tree with 2 children

class BinaryTreeNode():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree():
    def __init__(self):
        self.root = None
    
    def reverse1(self):
        val_list = []
        temp = None
        while node is not None:
            val_list.append(node.data)
            if node.left:
                node = node.left
            elif node.right:
                node = node.right
            else:
                break
        return val_list
# Binary Search Tree in Python  Credits: Joe James  https://youtu.be/YlgPi75hIBc
class Node:
    def __init__(self, val):
        self.value = val
        self.leftChild = None
        self.rightChild = None
    
    def insert(self,data):
        if self.value == data:
            return False
        elif self.value > data:
            if self.leftChild:
                return self.leftChild.insert(data)
            else:
                self.leftChild = Node(data)
                return True 
        else:
            if self.rightChild:
                return self.rightChild.insert(data)
            else:
                self.rightChild = Node(data)
                return True
    
    def find(self, data):
        if(self.value == data):
            return True
        elif self.value > data:
            if self.leftChild:
                return self.leftChild.find(data)
            else:
                return False
        else:
            if self.rightChild:
                return self.rightChild.find(data)
            else:
                return False
    
    def preorder(self):
        if self:
            print(str(self.value))
            if self.leftChild:
                self.leftChild.preorder()
            if self.rightChild:
                self.rightChild.preorder()
    
    def postorder(self):
        if self:
            if self.leftChild:
                self.leftChild.postorder()
            if self.rightChild:
                self.rightChild.postorder()
            print(str(self.value))
    
    def inorder(self):
        if self:
            if self.leftChild:
                self.leftChild.inorder()
            print(str(self.value))
            if self.rightChild:
                self.rightChild.inorder()



class Tree:
    def __init__(self):
        self.root = None

    def insert(self,data):
        if self.root:
            return self.root.insert(data)
        else:
            self.root = Node(data)
            return True
    
    def find(self, data):
        if self.root:
            return self.root.find(data)
        else:
            return False

    def preorder(self):
        print("PreOrder")
        self.root.preoder()

    def postorder(self):
        print("PostOrder")
        self.root.postorder()
    
    def inorder(self):
        print("InOrder")
        self.root.inorder()


            

if __name__ == "__main__":
    # bst = BinarySearchTree()
    bst = Tree()
    bst.insert(10)
    print(bst.insert(15))
    bst.preorder()
    bst.postorder()
    
