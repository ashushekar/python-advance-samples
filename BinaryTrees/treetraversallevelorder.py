"""
Level order traversal of a tree is breadth first traversal for the tree.

There are basically two functions in this method. One is to print all nodes
at a given level (printGivenLevel), and other is to print level order traversal
of the tree (printLevelorder).

printLevelorder makes use of printGivenLevel to print nodes at all levels one
by one starting from root.
"""

from introduction import Btree


def traversal(node):
    h = heightoftree(node)
    for i in reversed(range(1, h+1)):
        printEachlevel(node, i)


def printEachlevel(node, level):
    if node is None:
        return
    if level == 1:
        print(node.val, end=" ")
    elif level > 1:
        printEachlevel(node.left, level-1)
        printEachlevel(node.right, level-1)


def heightoftree(node):
    if node is None:
        return 0

    lheight = heightoftree(node.left)
    rheight = heightoftree(node.right)

    if lheight > rheight:
        return lheight + 1
    else:
        return rheight + 1


tree = Btree(5)

tree.left = Btree(4)
tree.left.left = Btree(3)
tree.left.right = Btree(2)

tree.right = Btree(4)
tree.right.left = Btree(2)
tree.right.right = Btree(3)
tree.right.right.left = Btree(7)

print(traversal(tree))
