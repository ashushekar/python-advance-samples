"""
Implementing binary tree
"""

class Btree:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def printBtree(self):
        if self.left:
            self.left.printBtree()
        print(self.val, end=" ")
        if self.right:
            self.right.printBtree()

    def insert(self, element):
        q = []
        q.append(self)

        while len(q):
            temp = q[0]
            q.pop(0)

            if temp.left is None:
                temp.left = Btree(element)
                break
            else:
                q.append(temp.left)

            if temp.right is None:
                temp.right = Btree(element)
                break
            else:
                q.append(temp.right)

    def printleaves(self):
        if self.left is None and self.right is None:
            print(self.val, end=" ")
        if self.left:
            self.left.printleaves()
        if self.right:
            self.right.printleaves()


def getLeavescount(tree):
    if tree is None:
        return 0
    if tree.left is None and tree.right is None:
        return 1
    else:
        return getLeavescount(tree.left) + getLeavescount(tree.right)


def mirror(tree1, tree2):
    if tree1 is None and tree2 is None:
        return True
    elif tree1 is not None and tree2 is not None:
        return mirror(tree1.left, tree2.right) and mirror(tree1.right, tree1.left)


def issymmetric(a):
    if a.val is None:
        return True
    return mirror(a, a)


def levelordertraversal(tree):
    h = height(tree)
    for i in range(1, h+1):
        printatEachlevel(tree, i)


def printatEachlevel(tree, level):
    if tree is None:
        return
    if level == 1:
        print(tree.val, end=" ")
    elif level > 1:
        printatEachlevel(tree.left, level-1)
        printatEachlevel(tree.right, level-1)


def height(tree):
    if tree is None:
        return 0

    lheight = height(tree.left)
    rheight = height(tree.right)

    if lheight > rheight:
        return lheight + 1
    else:
        return rheight + 1


a = Btree(2)
a.left = Btree(3)
a.left.left = Btree(13)
a.left.right = Btree(14)
a.right = Btree(4)
a.right.left = Btree(25)
a.right.right = Btree(27)
print("Tree before inserting: ")
a.printBtree()
a.insert(132)
print("\n\nTree after inserting: ")
a.printBtree()

if issymmetric(a):
    print("\nTree is Symmetric")
else:
    print("\nTree is not Symmetric")
print("\nLevel Order Traversal: ")
print(levelordertraversal(a))
print("\nLeaves: ")
print(a.printleaves())
print("\nCount of Leaves: ")
print(getLeavescount(a))
