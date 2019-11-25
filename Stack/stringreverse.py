"""
String Reverse using Stack
"""


class StackNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class Stack:
    def __init__(self):
        self.root = None

    def isempty(self):
        return self.root is None

    def push(self, element):
        newnode = StackNode(element)
        newnode.next = self.root
        self.root = newnode

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


input_string = "ABCDE"
stack = Stack()
for char in input_string:
    stack.push(char)

result = []
for _ in range(len(input_string)):
    result.append(stack.pop())

print(''.join(result))
