'''
In a binary tree, the root node is at depth 0, and children of each depth k node are at depth k+1.

Two nodes of a binary tree are cousins if they have the same depth, but have different parents.

We are given the root of a binary tree with unique values, and the values x and y of two different nodes in the tree.

Return true if and only if the nodes corresponding to the values x and y are cousins.
'''
# Given a binary tree return a bool if the given x and y values in the binary tree have the same depth and different parents.

# Assume valid input, tree has aleast to nodes
# Assume valid input, not given x or y that is not in the Binary Tree
# Are the x and y values always going to be found in the tree? Yes
# No the tree is not balanced'
# Are the nodes in order

# Solution Idea - In Progress

# create a dictionary [node_val: depth]
# traverse the tree and record the data
# access the depth of x and y and compare them
# Time Complexity: 0(n) n for nodes
# Space Complexity: O(n)

#
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        # create a dictionary [node_val: depth]
        node_to_depth = dict()
        # traverse the tree and record the data
        root = node
        if node is not None:

            # access the depth of x and y and compare them

class Solution:
    def isCousins(root, x, y):
        self.xDepth = -2
        self.yDepth = -1
        self.xParent = None
        self.yParent = None
        def dfs(root, parent, x, y, depth):
            if root == None:
                return
            if root.val == x:
                self.xDepth = depth
                self.xParent = parent
            elif root.val == y:
                self.yDepth = depth
                self.yParent = parent
            else:
                dfs(root.left, root, x, y, depth+1)
                dfs(root.right, root, x, y, depth+1)
        dfs(root, None, x, y, 0)
        return self.xDepth == self.yDepth and self.xParent != self.yParent


