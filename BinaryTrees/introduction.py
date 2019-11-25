"""
Binary trees:
Properties:
1. The maximum number of nodes at any level l in a Binary tree is 2^(l-1)
example: level = 2 then 2^(2-1) = 2
"""


class Btree:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def printBtree(self):
        if self.left:
            self.left.printBtree()
        print(self.val, end=' ')
        if self.right:
            self.right.printBtree()

    def insert(self, key):
        q = []
        q.append(self)

        while len(q):
            temp = q[0]
            q.pop(0)

            if temp.left is None:
                temp.left = Btree(key)
                break
            else:
                q.append(temp.left)

            if temp.right is None:
                temp.right = Btree(key)
                break
            else:
                q.append(temp.right)


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
