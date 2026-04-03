# Tree Traversals
=================
def preorder(node):
    if not node:
        return
    print(node.val, end=" ")
    preorder(node.left)
    preorder(node.right)
