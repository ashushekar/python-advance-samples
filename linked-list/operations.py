"""
1. How do you find the middle element of a singly linked list in one pass?
2. Reverse linked list without recursion
3. How are duplicate nodes removed in an unsorted linked list?
4. How do you check if a given linked list contains a cycle? How do you
find the starting node of the cycle?
5. How do you find the third node from the end in a singly linked list?
6. How do you find the sum of two linked lists using Stack?
7. How to remove Nth Node from the end of a linked list?
8. How to add an element at the middle of the linked list?
9. How to remove all elements from a linked list of integers which matches
with given value?
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

    def insertAtEnd(self, element):
        newnode = SlinkedListNode(element)
        traverse = self.head
        if traverse is None:
            self.head = newnode
        else:
            while traverse.next:
                traverse = traverse.next
            traverse.next = newnode

    def getmiddle(self):
        """
            Print middle element of a linked list
        """
        slow = self.head
        fast = self.head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        print("\nMiddle element is: {}".format(slow.val))

    def reverse(self):
        """
        Reverse the linked list
        """
        prev = None
        traverse = self.head
        while traverse is not None:
            temp = traverse.next
            traverse.next = prev
            prev = traverse
            traverse = temp
        self.head = prev

    def removeduplicatenodes(self):
        """
            Remove duplicate nodes from linked list
        """
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

    def checkcycle(self):
        """
            Check for any cycle present in the linked list
        """
        slow = self.head
        fast = self.head
        while slow is not None and fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow.val == fast.val:
                print("\nFound Loop")
        print("\nNo Loop Found")

    def findthirdlastnode(self):
        """
        Find the third last node of linked list
        """
        traverse = self.head
        length = 0
        while traverse is not None:
            traverse = traverse.next
            length += 1
        current = self.head
        for i in range(length - 3):
            current = current.next
        print("\nThe third last element is: {}".format(current.val))

    def sumLinkedlist(self, c):
        """
            Sum of two linked list
        """
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
        r = SlinkedList()
        for char in str(result):
            r.insertAtEnd(char)
        r.printList()

    def removenthnode(self, n):
        """
            Removes Nth node from the linked list
        """
        first = self.head
        second = self.head
        for i in range(n):
            if second.next is None:
                if i == n - 1:
                    self.head = self.head.next
                return self.head
            second = second.next

        while second.next is not None:
            second = second.next
            first = first.next
        first.next = first.next.next

    def insertAtMiddle(self, element):
        """
            Inserting element at the middle of the linked list
        """
        newnode = SlinkedListNode(element)
        middle = self.head
        fast = self.head

        while fast is not None and fast.next is not None:
            prev = middle
            middle = middle.next
            fast = fast.next.next

        temp = prev.next
        prev.next = newnode
        newnode.next = temp

    def removeelementmatchingX(self, element):
        """
            Remove all elements from a linked list of integers which matches
            with given value x
        """
        traverse = self.head
        if self.head is None:
            return None
        elif self.head.val == element:
            self.head = self.head.next
            return None

        previous = self.head
        while traverse is not None:
            if traverse.val == element:
                previous.next = traverse.next
            previous = traverse
            traverse = traverse.next


a = SlinkedList()
a.insertAtEnd(10)
a.insertAtEnd(20)
a.insertAtEnd(30)
a.insertAtEnd(40)
a.insertAtEnd(100)
a.printList()

# 1. Get the middle element
a.getmiddle()

# 2. Reverse the linked list without recursion
a.reverse()
a.printList()

# 3. Remove duplicate nodes from linked list
a.insertAtEnd(-2)
a.insertAtEnd(12)
a.insertAtEnd(201)
a.insertAtEnd(19)
a.insertAtEnd(12)
a.insertAtEnd(10)
print("\nLinked List with Duplicates: ")
a.printList()
a.removeduplicatenodes()
print("\nLinked List without Duplicates: ")
a.printList()

# 4. Check linklist contains cycle or not
a.insertAtEnd(20)
a.insertAtEnd(10)
print("\nLinked List: ")
a.printList()
a.checkcycle()

# 5. Find the third node from the end in a singly linked list
a.printList()
a.findthirdlastnode()

# 6. Find the sum of two linked lists using Stack
b = SlinkedList()
b.insertAtEnd(5)
b.insertAtEnd(6)
b.insertAtEnd(3)
c = SlinkedList()
c.insertAtEnd(8)
c.insertAtEnd(4)
c.insertAtEnd(2)
b.sumLinkedlist(c)

# 7. Remove Nth node from a linked list
n = 4
a.removenthnode(n)
print('\n')
a.printList()

# 8. Add an element at the middle of the linked list
a.insertAtMiddle(-33)
print('\n')
a.printList()

# 9. Remove element from linked list which matches with given value
a.removeelementmatchingX(100)
print('\n')
a.printList()
