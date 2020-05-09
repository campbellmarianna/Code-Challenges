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
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        self.xDepth = -1
        self.yDepth = -2
        self.xParent = None
        self.yParent = None

        def dfs(root, parent, x, y, depth):
            if root is None:
                return
            if root.val == x:
                self.xParent = parent
                self.xDepth = depth
            elif root.val == y:
                self.yParent = parent
                self.yDepth = depth
            else:
                dfs(root.left, root, x, y, depth+1)
                dfs(root.right, root, x, y, depth+1)
        dfs(root, None, x, y, 0)
        return self.xDepth == self.yDepth and self.xParent != self.yParent
