# Given two binary trees return true if the trees are the same and false others. The two binary trees are the same if the nodes have the same values and they are in the same order.
# sorted order

# Solution Ideas
# traverse trees one by one and get node values in a lists then compare lists 
    # Time Complexity: 0(n) + 0(m), n for nodes in first tree and m for second tree
    # Space Complexity: 0(m) + 0(n), stores every node value from both trees
# traverse trees at the same time and compare node values as we go
    # Time Comlexity: 0(n)
    # Space Complexity: 0(1)
    
# Assumptions:
# - given valid trees
# - non empty trees

# Edge Cases
# - empty tree

# Idea #1 Psudeocode
# create vals_1 list
# traverse the tree1
    # store node values
# create vals_2 list
# traverse the tree2
    # store node values
# compare list
    # True
# otherwise false

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.first_tree_values = [] 
        self.second_tree_values = [] 
        
    def in_order_traversal_first(self, curr_tree: TreeNode) -> list:
        '''Add values from a given tree to first_tree_values list (class property), in order.'''
        if curr_tree.val:
            self.first_tree_values.append(curr_tree.val)
        else:
            self.first_tree_values.append('None')
        if curr_tree.left:
            self.in_order_traversal_first(curr_tree.left)
        else: 
            self.first_tree_values.append('None')
        if curr_tree.right:
            self.in_order_traversal_first(curr_tree.right)
        else: 
            self.first_tree_values.append('None')
            
    def in_order_traversal_second(self, curr_tree: TreeNode) -> list:
        '''Add values from a given tree to second_tree_values list (class property), in order.'''
        if curr_tree.val:
            self.second_tree_values.append(curr_tree.val)
        else:
            self.second_tree_values.append('None')
        if curr_tree.left:
            self.in_order_traversal_second(curr_tree.left)
        else:
            self.second_tree_values.append('None')
        if curr_tree.right:
            self.in_order_traversal_second(curr_tree.right)
        else:
            self.second_tree_values.append('None')
            
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool: 
        # Edge cases: Empty trees, One empty Tree
        if p == None and q == None:
            return True
        if p == None or q == None:
            return False
        self.in_order_traversal_first(p)
        self.in_order_traversal_second(q)
        # compare lists
        if self.first_tree_values == self.second_tree_values:
            return True
        return False

# Suggest Improvements
# - only have one helper function instead of two (both have the same code) to reduce memory usage
# compare the lengths of the lists and return False if they are different lengths before comparing the list values can save time
    