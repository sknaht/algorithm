"""
Given a list, rotate the list to the right by k places, where k is non-negative.

For example:
Given 1->2->3->4->5->NULL and k = 2,
return 4->5->1->2->3->NULL.
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
    # @param {integer} k
    # @return {ListNode}
    def rotateRight(self, head, k):


        if not head: return head

        curr = head
        l = 0
        while curr:
            l += 1
            curr = curr.next
        k = k % l
        dummy = ListNode(-1)
        dummy.next = head
        curr = head
        for i in xrange(k):
            curr = curr.next
            if not curr: return head
        begin = head
        while curr.next:
            begin = begin.next
            curr = curr.next
        if begin.next:
            dummy.next = begin.next
            begin.next = None
            curr.next = head

        return dummy.next


t = ListNode(1)
t.next = ListNode(2)
#t.next.next = ListNode(3)
#t.next.next.next     = ListNode(4)
print Solution().rotateRight(t, 3)

