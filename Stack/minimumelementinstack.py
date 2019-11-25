"""
Design a stack which returns minimum element in constant time
"""

class StackNode:
    # Constructor to initialize the node
    def __init__(self, val):
        self.val = val
        self.next = None


class Stack:
    def __init__(self):
        self.rootmain = None
        self.rootaux = None

    def isemptymain(self):
        return self.rootmain is None

    def isemptyaux(self):
        return self.rootaux is None

    def pushmain(self, element):
        new = StackNode(element)
        new.next = self.rootmain
        self.rootmain = new

    def pushaux(self, element):
        new = StackNode(element)
        new.next = self.rootaux
        self.rootaux = new

    def popmain(self):
        if self.isemptymain():
            return float("-inf")
        temp = self.rootmain
        self.rootmain = self.rootmain.next
        return temp.val

    def popaux(self):
        if self.isemptyaux():
            return float("-inf")
        temp = self.rootaux
        self.rootaux = self.rootaux.next
        print(temp.val)
        return temp.val

    def pushboth(self, element):
        self.pushmain(element)
        if self.isemptyaux() or self.peekaux() >= element:
            self.pushaux(element)

    def popboth(self):
        mainelement = self.popmain()
        if self.peekaux() == mainelement:
            result = self.popaux()
            return result
        return

    def peekmain(self):
        if self.isemptymain():
            return float("-inf")
        return self.rootmain.val

    def peekaux(self):
        if self.isemptyaux():
            return float("-inf")
        return self.rootaux.val


stack = Stack()
stack.pushboth(10)
stack.pushboth(20)
stack.pushboth(-2)
stack.pushboth(5)

print(stack.popboth())
