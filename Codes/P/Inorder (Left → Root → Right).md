# Inorder (Left → Root → Right)
===============================
def inorder(node):
    if not node:
        return
    inorder(node.left)
    print(node.val, end=" ")
    inorder(node.right)
