"""
Create Singly linkedlist and insert and delete elements from it
"""


class SlinkedListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class SlinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        item = self.head
        while item is not None:
            print(item.val, end='-->')
            item = item.next

    def insertAtBeginning(self, element):
        newnode = SlinkedListNode(element)
        newnode.next = self.head
        self.head = newnode

    def insertAtEnd(self, element):
        newnode = SlinkedListNode(element)
        traverse = self.head
        if traverse is None:
            self.head = newnode
        else:
            while traverse.next:
                traverse = traverse.next
            traverse.next = newnode

    def insertAtmiddle(self, middlenode, element):
        newnode = SlinkedListNode(element)
        traverse = self.head
        if traverse is None:
            self.head = newnode
        else:
            temp = middlenode.next
            middlenode.next = newnode
            newnode.next = temp


# a = SlinkedList()
# a.insertAtBeginning(10)
# a.insertAtEnd(20)
# a.insertAtEnd(30)
#
# a.printList()


