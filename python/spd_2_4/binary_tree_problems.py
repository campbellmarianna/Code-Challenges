'''
Prompt:
Given a binary search tree, reverse the order of its values by modifying the nodes’ links.

Check print_reverse method for solution.
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
# - build tree based on reversed order

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
        self.length = 0
    
    def print_bfs(self):
        if not self.root:
            return

        queue = [self.root]

        while len(queue) > 0:
            current_node = queue.pop(0)
            print(current_node.data)
            self.length += 1
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)

    def print_reverse(self):
        print("Reverse")
        if not self.root:
            return

        queue = [self.root]

        while len(queue) > 0:
            current_node = queue.pop(0)
            print(current_node.data)
            if current_node.right and current_node.left:
                tmp_right = current_node.right
                tmp_left = current_node.left
                current_node.left = tmp_right
                current_node.right = tmp_left
                queue.append(current_node.left)
                queue.append(current_node.right)
            else:
                if current_node.left:
                    queue.append(current_node.left)
                if current_node.right:
                    queue.append(current_node.right) 
    
    def find_two_sum(self, t):
        node = self.root
        # create result
        result = []
        # traverse tree
        while node is not None:
            # subtract curr node.data from target
            comp = t - node.data
            # check if complement in tree
            is_found = self.search(comp)
            # add curr node.data and complent to result and stop
            if is_found:
                result.extend([node.data, comp])
                break
            # otherwise go to next node
            else:
                if node.left:
                    node = node.left
                else:  # node.right
                    node = node.right
                # node = node.next
        # if complement never found return result (empty list)
        return result
    
    def search(self, t):
        node = self.root
        while node is not None:
            if node.data == t:
                return True 
            elif node.left:
                node = node.left
            elif node.right:
                node = node.right
        return False


    
'''
Prompt:
Given a binary search tree containing integers and a target integer, come up with an efficient way to locate two nodes in the tree whose sum is equal to the target value.
'''
# Given a BST and a target write an algorithm that efficiently (greater than n^2 or n^m) find two numbers in the BST that have a sum of the target 
# input: BST=[8,2,4,5,11,12,14], t=[9]
# output: [4,5]
# Ask c qs through making assumptions
# - small BST
# - return empty when no nodes meet the target
# Write your own test input and out - Understand the problem
# [8, 4] => []
# Brainstorm 2 ideas at least
# - calculate and find complement - 0(n)*(log(n)) S:0(1)
# - Put nodes in a list and loop the list for the currrent and the compement - 0(n)+0(n)*0(n-1) S: 0(n)
# break solution idea into parts
# calculate complement
    # single digit number
# find complement and return it
    # find 1 complement
# simplify parts if need be # DONE
# psuedocode
# create result
# traverse tree
    # subtract curr node.data from target
    # check if complement in tree
        # add curr node.data and complent to result and stop
    # otherwise go to next node
# if complement never found return result (empty list)
    
# code
# looking about edge cases what could break your code
# test




if __name__ == "__main__":
    # bst = BinarySearchTree()
    tree = BinarySearchTree()
    # Test Case 1
    # tree.root = BinaryTreeNode(9)

    # tree.root.left = BinaryTreeNode(5)
    # tree.root.right = BinaryTreeNode(11)

    # tree.root.left.left = BinaryTreeNode(3)
    # tree.root.left.right = BinaryTreeNode(7)
    
    # tree.print_bfs()
    # tree.print_reverse()

    # Test Case 2
    # tree.root = BinaryTreeNode('red')

    # tree.root.left = BinaryTreeNode('orange')
    # tree.root.left.left = BinaryTreeNode('green')

    # tree.root.right = BinaryTreeNode('yellow')
    # tree.root.right.left = BinaryTreeNode('violet')

    # tree.print_bfs()
    # tree.print_reverse()

    # Test Case 1 - Prompt 2
    tree.root = BinaryTreeNode(8)

    tree.root.left = BinaryTreeNode(4)
    tree.root.right = BinaryTreeNode(12)

    tree.root.left.left = BinaryTreeNode(2)
    tree.root.left.right = BinaryTreeNode(5)

    tree.root.right.left = BinaryTreeNode(11)
    tree.root.right.right = BinaryTreeNode(14)
    tree.print_bfs()
    print(tree.find_two_sum(9))
