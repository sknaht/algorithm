"""
Given a linked list, remove the nth node from the end of list and return its head.

For example,

   Given linked list: 1->2->3->4->5, and n = 2.

   After removing the second node from the end, the linked list becomes 1->2->3->5.

Note:
Given n will always be valid.
Try to do this in one pass.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        if self:
            return "{} -> {}".format(self.val, repr(self.next))

class Solution:
    # @param {ListNode} head
    # @param {integer} n
    # @return {ListNode}
    def removeNthFromEnd(self, head, n):

        dummy = ListNode(-1)
        dummy.next = head
        curr, next = dummy, dummy
        while n > 0 and next:
            next = next.next
            n -= 1
        while next.next:
            next = next.next
            curr = curr.next
        curr.next = curr.next.next
        return dummy.next


t = ListNode(1)
t.next = ListNode(2)
t.next.next = ListNode(3)
t.next.next.next = ListNode(4)
t.next.next.next.next = ListNode(5)

print Solution().removeNthFromEnd(t, 5)