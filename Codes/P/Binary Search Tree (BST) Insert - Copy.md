# Binary Search Tree (BST) Insert
=================================
def bst_insert(root, val):
    if not root:
        return TreeNode(val)
    if val < root.val:
        root.left = bst_insert(root.left, val)
    else:
        root.right = bst_insert(root.right, val)
    return root

root = TreeNode(10)
bst_insert(root, 5)
bst_insert(root, 15)