"""
 Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

You may not alter the values in the nodes, only nodes itself may be changed.

Only constant memory is allowed.

For example,
Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5
"""

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
    def reverseKGroup(self, head, k):

        dummy = ListNode(-1)
        dummy.next = head
        curr_dummy = dummy
        curr = head

        l = 0
        while curr:
            next_cur = curr.next
            l = (l + 1) % k
            if l == 0:
                next_dummy = curr_dummy.next
                self.reverse(curr_dummy, next_cur)
                curr_dummy = next_dummy
            curr = next_cur

        return dummy.next

    def reverse(self, begin, end):
        first = begin.next
        curr = first.next
        while curr != end:
            first.next = curr.next
            curr.next = begin.next
            begin.next = curr
            curr = first.next

if __name__ == "__main__":

    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    print Solution().reverseKGroup(head, 2)



