"""
Practice problems
"""

class Node:
    def __init__(self, x):
        self.val = x
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtBeginning(self, x):
        newnode = Node(x)
        newnode.next = self.head
        self.head = newnode

    def insertAtmiddle(self, middlenode, x):
        newnode = Node(x)
        if self.head is None:
            self.head = newnode
        else:
            temp = middlenode.next
            middlenode.next = newnode
            newnode.next = temp

    def insertAtend(self, x):
        newnode = Node(x)
        traverse = self.head
        if traverse is None:
            self.head = newnode
        else:
            while traverse.next:
                traverse = traverse.next
            traverse.next = newnode

    def printList(self):
        traverse = self.head
        while traverse is not None:
            print(traverse.val, end=" ")
            traverse = traverse.next

    def findmiddle(self):
        slow = self.head
        fast = self.head

        while slow is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow.val

    def checkcycle(self):
        """
            Check for any cycle present in the linked list
        """
        temp = set()
        traverse = self.head
        while traverse:
            if traverse.val in temp:
                return traverse.val
            temp.add(traverse.val)
            traverse = traverse.next
        return False

    def reverse(self):
        traverse = self.head
        prev = None
        while traverse:
            temp = traverse.next
            traverse.next = prev
            prev = traverse
            traverse = temp
        self.head = prev

    def removeduplicatenodes(self):
        duplicates = []
        traverse = self.head
        prev = None
        while traverse is not None:
            if traverse.val not in duplicates:
                duplicates.append(traverse.val)
                prev = traverse
            else:
                prev.next = traverse.next
                traverse = prev
            traverse = traverse.next

    def sumLinkedlist(self, c):
        first = self.head
        second = c.head
        a = ""
        while first is not None:
            a += str(first.val)
            first = first.next

        b = ""
        while second is not None:
            b += str(second.val)
            second = second.next

        result = int(a) + int(b)
        r = LinkedList()
        for char in str(result):
            r.insertAtend(char)
        print('\n')
        r.printList()


a = LinkedList()
a.insertAtBeginning(10)
a.insertAtBeginning(5)
a.insertAtend(20)
a.insertAtend(30)
a.insertAtend(10)
a.insertAtend(50)
a.insertAtBeginning(50)

a.printList()
print("\n")
print(a.findmiddle())
print(a.checkcycle())
a.reverse()
print("\n")
a.printList()
a.removeduplicatenodes()
print("\n")
a.printList()

b = LinkedList()
b.insertAtend(5)
b.insertAtend(6)
b.insertAtend(3)
c = LinkedList()
c.insertAtend(8)
c.insertAtend(4)
c.insertAtend(2)
b.sumLinkedlist(c)

