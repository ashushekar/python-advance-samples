"""
Splitting the linked list by x.
Given a linked list and a value x, partition it such that all nodes less than
x come before nodes greater than or equal to x.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        before = bhead = ListNode(0)
        after = ahead = ListNode(0)

        while head:
            if head.val < x:
                before.next = head
                before = before.next
            else:
                after.next = head
                after = after.next

            head = head.next

        after.next = None
        before.next = ahead.next
        return bhead.next

