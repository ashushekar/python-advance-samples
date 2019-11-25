"""
# Python program for implementation of stack
push(), pop(), isEmpty() and peek() all take O(1) time. We do not run any loop in any of these operations.
"""


class StackNode:
    # Constructor to initialize the node
    def __init__(self, val):
        self.val = val
        self.next = None


class Stack:
    def __init__(self):
        self.root = None

    def isempty(self):
        return self.root is None

    def push(self, element):
        new = StackNode(element)
        new.next = self.root
        self.root = new
        print("%s element pushed." % element)

    def pop(self):
        if self.isempty():
            return float("-inf")
        temp = self.root
        self.root = self.root.next
        return temp.val

    def peek(self):
        if self.isempty():
            return float("-inf")
        return self.root.val


stack = Stack()
stack.push(str(10))
stack.push(str(20))
stack.push(str(40))
stack.push(str(50))
print("\nElement in Stack: {}".format(stack.peek()))

print("Element popped: {}".format(stack.pop()))
print("Element popped: {}".format(stack.pop()))
print("Element popped: {}".format(stack.pop()))
print("Element popped: {}".format(stack.pop()))
