"""
Given a singly linked list where elements are sorted in ascending order,
convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in
which the depth of the two subtrees of every node never differ by more than 1.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if head is None:
            return None
        values = self.get_values(head)
        return self.buildBST(values, 0, len(values)-1)

    def get_values(self, head):
        values = []
        while head is not None:
            values.append(head.val)
            head = head.next
        return values

    def buildBST(self, values, start, end):
        if start > end:
            return None
        if start == end:
            return TreeNode(values[start])
        mid = int((start+end)/2)
        root = TreeNode(values[mid])
        root.left = self.buildBST(values, start, mid-1)
        root.right = self.buildBST(values, mid+1, end)

        return root


a = ListNode(-10)
a.next = ListNode(-3)
a.next.next = ListNode(0)
a.next.next.next = ListNode(5)
a.next.next.next.next = ListNode(9)

b = Solution()
print(b.sortedListToBST(a))


