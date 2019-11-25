class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None


class SLinkedList:
    def __init__(self):
        self.headval = None

    def listprint(self):
        printval = self.headval
        while printval is not None:
            print(printval.dataval, end='-->')
            printval = printval.nextval

    def insertAtbeginning(self, new_element):
        newnode = Node(new_element)
        newnode.nextval = self.headval
        self.headval = newnode

    # def insertatEnd(self, new_element):
    #     new_node = Node(new_element)
    #     traverse = self.headval
    #     if traverse is None:
    #         return new_node
    #     while traverse.nextval:
    #         traverse = traverse.nextval
    #     traverse.nextval = new_node
    #
    # def insertatMiddle(self, middlenode, new_element):
    #     new_node = Node(new_element)
    #     traverse = self.headval
    #     if traverse is None:
    #         return new_node
    #     temp = middlenode.nextval
    #     middlenode.nextval = new_node
    #     new_node.nextval = temp



list1 = SLinkedList()
list1.headval = Node('Monday')
e2 = Node('Tuesday')
e3 = Node('Wednesday')

list1.headval.nextval = e2
e2.nextval = e3

print("\n\nTraversing a Linked List:")
list1.listprint()

print("\n\nInserting at the Beginning of the Linked List:")
list1.insertAtbeginning('Sunday')
list1.listprint()


list2 = SLinkedList()
list2.headval = Node('January')
list2.insertAtbeginning('February')
list2.listprint()
# print("\n\nInserting at the End of the Linked List:")
# list1.insertatEnd('Thursday')
# list1.listprint()
#
# print("\n\nInserting in between two Data Nodes: ")
# list1.insertatMiddle(e2, 'between')
# list1.listprint()

