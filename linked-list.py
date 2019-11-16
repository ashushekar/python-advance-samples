"""
A linked list is a sequence of data elements, which are connected together via links.
Each data element contains a connection to another data element in form of a pointer.
Python does not have linked lists in its standard library. We implement the concept of linked lists
using the concept of nodes. Here, We are going to study the types of linked lists known as singly
linked lists. In this type of data structure there is only one link between any two data elements.
We create such a list and create additional methods to insert, update and remove elements from the list.
"""


class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None


class SLinkedList:
    def __init__(self):
        self.headval = None

    def listprint(self):
        """
        Singly linked lists can be traversed in only forward direction starting from
        the first data element. We simply print the value of the next data element by
        assigning the pointer of the next node to the current data element.
        """
        printval = self.headval
        while printval is not None:
            print(printval.dataval, end='-->')
            printval = printval.nextval

    def insertAtbeginning(self, new_element):
        """
        This involves pointing the next pointer of the new data node to the current head
        of the linked list. So the current head of the linked list becomes the second data
        element and the new node becomes the head of the linked list.
        """
        newnode = Node(new_element)
        newnode.nextval = self.headval
        self.headval = newnode

    def insertatEnd(self, new_element):
        """
        This involves pointing the next pointer of the the current last node of the linked
        list to the new data node. So the current last node of the linked list becomes the
        second last data node and the new node becomes the last node of the linked list.
        """
        new_node = Node(new_element)
        traverse = self.headval
        if traverse is None:
            return new_node
        while traverse.nextval:
            traverse = traverse.nextval
        traverse.nextval = new_node

    def insertatMiddle(self, middlenode, new_element):
        """
        This involves changing the pointer of a specific node to point to the new node. That
        is possible by passing in both the new node and the existing node after which the new
        node will be inserted. So we define an additional class which will change the next
        pointer of the new node to the next pointer of middle node. Then assign the new node
        to next pointer of the middle node.
        """
        new_node = Node(new_element)
        traverse = self.headval
        if traverse is None:
            return new_node
        temp = middlenode.nextval
        middlenode.nextval = new_node
        new_node.nextval = temp

    def deleteItem(self, element):
        """
        We can remove an existing node using the key for that node. In the below program we
        locate the previous node of the node which is to be deleted. Then point the next pointer
        of this node to the next node of the node to be deleted.
        """
        if self.headval is None:
            return None
        elif self.headval.dataval == element:
            self.headval = self.headval.nextval
        else:
            traverse = self.headval
            while traverse is not None:
                if traverse.dataval == element:
                    break
                previous = traverse
                traverse = traverse.nextval
            previous.nextval = traverse.nextval


list1 = SLinkedList()
list1.headval = Node('Monday')
e2 = Node('Tuesday')
e3 = Node('Wednesday')

# Link the first node to the second node
list1.headval.nextval = e2
# Link the second node to the third node
e2.nextval = e3

# Traverse
print("\n\nTraversing a Linked List:")
list1.listprint()

# Insertion
print("\n\nInserting at the Beginning of the Linked List:")
list1.insertAtbeginning('Sunday')
list1.listprint()

print("\n\nInserting at the End of the Linked List:")
list1.insertatEnd('Thursday')
list1.listprint()

print("\n\nInserting in between two Data Nodes: ")
list1.insertatMiddle(e2, 'between')
list1.listprint()

# Deleting Node
print("\n\nRemoving an Item from a Linked List: ")
list1.deleteItem('Tuesday')
list1.listprint()
