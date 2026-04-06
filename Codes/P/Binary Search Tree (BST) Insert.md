# Binary Search Tree (BST) Insert
=================================
def bst_insert(root, val):
    if not root:
        return TreeNode(val)
    if val < root.val:
        root.left = bst_insert(root.left, val)
    else:
