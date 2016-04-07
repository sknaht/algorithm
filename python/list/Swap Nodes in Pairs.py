"""
 Given a linked list, swap every two adjacent nodes and return its head.

For example,
Given 1->2->3->4, you should return the list as 2->1->4->3.

Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed.

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        if self:
            return "{} -> {}".format(self.val, repr(self.next))

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def swapPairs(self, head):
        dummy = ListNode(-1)
        dummy.next = head
        curr = dummy
        next = dummy
        while next.next and next.next.next:
            next = next.next.next
            curr.next.next = next.next
            next.next = curr.next
            curr.next = next

            curr = curr.next.next
            next = curr
        return dummy.next

t = ListNode(1)
t.next = ListNode(2)

print Solution().swapPairs(t)
