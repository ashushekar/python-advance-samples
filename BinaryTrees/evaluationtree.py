"""
Given a simple expression tree, consisting of basic binary operators
i.e., + , – ,* and / and some integers, evaluate the expression tree.
"""
from introduction import Btree

tree = Btree('+')

tree.left = Btree('*')
tree.left.left = Btree('-')
tree.left.left.left = Btree(22)
tree.left.left.right = Btree(60)
tree.left.right = Btree(4)

tree.right = Btree('-')
tree.right.left = Btree(100)
tree.right.right = Btree(20)
tree.printBtree()


def evaluate(root):
    if root is None:
        return 0

    if root.left is None and root.right is None:
        return int(root.val)

    evaluateleft = evaluate(root.left)
    evaluateright = evaluate(root.right)

    if root.val == '+':
        return evaluateleft + evaluateright
    if root.val == '*':
        return evaluateleft * evaluateright
    if root.val == '-':
        return evaluateleft - evaluateright


result = evaluate(tree)
print("\nEvaluation output is: {}".format(result))
