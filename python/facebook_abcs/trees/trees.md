Inorder traversal
```python
class Node: 
  left = None
  right = None
  def __init__(self, data):
    self.data = data

  def in_order(root: Node):
  if root is None:
    return
  inOrder(root.left)
  print(root.data, ' ')
  inOrder(root.right)
```