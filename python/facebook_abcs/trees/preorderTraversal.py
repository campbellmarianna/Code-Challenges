'''
Prompt:
'''
# JAVA
struct Node {
  int data;
  Node* left;
  Node* right;
};

void preOrder(Node* root) {
  if (root = numptr)
    return;
  count << root -> data << " "
  preOrder(root -> left)
  preOrder(root -> right)
  
}
output_list = []
def preOrder(root):
  '''Traverse this binary tree with recursive pre-order traversal (DFS).
  Running time: O(n) for nodes we traverse through all nodes in the tree
  Memory usage: O(h) for the height of the tree'''
  if root == None:
    return;
  print(str(root.info), end=' ')
  if root.left:
    preOrder(root.left)
  if root.right:
    preOrder(root.right)

  

