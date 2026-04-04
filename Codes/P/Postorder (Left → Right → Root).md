# Postorder (Left → Right → Root)
=================================
def postorder(node):
    if not node:
        return
    postorder(node.left)
    postorder(node.right)
