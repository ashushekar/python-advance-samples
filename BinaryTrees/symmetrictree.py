"""
Given a binary tree, check whether it is a mirror of itself.
"""
from introduction import Btree


def mirror(root1, root2):
    if root1 is None and root2 is None:
        return True
    if root1 is not None and root2 is not None:
        if root1.val == root2.val:
            return mirror(root1.left, root2.right) and mirror(root2.left, root1.right)


def issymmetric(node):
    if node.val is None:
        return True

    return mirror(node, node)

tree = Btree(5)

tree.left = Btree(4)
tree.left.left = Btree(3)
tree.left.right = Btree(2)

tree.right = Btree(4)
tree.right.left = Btree(2)
tree.right.right = Btree(3)
tree.right.right.left = Btree(7)
tree.printBtree()

if issymmetric(tree):
    print("\nTree is Symmetric")
else:
    print("\nTree is not Symmetric")
