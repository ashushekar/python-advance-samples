"""
Using Stack is the obvious way to traverse tree without recursion. Below is an algorithm for
traversing binary tree using stack.
"""

from introduction import Btree


def traversal(root):
    current = root
    stack = []

    while True:
        if current is not None:
            stack.append(current)
            current = current.right

        elif stack:
            current = stack.pop()
            print(current.val, end=" ")
            current = current.left

        else:
            break


tree = Btree(5)

tree.left = Btree(4)
tree.left.left = Btree(3)
tree.left.right = Btree(2)

tree.right = Btree(4)
tree.right.left = Btree(2)
tree.right.right = Btree(3)
tree.right.right.left = Btree(7)

traversal(tree)
