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
    
    def print_bfs(self):
        if not self.root:
            return

        queue = [self.root]

        while len(queue) > 0:
            current_node = queue.pop(0)
            print(current_node.data)
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
