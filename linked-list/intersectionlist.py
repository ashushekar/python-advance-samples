"""
Write a program to find the node at which the intersection of two singly linked lists begins.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if headA is None or headB is None:
            return None

        ptrA = headA
        ptrB = headB

        lenA = 0
        while ptrA is not None:
            lenA += 1
            ptrA = ptrA.next

        lenB = 0
        while ptrB is not None:
            lenB += 1
            ptrB = ptrB.next

        ptrA = headA
        ptrB = headB

        if lenA > lenB:
            for _ in range(lenA - lenB):
                ptrA = ptrA.next
        else:
            for _ in range(lenB - lenA):
                ptrB = ptrB.next

        while ptrA != ptrB:
            ptrA = ptrA.next
            ptrB = ptrB.next

        return ptrA
