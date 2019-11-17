"""
Tree represents the nodes connected by edges. It is a non-linear data structure.
It has the following properties.

    1. One node is marked as Root node.
    2. Every node other than the root is associated with one parent node.
    3. Each node can have an arbiatry number of chid node.

We create a tree data structure in python by using the concept os node.
We designate one node as root node and then add more nodes as child nodes.
Below is program to create the root node.
"""


class Node:
    """
        We just create a Node class and add assign a value to the node.
        This becomes tree with only a root node.
    """
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.data)
        if self.right:
            self.right.printTree()

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def findval(self, data):
        if data < self.data:
            if self.left is None:
                print("{} Not Found".format(data))
            else:
                self.left.findval(data)
        elif data > self.data:
            if self.right is None:
                print("{} Not Found".format(data))
            else:
                self.right.findval(data)
        else:
            print("{} Found.".format(data))


root = Node(10)
root.insert(12)
root.insert(-2)
root.insert(100)
root.insert(-50)
root.printTree()
root.findval(20)
root.findval(12)
