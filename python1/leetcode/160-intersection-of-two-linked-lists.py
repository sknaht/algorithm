# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """

        a = headA
        b = headB


        while a and b:
            if a == b:
                return a
            a = a.next
            b = b.next
            if a == b == None:
                return None
            if not a:
                a = headB
            if not b:
                b = headA


        return None
