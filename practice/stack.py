"""
implementing stack examples
"""


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class StackNode:
    def __init__(self):
        self.root = None

    def push(self, element):
        newnode = Node(element)
        newnode.next = self.root
        self.root = newnode

    def isempty(self):
        if self.root is None:
            return True
        return False

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


def balancedparenthsis(str):
    st = StackNode()
    open = ["[", "{", "("]
    close = ["]", "}", ")"]
    for i in str:
        if i in open:
            st.push(i)
        elif i in close:
            pos = close.index(i)
            if not st.isempty() and open[pos] == st.peek():
                st.pop()
            else:
                return "Unbalanced"
    return "Balanced"


def findDuplicateparenthesis(str):
    st = StackNode()
    for i in str:
        if i == ')':
            top = st.pop()
            counter = 0
            while top != '(':
                top = st.pop()
                counter += 1
            if counter == 0:
                return True
        else:
            st.push(i)
    return False


stack = StackNode()
stack.push(str(10))
stack.push(str(20))
stack.push(str(40))
stack.push(str(50))
print("\nElement in Stack: {}".format(stack.peek()))

# print("Element popped: {}".format(stack.pop()))
# print("Element popped: {}".format(stack.pop()))
# print("Element popped: {}".format(stack.pop()))
# print("Element popped: {}".format(stack.pop()))
print(balancedparenthsis(")[{}{}]"))
print(findDuplicateparenthesis("((a+b))"))
